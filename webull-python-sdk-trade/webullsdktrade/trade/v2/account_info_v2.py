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

from webullsdktrade.request.v2.get_account_balance_request import AccountBalanceRequest
from webullsdktrade.request.v2.get_account_list import GetAccountList
from webullsdktrade.request.v2.get_account_positions_request import AccountPositionsRequest


class AccountV2:
    def __init__(self, api_client):
        self.client = api_client

    def get_account_list(self):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        account_list = GetAccountList()
        response = self.client.get_response(account_list)
        return response

    def get_account_balance(self, account_id):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        account_balance_request = AccountBalanceRequest()
        account_balance_request.set_account_id(account_id)
        response = self.client.get_response(account_balance_request)
        return response

    def get_account_position(self, account_id):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        account_positions_request = AccountPositionsRequest()
        account_positions_request.set_account_id(account_id)
        response = self.client.get_response(account_positions_request)
        return response
