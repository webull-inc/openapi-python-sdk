# coding=utf-8
import unittest
from webullsdkmdata.request.get_quote_request import GetQuoteRequest
from webullsdkmdata.common.category import Category
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"
class TestGetQuoteRequest(unittest.TestCase):
    def test_request(self):
        reuqest = GetQuoteRequest()
        reuqest.set_category(Category.US_STOCK.name)
        reuqest.set_symbols(["AAPL", "TSLA"])
        reuqest.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        response = client.get_response(reuqest)
        self.assertTrue(len(response.json()[0]['price']) > 0)
        self.assertTrue(len(response.json()[1]['open']) > 0)