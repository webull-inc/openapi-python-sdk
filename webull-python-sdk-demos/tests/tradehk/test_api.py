import unittest
import uuid

from webullsdkcore.client import ApiClient
from webullsdkmdata.common.category import Category
from webullsdktradehk.api import API


optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret,'hk')
api_client.add_endpoint('us', optional_api_endpoint)


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
        res = api.instrument.get_trade_instrument_detail("913256135")
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_trade_instrument_detail("913256409")
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_trade_instrument_detail("913244615")
        if res.status_code == 200:
            print(res.json())
        res = api.market_data.get_quote('AAPL','US_STOCK')
        if res.status_code == 200:
            print('us stock quote:', res.json())
        res = api.market_data.get_quote('00700', 'HK_STOCK')
        if res.status_code == 200:
            print('hk stock quote:', res.json())
        res = api.market_data.get_quote('600000', 'CN_STOCK')
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
        res = api.account.get_app_subscriptions()
        if res.status_code == 200:
            print('app subscriptions:', res.json())
        res = api.account.get_account_profile(account_id)
        if res.status_code == 200:
            print('account profile:', res.json())
        res = api.account.get_account_position(account_id)
        if res.status_code == 200:
            print('account position:', res.json())
        res = api.account.get_account_balance(account_id,'HKD')
        if res.status_code == 200:
            print('account balance:', res.json())
        client_order_id = uuid.uuid4().hex
        print('client order id:',client_order_id)
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
        res = api.order.place_order(stock_order['account_id'], **stock_order['stock_order'])
        if res.status_code == 200:
            print('place order res:', res.json())
        res = api.order.list_open_orders(account_id, page_size=20)
        if res.status_code == 200:
            print('open orders:', res.json())
        res = api.order.list_today_orders(account_id,page_size=20)
        if res.status_code == 200:
            print('today orders', res.json())
        res = api.order.query_order_detail(account_id, client_order_id)
        if res.status_code == 200:
            print('order detail:',res.json())
        res = api.order.cancel_order(account_id, client_order_id)
        if res.status_code == 200:
            print('cancel order status:', res.json())



