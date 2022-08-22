# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

from json.tool import main
from webullsdktradehk.common.currency import Currency
from webullsdktradehk.request.get_account_balance_request import AccountBalanceRequest
from webullsdktradehk.request.get_account_positions_request import AccountPositionsRequest
from webullsdktradehk.request.get_account_profile_request import AccountProfileRequest
from webullsdktradehk.request.get_app_subscriptions import GetAppSubscriptions

class Account:
    def __init__(self, api_client):
        self.client = api_client

    def get_account_profile(self,  account_id):
        account_profile_request = AccountProfileRequest()
        account_profile_request.set_account_id(account_id)
        response = self.client.get_response(account_profile_request)
        return response

    def get_account_balance(self, account_id, total_asset_currency=Currency.HKD.name):
        account_balance_request = AccountBalanceRequest()
        account_balance_request.set_account_id(account_id)
        account_balance_request.set_total_asset_currency(total_asset_currency)
        response = self.client.get_response(account_balance_request)
        return response

    def get_account_position(self,  account_id,page_size=10, last_instrument_id=None):
        account_positions_request = AccountPositionsRequest()
        account_positions_request.set_account_id(account_id)
        account_positions_request.set_page_size(page_size)
        if last_instrument_id is not None:
            account_positions_request.set_last_instrument_id(last_instrument_id)
        response = self.client.get_response(account_positions_request)
        return response
    
    def get_app_subscriptions(self, subscription_id=None):
        app_subscriptions = GetAppSubscriptions()
        if subscription_id is not None:
            app_subscriptions.set_subscription_id(subscription_id)
        response = self.client.get_response(app_subscriptions)
        return response
