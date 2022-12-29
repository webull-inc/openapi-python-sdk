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
from webullsdkmdata.request.get_historical_bars_request import GetHistoricalBarsRequest
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.timespan import Timespan
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestGetHistoricalBarsRequest(unittest.TestCase):

    def test_request(self):

        request = GetHistoricalBarsRequest()
        request.set_category(Category.US_STOCK.name)
        request.set_symbol("AAPL")
        request.set_timespan(Timespan.D.name)
        request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        response = client.get_response(request)
        self.assertTrue(len(response.json()) == 200)
