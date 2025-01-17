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
from time import sleep

from webullsdkcore.client import ApiClient
from webullsdktrade.api import API


optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
# current only for 'jp' region
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)


class TestApi(unittest.TestCase):
    def test_api(self):
        api = API(api_client)
        res = api.account_v2.get_account_list()
        if res.status_code == 200:
            print("account_list=" + json.dumps(res.json(), indent=4))

        res = api.account_v2.get_account_balance(account_id)
        if res.status_code == 200:
            print("account_balance=" + json.dumps(res.json(), indent=4))

        res = api.account_v2.get_account_position(account_id)
        if res.status_code == 200:
            print("account_position=" + json.dumps(res.json(), indent=4))

        preview_orders = {
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
        res = api.order_v2.preview_order(account_id=account_id, preview_orders=preview_orders)
        if res.status_code == 200:
            print("preview_res=" + json.dumps(res.json(), indent=4))

        client_order_id = uuid.uuid4().hex
        new_orders = {
            "client_order_id": client_order_id,
            "symbol": "7011",
            "instrument_type": "EQUITY",
            "market": "JP",
            "order_type": "LIMIT",
            "limit_price": "2080",
            "quantity": "100",
            "support_trading_session": "N",
            "side": "BUY",
            "time_in_force": "DAY",
            "entrust_type": "QTY",
            "account_tax_type": "GENERAL"
        }
        res = api.order_v2.place_order(account_id=account_id, new_orders=new_orders)
        if res.status_code == 200:
            print("place_order_res=" + json.dumps(res.json(), indent=4))
        modify_orders = {
            "client_order_id": client_order_id,
            "quantity": "100",
            "limit_price": "2090"
        }
        sleep(5)
        res = api.order_v2.replace_order(account_id=account_id, modify_orders=modify_orders)
        if res.status_code == 200:
            print("replace_order_res=" + json.dumps(res.json(), indent=4))
        sleep(5)
        res = api.order_v2.cancel_order_v2(account_id=account_id, client_order_id=client_order_id)
        if res.status_code == 200:
            print("cancel_order_res=" + json.dumps(res.json(), indent=4))
        res = api.order_v2.get_order_history_request(account_id=account_id)
        if res.status_code == 200:
            print("order_history_res=" + json.dumps(res.json(), indent=4))

        # order detail
        res = api.order_v2.get_order_detail(account_id=account_id, client_order_id=client_order_id)
        if res.status_code == 200:
            print("order_detail_res=" + json.dumps(res.json(), indent=4))