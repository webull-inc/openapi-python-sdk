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
import uuid

from webullsdkcore.client import ApiClient
from webullsdkcore.context.request_context_holder import RequestContextHolder
from webullsdkcore.exception.exceptions import ServerException
from webullsdkmdata.common.category import Category
from webullsdktrade.request.v2.palce_order_request import PlaceOrderRequest

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
#'jp'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)
client_order_id = uuid.uuid4().hex
new_orders = {
    "client_order_id": client_order_id,
    "symbol": "AAPL",
    "instrument_type": "EQUITY",
    "market": "US",
    "order_type": "LIMIT",
    "limit_price": "196",
    "quantity": "1",
    "support_trading_session": "N",
    "side": "BUY",
    "time_in_force": "DAY",
    "entrust_type": "QTY"
}


class TestOrderOperation(unittest.TestCase):
    def test_place_order(self):
        request = PlaceOrderRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        request.set_new_orders(new_orders)
        request.finalize_order()
        post_body = request.get_body_params()
        print(json.dumps(post_body, indent=4))
        params = request.get_query_params()
        print(params)

        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_STOCK.name}
        request.add_custom_headers(custom_headers_map)

        try:
            response = api_client.get_response(request)
            print(response.json())

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
