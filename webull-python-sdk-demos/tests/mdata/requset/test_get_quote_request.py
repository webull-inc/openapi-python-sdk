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
import unittest
from webullsdkmdata.request.get_snapshot_request import GetSnapshotRequest
from webullsdkmdata.common.category import Category
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestGetQuoteRequest(unittest.TestCase):
    def test_request(self):
        reuqest = GetSnapshotRequest()
        reuqest.set_category(Category.US_STOCK.name)
        reuqest.set_symbols(["AAPL", "TSLA"])
        reuqest.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        response = client.get_response(reuqest)
        self.assertTrue(len(response.json()[0]['price']) > 0)
        self.assertTrue(len(response.json()[1]['open']) > 0)
