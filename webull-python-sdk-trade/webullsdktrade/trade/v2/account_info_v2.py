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
from webullsdktrade.request.v2.get_account_position_details_request import AccountPositionDetailsRequest


class AccountV2:
    def __init__(self, api_client):
        self.client = api_client

    def get_account_list(self):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        account_list = GetAccountList()
        response = self.client.get_response(account_list)
        return response

    def get_account_balance(self, account_id):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        account_balance_request = AccountBalanceRequest()
        account_balance_request.set_account_id(account_id)
        response = self.client.get_response(account_balance_request)
        return response

    def get_account_position(self, account_id):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        account_positions_request = AccountPositionsRequest()
        account_positions_request.set_account_id(account_id)
        response = self.client.get_response(account_positions_request)
        return response

    def get_account_position_details(self, account_id, size, ticker_id, last_instrument_id):
        """
        Query the account position list according to the account ID page.

        :param account_id: Account ID
        :param ticker_id: Ticker ID
        :param size: Number of entries per page: default value is 20,
        :param last_instrument_id: The last position id of the previous page,if not passed,
        the first page is checked by default
        """
        account_position_details_request = AccountPositionDetailsRequest()
        account_position_details_request.set_account_id(account_id)
        account_position_details_request.set_ticker_id(ticker_id)
        if size is not None:
            account_position_details_request.set_size(size)
        if last_instrument_id is not None:
            account_position_details_request.set_last_instrument_id(last_instrument_id)
        response = self.client.get_response(account_position_details_request)
        return response