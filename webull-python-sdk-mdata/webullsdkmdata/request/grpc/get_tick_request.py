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


class GetTickRequest(GRPCBaseRequest):

    def __init__(self, symbol, category, count='30'):
        request = quote_pb2.TickRequest(
            symbol=symbol,
            category=category,
            count=count
        )
        GRPCBaseRequest.__init__(self, "/market-data/tick", request, version='v1')
