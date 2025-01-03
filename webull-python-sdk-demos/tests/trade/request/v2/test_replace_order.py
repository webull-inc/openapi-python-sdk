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
from webullsdktrade.request.v2.replace_order_request import ReplaceOrderRequest

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
#'jp'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)
modify_orders = {
    "client_order_id": "0431f6c3b3554647a485c519cb83fc18",
    "quantity": "100",
    "limit_price": "2090"
}


class TestOrderOperation(unittest.TestCase):
    def test_replace_order(self):
        request = ReplaceOrderRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        request.set_modify_orders(modify_orders)
        request.finalize_order()
        post_body = request.get_body_params()
        print(post_body)
        params = request.get_query_params()
        print(params)
        try:
            response = api_client.get_response(request)
            print(json.dumps(response.json(), indent=4))

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
