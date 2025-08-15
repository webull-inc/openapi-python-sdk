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

from webullsdkmdata.quotes.grpc.pb import quote_pb2
from webullsdkmdata.quotes.grpc.response import Response
from webullsdkmdata.request.grpc.get_batch_historical_bars_request import GetBatchHistoricalBarsRequest
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
        """
        Obtain the token required by the market subscription interface, Subscribe and UnSubscribe require the token.
        Request the token before initiating the establishment of a persistent connection.
        """
        request = GetStreamingTokenRequest()
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.TokenResponse())

    def create_subscription_rel(self, token, symbols, category, sub_types):
        """
       Real-time quotes unsubscribe interface is subscribed to real-time quotes pushes according to symbol and data type.

       :param token: Subscribe to the token returned by the pre-request,
        and the token needs to be a token that has already created a connection
       :param symbols: Such as: [AAPL,TSLA]
       :param category: Security type, enumeration
       :param sub_types: Unsubscribe data type, such as: [SNAPSHOT]、SubType Required when unsubscribe_all is empty
        or not true
       """
        request = SubscribeRequest(token, symbols, category, sub_types)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())

    def remove_subscription_rel(self, token, symbols, category, sub_types, unsubscribe_all=False):
        """
        Real-time quotes unsubscribe interface is subscribed to real-time quotes pushes according to symbol and data type.
        When unsubscribing from the interface, you get no result returned if it succeeds, and Error is returned if it fails.

        :param token: Subscribe to the token returned by the pre-request,
         and the token needs to be a token that has already created a connection
        :param symbols: Such as: [AAPL,TSLA]
        :param category: Security type, enumeration
        :param sub_types: Unsubscribe data type, such as: [SNAPSHOT]、SubType Required when unsubscribe_all is empty
         or not true

        :param unsubscribe_all: boolean false (true means canceling all real-time market subscriptions.
         When unsubscribe_all is true, symbols, category, sub_types can be empty)
        """
        request = UnsubcribeRequest(token, symbols, category, sub_types, unsubscribe_all)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())

    def get_history_bar(self, symbol, category, timespan, count='200', real_time_required=None, trading_sessions=None):
        """
        Returns to Instrument in the window aggregated data.
        According to the last N K-lines of the stock code, it supports various granularity K-lines such as m1 and m5.
        Currently, only the K-line with the previous weight is provided for the daily K-line and above,
        and only the un-weighted K-line is provided for the minute K.

        :param symbols: Securities code
        :param category: Security type, enumeration.
        :param timespan: K-line time granularity
        :param count: The number of lines: the default is 200, and the maximum limit is 1200
        :param real_time_required: Returns the latest trade quote data. By default, the most recent market data is returned.
        :param trading_sessions: Specify trading session, multiple selections are allowed
        """
        request = GetHistoricalBarsRequest(symbol, category, timespan, count, real_time_required, trading_sessions)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.BarsResponse())

    def get_batch_history_bar(self, symbols, category, timespan, count=200, real_time_required=None, trading_sessions=None):
        """
        Batch query K-line data for multiple symbols, returning aggregated data within the window.
        According to the last N K-lines of the stock code, it supports various granularity K-lines such as m1 and m5.
        Currently, only the K-line with the previous weight is provided for the daily K-line and above,
        and only the un-weighted K-line is provided for the minute K.

        :param symbols: List of security codes
        :param category: Security type, enumeration
        :param timespan: K-line interval
        :param count: Number of K-lines to return, default is 200, maximum is 1200
        :param real_time_required: Returns the latest trade quote data. By default, the most recent market data is returned.
        :param trading_sessions: Specify trading session, multiple selections are allowed
        """
        request = GetBatchHistoricalBarsRequest(symbols, category, timespan, count, real_time_required, trading_sessions)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.BatchBarsResponse())

    def get_quote(self, symbol, category):
        """
        Query the depth quote of securities according to the stock code list.

        :param symbol: security codes
        :param category: Security type, enumeration.
        """
        request = GetQuoteRequest(symbol, category)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.QuoteResponse())

    def get_snapshot(self, symbols, category):
        """
        Query the latest stock market snapshots in batches according to the stock code list.

        :param symbols: List of security codes; for example: single: 00700 multiple: 00700,00981;
        For each request,up to 100 symbols can be subscribed; Under the authority of Hong Kong stock BMP,
        a single request supports up to 20 symbols

        :param category: Security type, enumeration.
        """
        request = GetSnapshotRequest(symbols, category)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SnapshotResponse())

    def get_tick(self, symbol, category, count='30'):
        """
        Query tick-by-tick transaction of securities according to the stock code list.

        :param symbol: security codes
        :param category: Security type, enumeration.
        :param count: The number of lines: the default is 30, and the maximum limit is 1000
        """
        request = GetTickRequest(symbol, category, count)
        result = self.client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.TickResponse())
