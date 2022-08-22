from ast import Subscript
import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktradehk.request.get_app_subscriptions import GetAppSubscriptions


optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
api_client = ApiClient(your_app_key, your_app_secret)
subscription_id = '1646795638648'


class TestGetSubscriptions(unittest.TestCase):
    def test_get_app_subscriptions(self):
        request = GetAppSubscriptions()
        request.set_endpoint(optional_api_endpoint)
        request.set_subscription_id(subscription_id)
        try:
            response = api_client.get_response(request)
            print(response.json())
        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())