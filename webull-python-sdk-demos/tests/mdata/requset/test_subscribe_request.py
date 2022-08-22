# coding=utf-8
import unittest
from webullsdkmdata.request.quotes_subscribe_request import SubscribeRequest
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType
from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestSubscribeRequest(unittest.TestCase):
    def test_request(self):
        subscribe_request = SubscribeRequest()
        subscribe_request.set_token("token value")
        subscribe_request.set_category(Category.US_STOCK.name)
        subscribe_request.set_symbols(["AAPL", "TSLA"])
        subscribe_request.set_subscribe_types(
            [SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name])
        subscribe_request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>",
                           app_secret="<your_app_secret>")
        try:
            client.get_response(subscribe_request)
        except ServerException as se:
            self.assertEqual(se.get_error_code(), "INVALID_TOKEN")
