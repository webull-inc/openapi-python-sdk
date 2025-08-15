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

from webullsdkmdata.common.category import Category

from webullsdkcore.client import ApiClient
from webullsdkcore.common.region import Region
from webullsdktrade.api import API

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
# current only for 'jp','hk' region
region_id = Region.HK.value
api_client = ApiClient(
    app_key=your_app_key,
    app_secret=your_app_secret,
    region_id=region_id,
)
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
            "symbol": "AAPL",
            "instrument_type": "EQUITY",
            "market": "US",
            "order_type": "MARKET",
            "quantity": "1",
            "support_trading_session": "N",
            "side": "BUY",
            "time_in_force": "DAY",
            "entrust_type": "QTY"
        }
        res = api.order_v2.preview_order(account_id=account_id, preview_orders=preview_orders)
        if res.status_code == 200:
            print("preview_res=" + json.dumps(res.json(), indent=4))

        client_order_id = uuid.uuid4().hex
        new_orders = {
            "client_order_id": client_order_id,
            "symbol": "AAPL",
            "instrument_type": "EQUITY",
            "market": "US",
            "order_type": "LIMIT",
            "limit_price": "188",
            "quantity": "1",
            "support_trading_session": "N",
            "side": "BUY",
            "time_in_force": "DAY",
            "entrust_type": "QTY",
            # "account_tax_type": "GENERAL"
            # "total_cash_amount": "100.20"
            # "sender_sub_id": "123321-lzg",
            # "no_party_ids":[
            #     {"party_id":"BNG144.666555","party_id_source":"D","party_role":"3"}
            # ]
        }

        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_STOCK.name}
        api.order_v2.add_custom_headers(custom_headers_map)
        res = api.order_v2.place_order(account_id=account_id, new_orders=new_orders)
        api.order_v2.remove_custom_headers()
        if res.status_code == 200:
            print("place_order_res=" + json.dumps(res.json(), indent=4))
        sleep(5)
        modify_orders = {
            "client_order_id": client_order_id,
            "quantity": "100",
            "limit_price": "200"
        }
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
            print("order detail=" + json.dumps(res.json(), indent=4))

        # Options
        # For option order inquiries, please use the V2 query interface: api.order_v2.get_order_detail(account_id, client_order_id).
        client_order_id = uuid.uuid4().hex
        option_new_orders = [
            {
                "client_order_id": client_order_id,
                "combo_type": "NORMAL",
                "order_type": "LIMIT",
                "quantity": "1",
                "limit_price": "11.25",
                "option_strategy": "SINGLE",
                "side": "BUY",
                "time_in_force": "GTC",
                "entrust_type": "QTY",
                "orders": [
                    {
                        "side": "BUY",
                        "quantity": "1",
                        "symbol": "AAPL",
                        "strike_price": "250.0",
                        "init_exp_date": "2025-08-15",
                        "instrument_type": "OPTION",
                        "option_type": "CALL",
                        "market": "US"
                    }
                ]
            }
        ]
        option_modify_orders = [
            {
                "client_order_id": client_order_id,
                "quantity": "2",
                "limit_price": "11.3",
                "orders": [
                    {
                        "client_order_id": client_order_id,
                        "quantity": "2"
                    }
                ]
            }
        ]
        # preview
        res = api.order_v2.preview_option(account_id, option_new_orders)
        if res.status_code == 200:
            print("preview option=" + json.dumps(res.json(), indent=4))
        sleep(5)
        # place

        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_OPTION.name}
        api.order_v2.add_custom_headers(custom_headers_map)
        res = api.order_v2.place_option(account_id, option_new_orders)
        api.order_v2.remove_custom_headers()
        if res.status_code == 200:
            print("place option=" + json.dumps(res.json(), indent=4))
        sleep(5)
        # replace
        res = api.order_v2.replace_option(account_id, option_modify_orders)
        if res.status_code == 200:
            print("replace option=" + json.dumps(res.json(), indent=4))
        sleep(5)
        # cancel
        res = api.order_v2.cancel_option(account_id, client_order_id)
        if res.status_code == 200:
            print("cancel option=" + json.dumps(res.json(), indent=4))
        res = api.market_data.get_batch_history_bar(
            symbols=['AAPL', 'TSLA'],
            category=Category.US_STOCK.name,
            timespan='M1',
            count=1
        )
        if res.status_code == 200:
            print('us batch history bar:', res.json())
        res = api.market_data.get_batch_history_bar(
            symbols=['00700', '00981'],
            category=Category.HK_STOCK.name,
            timespan='M1',
            count=1
        )
        if res.status_code == 200:
            print('hk batch history bar:', res.json())
        res = api.market_data.get_batch_history_bar(
            symbols=['600000', '600519'],
            category=Category.CN_STOCK.name,
            timespan='M1',
            count=1
        )
        if res.status_code == 200:
            print('cn batch history bar:', res.json())
        trading_sessions = ['PRE', 'RTH', 'ATH', 'OVN']
        res = api.market_data.get_history_bar('AAPL', 'US_STOCK', 'M1', 200, 'N', trading_sessions)
        if res.status_code == 200:
            print('us stock history bar:', res.json())

        res = api.market_data.get_batch_history_bar(
            symbols=['AAPL', 'TSLA'],
            category=Category.US_STOCK.name,
            timespan='M1',
            count=1,
            real_time_required='N',
            trading_sessions=trading_sessions
        )
        if res.status_code == 200:
            print('us batch history bar:', res.json())