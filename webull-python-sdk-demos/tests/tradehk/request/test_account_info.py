import unittest


from webullsdkcore.client import ApiClient

from webullsdktradehk.trade.account_info import Account

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)
api_client.add_endpoint('us', optional_api_endpoint)


class TestAccountInfo(unittest.TestCase):
    def test_account_info(self):
        account = Account(api_client)
        res = account.get_account_profile(account_id)
        if res.status_code == 200:
            print('account profile:', res.json())
        res = account.get_account_position(account_id)
        if res.status_code == 200:
            print('account profile:', res.json())

        res = account.get_account_balance(account_id)
        if res.status_code == 200:
            print('account balance:', res.json())

        res = account.get_app_subscriptions()
        if res.status_code == 200:
            print('app subscriptions:', res.json())

