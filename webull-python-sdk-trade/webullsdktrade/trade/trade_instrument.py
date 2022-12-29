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
from webullsdktrade.request.get_trade_instrument_detail_request import TradeInstrumentDetailRequest


class TradeInstrument:

    def __init__(self, api_client):
        self.client = api_client

    def get_trade_instrument_detail(self, instrument_id):
        """
        Query the information of traded symbol.

        :param instrument_id: Symbol ID
        """
        instrument_detail_request = TradeInstrumentDetailRequest()
        instrument_detail_request.set_instrument_id(instrument_id)
        response = self.client.get_response(instrument_detail_request)
        return response
