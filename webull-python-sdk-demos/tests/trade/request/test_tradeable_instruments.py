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

import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktrade.request.get_tradeable_instruments_request import TradeableInstrumentRequest;

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
api_client = ApiClient(your_app_key, your_app_secret)


class TestTradeableInstruments(unittest.TestCase):

    def test_tradeable_instruments(self):
        request = TradeableInstrumentRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_last_instrument_id("")
        request.set_page_size(10)
        try:
            response = api_client.get_response(request)
            print(response.json())
        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
