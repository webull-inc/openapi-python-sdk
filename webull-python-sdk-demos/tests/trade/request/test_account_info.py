# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest


from webullsdkcore.client import ApiClient

from webullsdktrade.trade.account_info import Account

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

