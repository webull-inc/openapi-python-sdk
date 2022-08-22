# coding=utf-8
import unittest
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest
from webullsdkmdata.common.category import Category
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestGetInstrumentsRequest(unittest.TestCase):

    def test_request(self):
        get_instruments_request = GetInstrumentsRequest()
        get_instruments_request.set_category(Category.US_STOCK.name)
        get_instruments_request.set_symbols(["AAPL", "TSLA"])
        get_instruments_request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        response = client.get_response(get_instruments_request)
        self.assertTrue(response.json()[0]['instrument_id'] == '913256135')
        self.assertTrue(response.json()[1]['instrument_id'] == '913255598')
