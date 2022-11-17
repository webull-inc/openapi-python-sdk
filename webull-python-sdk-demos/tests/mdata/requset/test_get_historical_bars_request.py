import unittest
from webullsdkmdata.request.get_historical_bars_request import GetHistoricalBarsRequest
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.timespan import Timespan
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestGetHistoricalBarsRequest(unittest.TestCase):

    def test_request(self):

        request = GetHistoricalBarsRequest()
        request.set_category(Category.US_STOCK.name)
        request.set_symbol("AAPL")
        request.set_timespan(Timespan.D.name)
        request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        response = client.get_response(request)
        self.assertTrue(len(response.json()) == 200)
