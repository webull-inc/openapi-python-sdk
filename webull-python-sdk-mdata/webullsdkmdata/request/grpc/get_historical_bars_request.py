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
from webullsdkmdata.request.grpc.base_request import GRPCBaseRequest


class GetHistoricalBarsRequest(GRPCBaseRequest):

    def __init__(self, symbol, category, timespan, count='200', real_time_required=None, trading_sessions=None):
        request = quote_pb2.BarsRequest(
            symbol=symbol,
            category=category,
            timespan=timespan,
            count=count
        )

        if real_time_required:
            request.real_time_required = real_time_required
        if trading_sessions:
            request.trading_sessions = ','.join(trading_sessions)

        GRPCBaseRequest.__init__(self, "/market-data/bars", request, version='v1')
