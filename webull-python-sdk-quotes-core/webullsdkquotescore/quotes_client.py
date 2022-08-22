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

import threading
import time
import uuid

import paho.mqtt.client as mqttc
import webullsdkcore.exception.error_code as error_code
from webullsdkcore.client import ApiClient
from webullsdkcore.common import api_type
from webullsdkcore.endpoint.default_endpoint_resolver import \
    DefaultEndpointResolver
from webullsdkcore.endpoint.resolver_endpoint_request import \
    ResolveEndpointRequest
from webullsdkcore.exception.exceptions import ClientException
from webullsdkcore.retry.retry_condition import RetryCondition

from webullsdkquotescore.default_retry_policy import (DefaultQuotesRetryPolicy,
                                                      QuotesRetryPolicyContext)
from webullsdkquotescore.exceptions import ConnectException, LoopException
from webullsdkquotescore.quotes_decoder import QuotesDecoder

DEFAULT_REGION_ID = "us"

LOG_INFO = mqttc.MQTT_LOG_INFO
LOG_NOTICE = mqttc.MQTT_LOG_NOTICE
LOG_WARNING = mqttc.MQTT_LOG_WARNING
LOG_ERR = mqttc.MQTT_LOG_ERR
LOG_DEBUG = mqttc.MQTT_LOG_DEBUG


class QuotesClient(mqttc.Client):
    def __init__(self, app_key, app_secret, region_id=DEFAULT_REGION_ID, tls_enable=True, transport="tcp", retry_policy=None):
        self._endpoint_resolver = DefaultEndpointResolver(self)
        self._client_id = app_key + "_" + str(uuid.uuid4())
        self._app_key = app_key
        self._app_secret = app_secret
        self._region_id = region_id
        self._out_api_message_mutex = threading.Lock()
        self._refresh_token = None
        self._quotes_token = None
        self._quotes_subscribe = None
        self._quotes_unsubscribe = None
        self._on_quotes_message = None
        self._quotes_decoder = QuotesDecoder()
        self._api_client = ApiClient(
            app_key=app_key, app_secret=app_secret, region_id=region_id)

        def _quotes_message(client, userdata, message):
            decoded = client._quotes_decoder.decode(message)
            if decoded:
                client._easy_log(
                    LOG_INFO, 'decoded message topic: %s, payload: %s', decoded[0], decoded[1])
                _on_quotes_message = client._on_quotes_message
                if _on_quotes_message:
                    _on_quotes_message(client, decoded[0], decoded[1])
            else:
                client._easy_log(
                    LOG_ERR, 'unexpected decoding for message topic: %s', message.topic)

        def _quotes_on_connect(client, userdata, flags, rc):
            if rc == 0:
                if not client._quotes_token:
                    raise RuntimeError(
                        "token must be refreshed in method on_refresh_token")
                with self._callback_mutex:
                    _quotes_subscribe = self._quotes_subscribe
                if _quotes_subscribe:
                    with self._out_api_message_mutex:
                        try:
                            _quotes_subscribe(
                                client, self._api_client, self._quotes_token)
                        except Exception as e:
                            self._easy_log(
                                LOG_ERR, 'Caught exception in on_quotes_subscribe: %s', e)
                            raise
                else:
                    raise ClientException(
                        error_code.SDK_INVALID_PARAMETER, "on_quotes_subscribe func must be set")
            else:
                raise ConnectException(rc)

        self._quotes_message = _quotes_message
        self._quotes_on_connect = _quotes_on_connect
        mqttc.Client.__init__(self, self._client_id,
                              transport, reconnect_on_failure=False)
        if tls_enable:
            self.tls_set()
        if retry_policy:
            self._retry_policy = retry_policy
        else:
            self._retry_policy = DefaultQuotesRetryPolicy()

    @property
    def on_refresh_token(self):
        return self._refresh_token

    @on_refresh_token.setter
    def on_refresh_token(self, func):
        with self._callback_mutex:
            self._refresh_token = func

    @property
    def on_quotes_subscribe(self):
        return self._quotes_subscribe

    @on_quotes_subscribe.setter
    def on_quotes_subscribe(self, func):
        with self._callback_mutex:
            self._quotes_subscribe = func

    @property
    def on_quotes_unsubscribe(self):
        return self._quotes_unsubscribe

    @on_quotes_unsubscribe.setter
    def on_quotes_unsubscribe(self, func):
        with self._callback_mutex:
            self._quotes_unsubscribe = func

    @property
    def on_quotes_message(self):
        return self._on_quotes_message

    @on_quotes_message.setter
    def on_quotes_message(self, func):
        with self._callback_mutex:
            self._on_quotes_message = func

    def register_payload_decoder(self, type, decoder):
        with self._callback_mutex:
            self._quotes_decoder.register_payload_decoder(type, decoder)

    def _quotes_connect(self, host, port):
        self.on_message = self._quotes_message
        self.on_connect = self._quotes_on_connect
        if not host:
            endpoint_request = ResolveEndpointRequest(
                self._region_id, api_type=api_type.QUOTES)
            endpoint = self._endpoint_resolver.resolve(endpoint_request)
            _host = endpoint
        else:
            _host = host
        with self._callback_mutex:
            refresh_token = self._refresh_token
        if not refresh_token:
            raise ClientException(
                error_code.SDK_INVALID_PARAMETER, "on_refresh_token func must be set")
        with self._out_api_message_mutex:
            try:
                token = refresh_token(self, self._api_client)
                self._quotes_token = token
                self.username_pw_set(self._app_key, token)
            except Exception as e:
                self._easy_log(LOG_ERR,
                               'Caught exception in on_refresh_token: %s', e)
                raise
            if not token:
                raise ClientException(
                    error_code.SDK_INVALID_REQUEST, "token refreshed failed")
        try:
            return super().connect(_host, port)
        except Exception as e:
            self._easy_log(
                LOG_ERR, 'Caught exception in connect: %s, host: %s, port: %s, ssl: %s', e, _host, port, self._ssl)
            raise e

    def connect_and_loop_forever(self, host=None, port=8883, timeout=1):
        retry_policy_context = QuotesRetryPolicyContext(None, 0, None)
        retries = 0
        final_exception = None
        while True:
            if self._thread_terminate is True:
                self._easy_log(LOG_WARNING,
                               'exited due to thread terminated')
                self._sock_close()
                return
            try:
                self._quotes_connect(host, port)
                loop_ret = super().loop_forever(timeout)
                # loop_ret != 0 means unexpected error returned from server, should be retry in future
                if loop_ret != 0:
                    raise LoopException(loop_ret)
                else:
                    self._easy_log(LOG_WARNING, 'exited normally')
                    return
            except ConnectException as connect_exception:
                final_exception = connect_exception
                retry_policy_context = QuotesRetryPolicyContext(
                    None, retries, connect_exception.error_code)
                self._easy_log(LOG_ERR,
                               'connect exception:%s', connect_exception)
            except Exception as exception:
                final_exception = exception
                retry_policy_context = QuotesRetryPolicyContext(
                    exception, retries, None)
                self._easy_log(LOG_ERR, 'exception:%s', exception)
            retryable = self._retry_policy.should_retry(retry_policy_context)
            if retryable & RetryCondition.NO_RETRY:
                self._easy_log(
                    LOG_ERR, 'processing will stopped due to not be retryable, retry_context:%s', retry_policy_context)
                break
            retry_policy_context.retryable = retryable
            time_to_sleep = self._retry_policy.compute_delay_before_next_retry(
                retry_policy_context)
            self._easy_log(LOG_INFO, "next retry will be started in %s ms, retry_context:%s",
                           time_to_sleep, retry_policy_context)
            time.sleep(time_to_sleep / 1000.0)
            retries += 1
            retry_policy_context.retries_attempted = retries
        self._sock_close()
        if final_exception:
            raise final_exception

    def connect_and_loop_async(self, host=None, port=8883, timeout=1, thread_daemon=False):
        if self._thread is not None:
            return mqttc.MQTT_ERR_INVAL
        self._sockpairR, self._sockpairW = mqttc._socketpair_compat()
        self._thread_terminate = False
        self._thread = threading.Thread(
            target=self.connect_and_loop_forever, name="Thread-Async-Quotes-Client", args=(host, port, timeout))
        self._thread.daemon = True
        self._thread.daemon = thread_daemon
        self._thread.start()

    def connect_and_loop_start(self, host=None, port=8883, timeout=1):
        self.connect_and_loop_async(host, port, timeout, True)

    def loop_wait(self):
        if self._thread is None:
            return mqttc.MQTT_ERR_INVAL
        if threading.current_thread() != self._thread:
            self._thread.join()

    def loop_stop(self):
        return super().loop_stop()
