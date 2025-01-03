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
import uuid

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

        res = api.order.place_order(stock_order['account_id'], **stock_order['stock_order'])
        if res.status_code == 200:
            print('place order res:', res.json())
        res = api.order.replace_order(stock_order['account_id'], **stock_order['stock_order'])
        if res.status_code == 200:
            print('replace order res:', res.json())
        res = api.order.place_order_v2(stock_order['account_id'], stock_order['stock_order'])
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
