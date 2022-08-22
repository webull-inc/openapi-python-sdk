import unittest
from webullsdkcore.client import ApiClient
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest


class TestTimeout(unittest.TestCase):

    def test_timeout(self):
        # Set the connection timeout to 3 seconds and the read timeout to 6 seconds.
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk", connect_timeout=3,
                           timeout=6)

        request = GetInstrumentsRequest()
        # Set the connection timeout of the request to 2 seconds and the read timeout to 4 seconds, only valid for the current request.
        request.set_connect_timeout(2)
        request.set_read_timeout(4)
        request.set_category("HK_STOCK")
        request.set_symbols("00700")
        client.get_response(request)
