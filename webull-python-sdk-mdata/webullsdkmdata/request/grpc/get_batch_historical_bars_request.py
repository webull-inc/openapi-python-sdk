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
from webullsdkmdata.request.grpc.base_request import GRPCBaseRequest


class GetBatchHistoricalBarsRequest(GRPCBaseRequest):

    def __init__(self, symbols, category, timespan, count='200', real_time_required=None, trading_sessions=None):
        """
        Initialize a batch historical bars request.

        :param symbols: List of security codes (e.g., ['AAPL', 'GOOGL', 'MSFT'])
        :param category: Security type, enumeration.
        :param timespan: K-line time granularity
        :param count: The number of lines: the default is 200, and the maximum limit is 1200
        :param real_time_required: Returns the latest trade quote data. By default, the most recent market data is returned.
        :param trading_sessions: Specify trading session, multiple selections are allowed
        """
        request = quote_pb2.BatchBarsRequest()
        request.symbols.extend(symbols)
        request.category = category
        request.timespan = timespan
        request.count = count

        if real_time_required:
            request.real_time_required = real_time_required
        if trading_sessions:
            request.trading_sessions.extend(trading_sessions)

        GRPCBaseRequest.__init__(self, "/market-data/batch-bars", request, version='v1')
