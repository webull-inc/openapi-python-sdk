# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
import json
import logging
import threading
import time

import grpc
from webullsdkcore.common import api_type
from webullsdkcore.endpoint.default_endpoint_resolver import \
    DefaultEndpointResolver
from webullsdkcore.endpoint.resolver_endpoint_request import \
    ResolveEndpointRequest
from webullsdkcore.retry.retry_condition import RetryCondition

import webullsdktradeeventscore.events_pb2 as pb
import webullsdktradeeventscore.events_pb2_grpc as pb_grpc
from webullsdktradeeventscore.default_retry_policy import (
    DefaultSubscribeRetryPolicy, SubscribeRetryPolicyContext)
from webullsdktradeeventscore.signature_composer import calc_signature

# contentTypes
JSON = "application/json"
TEXT = "text/plain"

DEFAULT_REGION_ID = "us"


class EventsClient():
    def __init__(self, app_key, app_secret, region_id=DEFAULT_REGION_ID, host=None, port=443, tls_enable=True, retry_policy=None):
        self._app_key = app_key
        self._app_secret = app_secret
        self._region_id = region_id
        self._tls_enable = tls_enable
        self._endpoint_resolver = DefaultEndpointResolver(self)
        if not host:
            endpoint_request = ResolveEndpointRequest(
                self._region_id, api_type=api_type.EVENTS)
            endpoint = self._endpoint_resolver.resolve(endpoint_request)
            self._host = endpoint
        else:
            self._host = host
        self._port = port
        if retry_policy:
            self._retry_policy = retry_policy
        else:
            self._retry_policy = DefaultSubscribeRetryPolicy()

        self._logger = None
        self._in_callback_mutex = threading.Lock()
        self._callback_mutex = threading.RLock()
        # callbacks
        self._on_connect = None
        self._on_events_message = None
        self._on_log = None

    def _build_request(self, app_key, app_secret, accounts):
        request = pb.SubscribeRequest(
            subscribeType=1,  # only 1 allowed now
            timestamp=int(time.time() * 1000),  # millis
            accounts=accounts,
        )
        signature, metadata = calc_signature(app_key, app_secret, request)
        return request, metadata

    def _stream_processing(self, stub, accounts):
        retry_policy_context = SubscribeRetryPolicyContext(None, 0, None)
        retries = 0
        final_exception = None
        while True:
            request, metadata = self._build_request(
                self._app_key, self._app_secret, accounts)
            try:
                response_iterator = stub.Subscribe(
                    request=request, metadata=metadata)
                for response in response_iterator:
                    self._easy_handler(response)
            except grpc.RpcError as rpc_error:
                state = rpc_error._state
                final_exception = rpc_error
                retry_policy_context = SubscribeRetryPolicyContext(
                    None, retries, state.code)
                self._easy_log(logging.ERROR, "grpc error code:%s, error msg:%s, details:%s",
                               state.code, state.details, state.debug_error_string)
            except Exception as exception:
                final_exception = exception
                retry_policy_context = SubscribeRetryPolicyContext(
                    exception, retries, None)
                self._easy_log(logging.ERROR, "grpc exception:%s", exception)
            retryable = self._retry_policy.should_retry(retry_policy_context)
            if retryable & RetryCondition.NO_RETRY:
                self._easy_log(
                    logging.ERROR, "processing will stopped due to not be retryable, retry_context:%s", retry_policy_context)
                break
            retry_policy_context.retryable = retryable
            time_to_sleep = self._retry_policy.compute_delay_before_next_retry(
                retry_policy_context)
            self._easy_log(logging.INFO, "next retry will be started in %s ms, retry_context:%s",
                           time_to_sleep, retry_policy_context)
            time.sleep(time_to_sleep / 1000.0)
            retries += 1
            retry_policy_context.retries_attempted = retries
        if final_exception:
            raise final_exception

    @property
    def on_connect(self):
        return self._on_connect

    @on_connect.setter
    def on_connect(self, func):
        with self._callback_mutex:
            self._on_connect = func

    @property
    def on_events_message(self):
        return self._on_events_message

    @on_events_message.setter
    def on_events_message(self, func):
        with self._callback_mutex:
            self._on_events_message = func

    @property
    def on_log(self):
        return self._on_log

    @on_log.setter
    def on_log(self, func):
        self._on_log = func

    def _easy_log(self, level, fmt, *args):
        if self.on_log is not None:
            buf = fmt % args
            try:
                self.on_log(level, buf)
            except Exception:
                pass
        if self._logger is not None:
            self._logger.log(level, fmt, *args)

    def enable_logger(self, logger=None):
        if logger is None:
            if self._logger is not None:
                return
            logger = logging.getLogger(__name__)
        self._logger = logger

    def disable_logger(self):
        self._logger = None

    def _handle_subscribe_success(self, response):
        self._easy_log(
            logging.INFO, "subscribe success, response:%s", response)
        with self._callback_mutex:
            on_connect = self.on_connect
        if not on_connect:
            return
        with self._in_callback_mutex:
            try:
                on_connect(self, response.payload, response)
            except Exception as err:
                self._easy_log(
                    logging.ERROR, 'Caught exception in on_connect: %s', err)
                raise err

    def _handle_default(self, response, level):
        self._easy_log(level, "response:%s", response)

    def _handle_message(self, response):
        self._easy_log(
            logging.DEBUG, "message received, response:%s", response)
        with self._callback_mutex:
            on_events_message = self.on_events_message
        if not on_events_message:
            return
        with self._in_callback_mutex:
            content_type = response.contentType
            _payload = response.payload
            if JSON == content_type:
                try:
                    _payload = json.loads(response.payload)
                except Exception as err:
                    self._easy_log(
                        logging.ERROR, 'Caught exception in decode message: %s, %s', _payload, err)
                    raise err
            try:
                on_events_message(response.eventType,
                                  response.subscribeType, _payload, response)
            except Exception as err:
                self._easy_log(
                    logging.ERROR, 'Caught exception in on_events_message: %s', err)
                raise err

    def _easy_handler(self, response):
        event_type = response.eventType
        if event_type == pb.SubscribeSuccess:
            self._handle_subscribe_success(response)
        elif event_type == pb.Ping:
            self._handle_default(response, logging.DEBUG)
        elif event_type == pb.AuthError:
            self._handle_default(response, logging.FATAL)
        elif event_type == pb.NumOfConnExceed:
            self._handle_default(response, logging.FATAL)
        elif event_type == pb.SubscribeExpired:
            self._handle_default(response, logging.FATAL)
        else:
            self._handle_message(response)

    def do_subscribe(self, accounts):
        target = self._host + ":" + str(self._port)
        if self._tls_enable:
            ssl_channel_credentials = grpc.ssl_channel_credentials()
            with grpc.secure_channel(target, ssl_channel_credentials) as channel:
                stub = pb_grpc.EventServiceStub(channel)
                self._stream_processing(stub, accounts)
        else:
            with grpc.insecure_channel(target) as channel:
                stub = pb_grpc.EventServiceStub(channel)
                self._stream_processing(stub, accounts)
