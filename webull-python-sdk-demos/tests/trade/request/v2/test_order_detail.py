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
import json
import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktrade.request.v2.get_order_detail_request import OrderDetailRequest


optional_api_endpoint = "<api_endpoint>"
optional_api_region_id = "<api_region_id>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)
api_client.add_endpoint(optional_api_region_id, optional_api_endpoint)

# Replace with the client_order_id to be queried.
client_order_id = "<your_client_order_id>"

class TestOrderOperation(unittest.TestCase):
    def test_order_open(self):
        request = OrderDetailRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        request.set_client_order_id(client_order_id)
        params = request.get_query_params()
        print(params)
        try:
            response = api_client.get_response(request)
            print(json.dumps(response.json(), indent=4))

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
