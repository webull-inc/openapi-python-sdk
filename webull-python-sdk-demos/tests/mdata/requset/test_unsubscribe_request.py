# coding=utf-8

from webullsdkcore.exception.exceptions import ServerException
from webullsdkcore.client import ApiClient
from webullsdkmdata.request.quotes_unsubscribe_request import UnsubcribeRequest
from webullsdkmdata.request.get_streaming_token_request import GetStreamingTokenRequest
import unittest

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestUnsubscribeRequest(unittest.TestCase):
    def test_request(self):
        client = ApiClient(app_key="<your_app_key>",
                           app_secret="<your_app_secret>")
        client.add_endpoint('us', PRE_OPENAPI_ENDPOINT)
        token_request = GetStreamingTokenRequest()
        token = client.get_response(token_request).json()['token']
        unsubscribe_request = UnsubcribeRequest()
        unsubscribe_request.set_token(token)
        unsubscribe_request.set_unsubscribe_all(True)
        try:
            client.get_response(unsubscribe_request)
        except ServerException as se:
            self.assertEqual(se.get_error_code(), "INVALID_TOKEN")
