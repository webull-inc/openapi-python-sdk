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

from webullsdkmdata.request.get_historical_bars_request import GetHistoricalBarsRequest
from webullsdkmdata.request.get_quote_request import GetQuoteRequest
from webullsdkmdata.request.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkmdata.request.quotes_subscribe_request import SubscribeRequest
from webullsdkmdata.request.quotes_unsubscribe_request import UnsubcribeRequest



class MarketData:
    def __init__(self, api_client):
        self.client = api_client

    def get_token(self):
        token_request = GetStreamingTokenRequest()
        response = self.client.get_response(token_request)
        return response

    def create_subscription_rel(self, token, symbols, category, sub_types):
        subscribe_request = SubscribeRequest()
        subscribe_request.set_token(token)
        subscribe_request.set_symbols(symbols)
        subscribe_request.set_category(category)
        subscribe_request.set_subscribe_types(sub_types)
        response = self.client.get_response(subscribe_request)
        return response

    def remove_subscription_rel(self, token, symbols, category, sub_types, unsubscribe_all=False):
        unsubscribe_request = UnsubcribeRequest()
        unsubscribe_request.set_token(token)
        if unsubscribe_all:
            unsubscribe_request.set_unsubscribe_all(is_all=unsubscribe_all)
        else:
            unsubscribe_request.set_symbols(symbols)
            unsubscribe_request.set_category(category)
            unsubscribe_request.set_sub_types(sub_types)
        response = self.client.get_response(unsubscribe_request)
        return response

    def get_history_bar(self, symbol, category, timespan, count='200'):
        history_bar_request = GetHistoricalBarsRequest()
        history_bar_request.set_symbol(symbol)
        history_bar_request.set_category(category)
        history_bar_request.set_timespan(timespan)
        history_bar_request.set_count(count)
        response = self.client.get_response(history_bar_request)
        return response

    def get_quote(self, symbols, category):
        quote_request = GetQuoteRequest()
        quote_request.set_symbols(symbols)
        quote_request.set_category(category)
        response = self.client.get_response(quote_request)
        return response
