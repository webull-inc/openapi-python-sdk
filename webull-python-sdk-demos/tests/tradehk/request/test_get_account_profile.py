import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException

from webullsdktradehk.request.get_account_profile_request import AccountProfileRequest

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)


class TestAccountProfileRequest(unittest.TestCase):
    def test_get_account_profile(self):
        request = AccountProfileRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        try:
            response = api_client.get_response(request)
            print(response.json())
        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())