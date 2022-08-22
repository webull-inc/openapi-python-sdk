# coding=utf-8
import unittest
import sys
from webullsdkcore.client import ApiClient
from webullsdkcore.request import ApiRequest

OPENAPI_ENDPOINT = "<api_endpoint>"


class TestApiClient(unittest.TestCase):

    def test_api(self):
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        client.set_stream_logger(stream=sys.stderr)
        request = ApiRequest("/market-data/streaming/token", version="v1")
        request.set_endpoint(OPENAPI_ENDPOINT)
        self.assertIsNone(request.get_headers().get('Accept-Encoding'))
        client.get_response(request)
        self.assertEqual(request.get_headers()['Accept-Encoding'], 'gzip')
