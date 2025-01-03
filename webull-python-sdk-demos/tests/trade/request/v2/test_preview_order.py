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
from webullsdktrade.request.v2.preview_order_request import PreviewOrderRequest

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
#'jp'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)
new_orders = {
    "symbol": "7011",
    "instrument_type": "EQUITY",
    "market": "JP",
    "order_type": "LIMIT",
    "limit_price": "2070",
    "quantity": "10",
    "support_trading_session": "N",
    "side": "BUY",
    "time_in_force": "DAY",
    "entrust_type": "QTY",
    "account_tax_type": "GENERAL"
}


class TestOrderOperation(unittest.TestCase):
    def test_preview_order(self):
        request = PreviewOrderRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        request.set_new_orders(new_orders)
        request.finalize_order()
        post_body = request.get_body_params()
        print(json.dumps(post_body, indent=4))
        params = request.get_query_params()
        print(params)

        try:
            response = api_client.get_response(request)
            print(response.json())

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
