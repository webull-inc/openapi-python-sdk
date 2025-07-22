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

import grpc
import logging
import threading
from datetime import timedelta, datetime
import time

from webullsdkcore import compat
import webullsdkquotescore
from webullsdkcore.cache import MsgCache
from webullsdkquotescore.exceptions import ExitedException
from webullsdkquotescore.grpc.core import ResumableBidiRpc, BackgroundConsumer
from webullsdkquotescore.grpc.error import ExceptionContext
from webullsdkquotescore.grpc.msg import Msg
from webullsdkquotescore.grpc.retry import Retry
from webullsdkquotescore.grpc.pb import gateway_pb2 as pb
from webullsdkquotescore.grpc.pb import gateway_pb2_grpc as pb_grpc
from webullsdkquotescore.grpc.task.task_timer import TaskTimer

logger = logging.getLogger(__name__)


class Connect(object):

    def __init__(self,
                 app_key,
                 app_secret,
                 region_id=None,
                 host=None,
                 port=443,
                 cache_timeout=120,
                 tls_enable=True,
                 retry_policy=None,
                 daemon=False,
                 user_id=None):
        self._rpc = None
        self._consumer = None
        self._on_downgrade_message = None
        self._app_key = app_key
        self._app_secret = app_secret
        self._region_id = region_id
        self._tls_enable = tls_enable
        self._host = host
        self._port = port
        self._target = self._host + ":" + str(self._port)
        self._cache_timeout = cache_timeout
        self._daemon = daemon
        self._user_id = user_id

        self._msg_cache = MsgCache(maxsize=10000, ttl=timedelta(seconds=cache_timeout), timer=datetime.now)

        self._run_mutex = threading.Lock()
        self._callback_mutex = threading.RLock()

        self._retry = Retry(retry_policy, self._host)
        self._request_mutex = threading.Lock()
        self._done = False

        if self._tls_enable:
            self._channel = grpc.secure_channel(self._target, grpc.ssl_channel_credentials())
        else:
            self._channel = grpc.insecure_channel(self._target)

        self._stub = pb_grpc.QuoteStub(self._channel)

        def pong(*args, **kwargs):
            self.request(Msg(pb.Pong))

        self.task_timer = TaskTimer(function=pong, delay=10)
        self._exceptionContext = ExceptionContext()

    def _run_pong_task(self):
        self.task_timer.start()

    def _stop_pong_task(self):
        self.task_timer.cancel()

    def _initial_request(self):
        _msg = Msg(pb.Pong)
        return pb.ClientRequest(type=_msg.get_msg_type(), requestId=_msg.get_request_id(), path=_msg.get_path(),
                                payload=_msg.get_payload())

    @property
    def on_downgrade_message(self):
        return self._on_downgrade_message

    @on_downgrade_message.setter
    def on_downgrade_message(self, func):
        with self._callback_mutex:
            self._on_downgrade_message = func

    def request(self, msg):
        connection_active = False
        retries = 0
        max_retries = 3

        while not connection_active and retries < max_retries:
            try:
                if not self._consumer or not self._consumer.active() or not self._rpc:
                    logger.warning(
                        f"gRPC not started or not active. Attempting to start... (retry {retries + 1}/{max_retries})")
                    connection_active = self.run()
                else:
                    connection_active = True
            except Exception as e:
                logger.error(f"Failed to start connection (attempt {retries + 1}): {e}")
                retries += 1
                time.sleep(1)  # Increase retry interval

        if not connection_active:
            error_msg = "Failed to establish connection after multiple attempts"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

        if msg.get_msg_type() == pb.Pong and hasattr(self._rpc, "pending_requests") \
                and self._rpc.pending_requests > 2:
            logger.debug("There are requests in the queue.")
            return

        with self._request_mutex:
            if self._done:
                exception = self._exceptionContext.get_exception()
                if exception:
                    raise exception
                else:
                    raise ExitedException()

        # Ensure RPC instance exists
        if self._rpc is None:
            error_msg = "RPC instance is None even after initialization"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

        # Create client request
        client_request = pb.ClientRequest(
            type=msg.get_msg_type(),
            requestId=msg.get_request_id(),
            path=msg.get_path(),
            payload=msg.get_payload()
        )

        # User ID has already been passed through metadata during connection setup, no need to set it separately for each request

        # Send request
        send_success = False
        retries = 0
        max_retries = 3
        last_error = None

        while not send_success and retries < max_retries:
            try:
                # Send request directly, user ID has been passed through metadata during connection setup
                self._rpc.send(client_request)
                send_success = True
            except Exception as e:
                last_error = e
                # Try to reinitialize connection
                logger.info(f"Attempting to reinitialize connection (attempt {retries + 1})...")
                try:
                    self.run()
                    time.sleep(0.5)  # Give connection some time to establish
                except Exception as conn_error:
                    logger.error(f"Failed to reinitialize connection: {conn_error}")
                retries += 1

        if not send_success:
            error_msg = f"Failed to send request after {max_retries} attempts. Last error: {last_error}"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

        if msg.get_msg_type() == pb.Pong:
            return
        self._msg_cache[msg.get_request_id()] = msg

    def _handle_response(self, response) -> None:

        if self._exceptionContext.get_exception():
            self._exceptionContext.set_exception(None)

        if pb.Ping == response.type:
            logger.debug("Ping heartbeat message")
            return
        if pb.Downgrade == response.type:
            logger.warning("Your market authority has been taken by another device.Please restart later")
            if self._on_downgrade_message:
                with self._callback_mutex:
                    self._on_downgrade_message(self, response)
            return
        if pb.Payload == response.type:
            with self._callback_mutex:
                try:
                    msg = self._msg_cache.pop(response.requestId)
                    if not msg:
                        logger.warning("The request has expired, requestId:%s", response.requestId)
                        return
                    future = msg.get_future()
                    if not future:
                        msg = "The request future Lost, requestId. Host:%s SDK-Version:%s requestId:%s" % (
                            self._host, webullsdkquotescore.__version__, msg._request_id)
                        logger.error(compat.ensure_string(msg))
                        return
                    future.set_result(response)
                except Exception as e:
                    msg = "Error in response data. Host:%s SDK-Version:%s ClientException:%s" \
                          % (self._host, webullsdkquotescore.__version__, e)
                    logger.error(compat.ensure_string(msg))
                    future.set_result(e)
            return
        logger.warning("Other types of information are not processed, response_type:%s ", response.type)

    def done_callback(self, result):
        with self._request_mutex:
            self._done = True
        self._stop_pong_task()
        if isinstance(result, Exception) or isinstance(result, grpc.RpcError):
            self._exceptionContext.set_exception(result)
        items = self._msg_cache.items()
        for i in items:
            _msg = i[1]
            if pb.Pong == _msg.get_msg_type:
                return
            future = _msg.get_future()
            if not future:
                return
            future.set_result(result)

    def _should_recover(self, exc):
        should_retry = self._retry.should_recover(exc)
        self._exceptionContext.set_exception(exc)
        return should_retry

    def get_exception(self):
        return self._exceptionContext.get_exception()

    def run(self):
        with self._run_mutex:
            if not self._consumer or not self._consumer.active():
                # Close any existing old connection resources
                if self._consumer:
                    self._consumer.stop()
                if self._rpc:
                    try:
                        self._rpc.close()
                    except:
                        pass
                self._consumer = None
                self._rpc = None

                # Create new connection
                try:
                    initial_request = self._initial_request()
                    self._rpc = ResumableBidiRpc(
                        self._app_key,
                        self._app_secret,
                        self._target,
                        '/openapi.Quote/StreamRequest',
                        self._stub.StreamRequest,
                        self._should_recover,
                        initial_request=initial_request,
                        user_id=self._user_id  # Pass user ID
                    )

                    self._rpc.add_done_callback(self.done_callback)

                    self._consumer = BackgroundConsumer(self._rpc, self._handle_response)
                    self._consumer.start(self._daemon)

                    # Wait for connection to establish
                    retry = 0
                    max_retries = 5
                    while retry < max_retries:
                        if self._consumer.active() and self._rpc.is_active:
                            logger.info("Connection successfully established")
                            break
                        time.sleep(0.5)
                        retry += 1
                        logger.debug(f"Waiting for connection... {retry}/{max_retries}")

                    if not (self._consumer.active() and self._rpc.is_active):
                        logger.error("Failed to establish connection after retries")
                        raise RuntimeError("Failed to establish connection")

                    with self._request_mutex:
                        self._done = False
                    self._run_pong_task()
                    return True
                except Exception as e:
                    logger.error(f"Error establishing connection: {e}")
                    if self._consumer:
                        try:
                            self._consumer.stop()
                        except:
                            pass
                    if self._rpc:
                        try:
                            self._rpc.close()
                        except:
                            pass
                    self._consumer = None
                    self._rpc = None
                    raise RuntimeError(f"Failed to establish connection: {e}")
            return self._consumer.active() and self._rpc.is_active

    def stop(self):
        self._stop_pong_task()
        if self._consumer:
            self._consumer.stop()
            self._consumer = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._channel:
            self._channel.close()
            self._channel = None
        return False

    def __del__(self):
        if self._channel:
            self._channel.close()
            self._channel = None

    def set_user_id(self, user_id):
        if not self._user_id:
            self._user_id = user_id
