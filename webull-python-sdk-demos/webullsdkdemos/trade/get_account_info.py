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

# coding=utf-8
from webullsdktrade.trade.account_info import Account
from webullsdkcore.client import ApiClient

if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'hk' or 'us'
    region_id = "<region_id>"
    # not necessary in production env
    optional_api_endpoint = "<api_endpoint>"
    api_client = ApiClient(your_app_key, your_app_secret, region_id)
    account_id = "account_id_foo"
    account_info = Account(
        account_id, api_client, endpoint=optional_api_endpoint)
    response = account_info.get_account_profile()
    profile_data = response.json()
    print(profile_data['account_number'])
    print(profile_data['account_type'])
    response = account_info.get_account_balance()
    balance_data = response.json()
    print(balance_data['total_asset'])
    print(balance_data['total_market_value'])
    print(balance_data['total_cash'])
    print(balance_data['total_profit_loss'])
    print(balance_data['history_profit_loss'])
    print(balance_data['margin_utilization_rate'])
    for currency_asset in balance_data['account_currency_assets']:
        print(currency_asset['net_asset'])
        print(currency_asset['market_value'])
        print(currency_asset['cash_balance'])
        print(currency_asset['margin_power'])
        print(currency_asset['cash_power'])
        print(currency_asset['cash_in_transit'])
        print(currency_asset['cash_frozen'])
        print(currency_asset['cash_withdraw'])
