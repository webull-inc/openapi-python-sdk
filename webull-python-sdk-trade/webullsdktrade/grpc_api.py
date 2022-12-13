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

from webullsdkmdata.quotes.grpc.instrument import Instrument
from webullsdkmdata.quotes.grpc.market_data import MarketData


class API:
    def __init__(self, grpc_api_client):
        self.instrument = Instrument(grpc_api_client)
        self.market_data = MarketData(grpc_api_client)
