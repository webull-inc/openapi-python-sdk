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
from webullsdkmdata.common.category import Category
from webullsdktrade.api import API
from webullsdktrade.common.markets import Markets
from webullsdktrade.common.instrument_type import InstrumentType

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
# 'hk' or 'us' or 'jp'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)


class TestApi(unittest.TestCase):
    def test_api(self):
        api = API(api_client)
        res = api.instrument.get_instrument('AAPL', 'US_STOCK')
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_instrument('00700', 'HK_STOCK')
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_instrument('600000', Category.CN_STOCK.name)
        if res.status_code == 200:
            print(res.json())
        res = api.trade_instrument.get_trade_instrument_detail("913256135")
        if res.status_code == 200:
            print(res.json())
        res = api.trade_instrument.get_trade_instrument_detail("913256409")
        if res.status_code == 200:
            print(res.json())
        res = api.trade_instrument.get_trade_instrument_detail("913244615")
        if res.status_code == 200:
            print(res.json())
        res = api.trade_instrument.get_trade_security_detail("SPX", Markets.US.name, "OPTION",
                                                             InstrumentType.CALL_OPTION.name, "3400", "2024-12-20")
        if res.status_code == 200:
            print(res.json())
        res = api.market_data.get_snapshot('AAPL', 'US_STOCK')
        if res.status_code == 200:
            print('us stock quote:', res.json())
        res = api.market_data.get_snapshot('00700', 'HK_STOCK')
        if res.status_code == 200:
            print('hk stock quote:', res.json())
        res = api.market_data.get_snapshot('600000', 'CN_STOCK')
        if res.status_code == 200:
            print('cn stock quote:', res.json())
        res = api.market_data.get_history_bar('AAPL', 'US_STOCK', 'M1')
        if res.status_code == 200:
            print('us stock history bar:', res.json())
        res = api.market_data.get_history_bar('00700', 'HK_STOCK', 'M1')
        if res.status_code == 200:
            print('hk stock history bar:', res.json())
        res = api.market_data.get_history_bar('600000', 'CN_STOCK', 'M1')
        if res.status_code == 200:
            print('cn stock quote:', res.json())
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
        res = api.market_data.get_eod_bar(instrument_ids='913303964', count=10)
        if res.status_code == 200:
            print('eod bar quote:', res.json())
        res = api.market_data.get_corp_action(instrument_ids="913303964,913256135", event_types="301,302")
        if res.status_code == 200:
            print('corp action quote:', res.json())
        res = api.trade_instrument.get_tradeable_instruments()
        if res.status_code == 200:
            print('tradeable instruments:', res.json())
        res = api.account.get_app_subscriptions()
        if res.status_code == 200:
            print('app subscriptions:', res.json())
        res = api.account.get_account_profile(account_id)
        if res.status_code == 200:
            print('account profile:', res.json())
        res = api.account.get_account_position(account_id)
        if res.status_code == 200:
            print('account position:', res.json())
        res = api.account.get_account_balance(account_id, 'HKD')
        if res.status_code == 200:
            print('account balance:', res.json())
        client_order_id = uuid.uuid4().hex
        print('client order id:', client_order_id)
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "MARKET",
                # "limit_price": "385.000",
                "qty": "1",
                "extended_hours_trading": False
            }
        }
        """
        ENHANCED_LIMIT stock_order
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256409",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "ENHANCED_LIMIT",
                "limit_price": "1.000",
                "qty": "100",
                "extended_hours_trading": False
            }
        }
        """
        """
        STOP_LOSS stock_order
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "STOP_LOSS",
                "stop_price": "365.000",
                "qty": "1",
                "extended_hours_trading": False
            }
        }
        """
        """
        LIMIT stock_order
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "LIMIT",
                "limit_price": "385.000",
                "qty": "1",
                "extended_hours_trading": False
            }
        }
        """
        """
        STOP_LOSS_LIMIT stock_order
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "STOP_LOSS_LIMIT",
                "stop_price": "385.000",
                "limit_price": "385.100",
                "qty": "1",
                "extended_hours_trading": False
            }
        }
        """
        """
        TRAILING_STOP_LOSS stock_order
        stock_order = {
            "account_id": account_id,
            "stock_order": {
                "client_order_id": client_order_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "TRAILING_STOP_LOSS",
                # "stop_price": "385.000",
                # "limit_price": "385.100",
                "trailing_type": "AMOUNT",
                "trailing_stop_step": "0.01",
                "qty": "1",
                "extended_hours_trading": False
            }
        }
        """

        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_STOCK.name}
        api.order.add_custom_headers(custom_headers_map)
        res = api.order.place_order(stock_order['account_id'], **stock_order['stock_order'])
        api.order.remove_custom_headers()
        if res.status_code == 200:
            print('place order res:', res.json())
        res = api.order.replace_order(stock_order['account_id'], **stock_order['stock_order'])
        if res.status_code == 200:
            print('replace order res:', res.json())

        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_STOCK.name}
        api.order.add_custom_headers(custom_headers_map)
        res = api.order.place_order_v2(stock_order['account_id'], stock_order['stock_order'])
        api.order.remove_custom_headers()
        if res.status_code == 200:
            print('place order v2 res:', res.json())
        res = api.order.replace_order_v2(stock_order['account_id'], stock_order['stock_order'])
        if res.status_code == 200:
            print('replace order v2 res:', res.json())
        res = api.order.list_open_orders(account_id, page_size=20)
        if res.status_code == 200:
            print('open orders:', res.json())
        res = api.order.list_today_orders(account_id, page_size=20)
        if res.status_code == 200:
            print('today orders', res.json())
        res = api.order.query_order_detail(account_id, client_order_id)
        if res.status_code == 200:
            print('order detail:', res.json())
        res = api.order.cancel_order(account_id, client_order_id)
        if res.status_code == 200:
            print('cancel order status:', res.json())



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
        res = api.order.preview_option(account_id, option_new_orders)
        if res.status_code == 200:
            print("preview option=" + json.dumps(res.json(), indent=4))
        sleep(5)

        # place
        # This is an optional feature; you can still make a request without setting it.
        custom_headers_map = {"category": Category.US_OPTION.name}
        api.order.add_custom_headers(custom_headers_map)
        res = api.order.place_option(account_id, option_new_orders)
        api.order.remove_custom_headers()
        if res.status_code == 200:
            print("place option=" + json.dumps(res.json(), indent=4))
        sleep(5)

        # replace
        res = api.order.replace_option(account_id, option_modify_orders)
        if res.status_code == 200:
            print("replace option=" + json.dumps(res.json(), indent=4))
        sleep(5)

        # cancel
        res = api.order.cancel_option(account_id, client_order_id)
        if res.status_code == 200:
            print("cancel option=" + json.dumps(res.json(), indent=4))
