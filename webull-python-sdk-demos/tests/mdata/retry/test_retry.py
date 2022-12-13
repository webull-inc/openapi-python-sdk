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

import logging
import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.retry.retry_policy import NO_RETRY_POLICY
from webullsdkquotescore.default_retry_policy import DefaultQuotesRetryPolicy
from webullsdkquotescore.quotes_client import QuotesClient

PRE_HOST = "<quotes_endpoint>"
PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestQuotesClient(unittest.TestCase):

    def test_default_host(self):
        client = QuotesClient("app_key_mocked", "app_secret_mocked", retry_policy=NO_RETRY_POLICY)

        def _refresh_token_func(client, api_client):
            return "token_mocked"

        client.on_refresh_token = _refresh_token_func
        client.enable_logger(logger=logging.getLogger(__name__))
        try:
            client.connect_and_loop_forever()
        except:
            pass

    def test_reconnect(self):
        retry_policy = DefaultQuotesRetryPolicy(max_retry_times=2)
        client = QuotesClient("app_key_mocked", "app_secret_mocked", retry_policy=retry_policy)

        def _refresh_token_func(client, api_client):
            self.assertTrue(isinstance(client, QuotesClient))
            self.assertTrue(isinstance(api_client, ApiClient))
            return "token_mocked"

        client.on_refresh_token = _refresh_token_func

        def _on_log(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        client.on_log = _on_log
        try:
            client.connect_and_loop_forever(PRE_HOST)
        except:
            pass

    def test_invalid_host(self):
        client = QuotesClient("app_key_mocked", "app_secret_mocked", retry_policy=NO_RETRY_POLICY)

        def _refresh_token_func(client, api_client):
            self.assertTrue(isinstance(client, QuotesClient))
            self.assertTrue(isinstance(api_client, ApiClient))
            return "token_mocked"

        client.on_refresh_token = _refresh_token_func
        try:
            client.connect_and_loop_forever("invalid_mqtt_host")
        except Exception as e:
            self.assertTrue(str(e).find(
                "nodename nor servname provided, or not known") > -1)

        def _on_log(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        def _on_socket_close_callback(client, userdata, socket):
            print("on_socket_close -> userdata:%s, socket info:%s" %
                  (userdata, socket))

        def _on_disconnect_callback(client, userdata, rc):
            print("on_disconnect -> userdata:%s, rc:%s" % (userdata, rc))
            # due to app_key, token both mocked
            self.assertEqual(rc, 7)

        client.on_log = _on_log
        client.on_disconnect = _on_disconnect_callback
        client.on_socket_close = _on_socket_close_callback
        try:
            client.connect_and_loop_forever(PRE_HOST)
        except:
            pass
