# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8

import concurrent
import logging
import threading

import grpc
from webullsdkcore import compat
import webullsdkquotescore
from webullsdkcore.common import api_type
from webullsdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver
from webullsdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from webullsdkquotescore.grpc.grpc_retry_policy import DefaultSubscribeRetryPolicy
from webullsdkquotescore.grpc import error
from webullsdkquotescore.grpc.connect import Connect
from webullsdkquotescore.grpc.msg import Msg
from webullsdkquotescore.grpc.pb import gateway_pb2 as pb

DEFAULT_REGION_ID = "us"
logger = logging.getLogger(__name__)


class GrpcApiClient(object):
    _instance_lock = threading.Lock()

    _init_connect_lock = threading.Lock()

    def __init__(self,
                 app_key,
                 app_secret,
                 region_id=DEFAULT_REGION_ID,
                 host=None,
                 port=443,
                 read_timeout=10,
                 cache_timeout=120,
                 tls_enable=True,
                 retry_policy=None,
                 daemon=False,
                 downgrade_message=None):

        if not hasattr(self, '_connect'):
            with GrpcApiClient._init_connect_lock:
                if not hasattr(self, '_connect'):
                    self.read_timeout = read_timeout
                    self._retry_policy = retry_policy if retry_policy else DefaultSubscribeRetryPolicy()

                    def _provide_endpoint():
                        endpoint_resolver = DefaultEndpointResolver(self)
                        endpoint_request = ResolveEndpointRequest(region_id,
                                                                  api_type.QUOTES)
                        return endpoint_resolver.resolve(endpoint_request)

                    self._host = host if host is not None else _provide_endpoint()

                    self._connect = Connect(app_key, app_secret, region_id, self._host, port, cache_timeout, tls_enable,
                                            self._retry_policy, daemon)
                    if downgrade_message:
                        self._connect.on_downgrade_message(downgrade_message)
                    self._connect.run()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with GrpcApiClient._instance_lock:
                if not hasattr(cls, '_instance'):
                    GrpcApiClient._instance = super().__new__(cls)
        return GrpcApiClient._instance

    def stop(self):
        if self._connect:
            self._connect.stop()

    def __del__(self):
        self.stop()

    def get_response(self, path, payload, timeout=None):
        _read_time_out = timeout if timeout else self.read_timeout
        msg = Msg(pb.Payload, path, payload)
        self._connect.request(msg)
        try:
            result = msg.get_future().result(_read_time_out)
            if isinstance(result, Exception) or isinstance(result, grpc.RpcError):
                raise result
            return result
        except concurrent.futures._base.TimeoutError as e:
            exception = self._connect.get_exception()
            if exception:
                raise exception

            msg = "gRPC request exception. Host:%s SDK-Version:%s ClientException:%s" % (
                self._host, webullsdkquotescore.__version__, e)
            logger.error(compat.ensure_string(msg))
            raise TimeoutError(error.REQUEST_TIMEOUT, "Request timed out, please try again!")

    def set_stream_logger(self, log_level=logging.DEBUG, logger_name='webullsdkquotescore', stream=None,
                          format_string=None):
        log = logging.getLogger(logger_name)
        log.setLevel(log_level)
        ch = logging.StreamHandler(stream)
        ch.setLevel(log_level)
        if format_string is None:
            format_string = self.LOG_FORMAT
        formatter = logging.Formatter(format_string)
        ch.setFormatter(formatter)
        log.addHandler(ch)

    def set_file_logger(self, path, log_level=logging.DEBUG, logger_name='webullsdkquotescore', format_string=None):
        log = logging.getLogger(logger_name)
        log.setLevel(log_level)
        fh = logging.FileHandler(path)
        fh.setLevel(log_level)
        if format_string is None:
            format_string = self.LOG_FORMAT
        formatter = logging.Formatter(format_string)
        fh.setFormatter(formatter)
        log.addHandler(fh)
