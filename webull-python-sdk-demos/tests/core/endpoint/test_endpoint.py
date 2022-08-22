import unittest
from webullsdkcore.client import ApiClient
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest


class TestEndpoint(unittest.TestCase):

    def test_endpoint(self):
        """
            Set through ApiClient and take effect globally. The sample code is as follows.
        """
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk")

        client.add_endpoint("hk", "<api_endpoint>")
        request = GetInstrumentsRequest()
        request.set_category("HK_STOCK")
        request.set_symbols("00700")
        client.get_response(request)

    def test_endpoint_by_request(self):
        """
            Set by Request, and it only takes effect for the current Request. The sample code is as follows.
        """
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        request = GetInstrumentsRequest()
        request.set_category("HK_STOCK")
        request.set_symbols("00700")
        request.set_endpoint("<api_endpoint>")
        client.get_response(request)
