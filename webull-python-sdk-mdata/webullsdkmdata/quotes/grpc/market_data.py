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

from webullsdkmdata.quotes.grpc.pb import quote_pb2
from webullsdkmdata.quotes.grpc.response import Response
from webullsdkmdata.request.grpc.get_historical_bars_request import GetHistoricalBarsRequest
from webullsdkmdata.request.grpc.get_quote_request import GetQuoteRequest
from webullsdkmdata.request.grpc.get_snapshot_request import GetSnapshotRequest
from webullsdkmdata.request.grpc.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkmdata.request.grpc.quotes_subscribe_request import SubscribeRequest
from webullsdkmdata.request.grpc.quotes_unsubscribe_request import UnsubcribeRequest
from webullsdkmdata.request.grpc.get_tick_request import GetTickRequest


class MarketData:
    def __init__(self, grpc_client):
        self.client = grpc_client

    def get_token(self):
        request = GetStreamingTokenRequest()
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.TokenResponse())

    def create_subscription_rel(self, token, symbols, category, sub_types):
        request = SubscribeRequest(token, symbols, category, sub_types)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())

    def remove_subscription_rel(self, token, symbols, category, sub_types, unsubscribe_all=False):
        request = UnsubcribeRequest(token, symbols, category, sub_types, unsubscribe_all)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())

    def get_history_bar(self, symbol, category, timespan, count='200'):
        request = GetHistoricalBarsRequest(symbol, category, timespan, count)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.BarsResponse())

    def get_quote(self, symbol, category):
        request = GetQuoteRequest(symbol, category)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.QuoteResponse())

    def get_snapshot(self, symbols, category):
        request = GetSnapshotRequest(symbols, category)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SnapshotResponse())

    def get_tick(self, symbol, category, count='30'):
        request = GetTickRequest(symbol, category, count)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.TickResponse())
