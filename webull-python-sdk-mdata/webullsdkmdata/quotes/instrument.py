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

from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest


class Instrument:
    def __init__(self, api_client):
        self.client = api_client

    def get_instrument(self, symbols, category):
        """
         Query the underlying information according to the security symbol list and security type.

        :param symbols: Securities symbol, such as: 00700,00981.
        :param category: Security type, enumeration.
        """
        instruments_request = GetInstrumentsRequest()
        instruments_request.set_symbols(symbols)
        instruments_request.set_category(category)
        response = self.client.get_response(instruments_request)
        return response
