# coding=utf-8
import unittest
from webullsdkmdata.request.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkcore.client import ApiClient

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestGetStreamingTokenRequest(unittest.TestCase):
    def test_request(self):
        token_request = GetStreamingTokenRequest()
        token_request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client = ApiClient(app_key="<your_app_key>",
                           app_secret="<your_app_secret>")
        response = client.get_response(token_request)
        print(response.json())
        self.assertTrue(len(response.json()['token']) > 0)
