import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktradehk.request.palce_order_request import PlaceOrderRequest


optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)
stock_order = {
    "account_id": "ULGALPNJ7QMN0MP38UFM2PMN9A",
    "stock_order": {
        "client_order_id": "0191646207512192",
        "instrument_id": "913256409",
        "side": "BUY",
        "tif": "DAY",
        "order_type": "ENHANCED_LIMIT",
        "limit_price": "385.000",
        "qty": "100",
        "extended_hours_trading": False
    }
}


class TestOrderOperation(unittest.TestCase):
    def test_order(self):
        request = PlaceOrderRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(stock_order['account_id'])
        request.set_client_order_id(stock_order['stock_order']['client_order_id'])
        request.set_side(stock_order['stock_order']['side'])
        request.set_tif(stock_order['stock_order']['tif'])
        request.set_instrument_id(stock_order['stock_order']['instrument_id'])
        request.set_order_type(stock_order['stock_order']['order_type'])
        request.set_limit_price(stock_order['stock_order']['limit_price'])
        request.set_qty(stock_order['stock_order']['qty'])
        request.set_extended_hours_trading(stock_order['stock_order']['extended_hours_trading'])
        post_body = request.get_body_params()
        print(post_body)
        params = request.get_query_params()
        print(params)
        # request.set_trailing_type(stock_order['stock_order']['trailing_type'])
        # request.set_trailing_stop_step(stock_order['stock_order']['trailing_stop_step'])

        try:
            response = api_client.get_response(request)
            print(response.json())

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())