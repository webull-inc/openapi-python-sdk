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
from webullsdkmdata.quotes.grpc.pb import quote_pb2
from webullsdkmdata.quotes.subscribe.quote_decoder import QuoteDecoder
from webullsdkmdata.quotes.subscribe.payload_type import (PAYLOAD_TYPE_QUOTE,
                                                          PAYLOAD_TYPE_SHAPSHOT,PAYLOAD_TYPE_TICK)
from webullsdkmdata.quotes.subscribe.snapshot_decoder import SnapshotDecoder
from webullsdkmdata.quotes.subscribe.tick_decoder import TickDecoder
from webullsdkmdata.request.grpc.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkmdata.request.grpc.quotes_subscribe_request import SubscribeRequest
from webullsdkquotescore.quotes_client import QuotesClient
from webullsdkquotescore.quotes_client import LOG_ERR
from webullsdkmdata.quotes.grpc.response import Response


class DefaultQuotesClient(QuotesClient):
    def __init__(self, app_key, app_secret, region_id, customer_type=None, host=None, tls_enable=True, transport="tcp",
                 retry_policy=None):
        if region_id:
            super().__init__(app_key, app_secret, region_id, host,
                             tls_enable=tls_enable, customer_type=customer_type,
                             transport=transport, retry_policy=retry_policy)
        else:
            super().__init__(app_key, app_secret, host=host, tls_enable=tls_enable, customer_type=customer_type,
                             transport=transport, retry_policy=retry_policy)
        self._on_subscribe_success = None

    @property
    def on_subscribe_success(self):
        return self._on_subscribe_success

    @on_subscribe_success.setter
    def on_subscribe_success(self, func):
        with self._callback_mutex:
            self._on_subscribe_success = func

    def _default_refresh_token_func(self, client, grpc_client):
        request = GetStreamingTokenRequest()
        result = grpc_client.get_response(request.get_path(), request.serialize())
        response = Response(result, quote_pb2.TokenResponse())
        return response.json()['token']

    def _default_quotes_subscribe_func(self, client, grpc_client, token):
        request = SubscribeRequest(token, self.quotes_symbols, self.quotes_category, self.quotes_subtypes)
        result = grpc_client.get_response(request.get_path(), request.serialize())
        response = Response(result, quote_pb2.SubscribeResponse())
        if response.status_code == 200:
            with self._callback_mutex:
                _on_subscribe_success = self._on_subscribe_success
                if _on_subscribe_success:
                    try:
                        _on_subscribe_success(client, grpc_client, token)
                    except Exception as e:
                        self._easy_log(
                            LOG_ERR, 'Caught exception in on_subscribe_success: %s', e)
                        raise

    def init_default_settings(self, symbols, category, sub_types):
        self.on_refresh_token = self._default_refresh_token_func
        self.on_quotes_subscribe = self._default_quotes_subscribe_func
        self.register_payload_decoder(PAYLOAD_TYPE_QUOTE, QuoteDecoder())
        self.register_payload_decoder(PAYLOAD_TYPE_SHAPSHOT, SnapshotDecoder())
        self.register_payload_decoder(PAYLOAD_TYPE_TICK, TickDecoder())
        self.quotes_symbols = symbols
        self.quotes_category = category
        self.quotes_subtypes = sub_types
