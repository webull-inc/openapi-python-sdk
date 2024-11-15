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
from webullsdktrade.trade.v2.account_info_v2 import AccountV2

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
#'jp'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)


class TestAccountInfo(unittest.TestCase):
    def test_account_info(self):
        account = AccountV2(api_client)
        res = account.get_account_list()
        if res.status_code == 200:
            print('account list:', res.json())

        res = account.get_account_balance(account_id)
        if res.status_code == 200:
            print('account balance:', res.json())

        res = account.get_account_position(account_id)
        if res.status_code == 200:
            print('account position:', res.json())
