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

from json.tool import main
from webullsdktrade.common.currency import Currency
from webullsdktrade.request.get_account_balance_request import AccountBalanceRequest
from webullsdktrade.request.get_account_positions_request import AccountPositionsRequest
from webullsdktrade.request.get_account_profile_request import AccountProfileRequest
from webullsdktrade.request.get_app_subscriptions import GetAppSubscriptions
from webullsdktrade.request.get_account_position_details_request import AccountPositionDetailsRequest


class Account:
    def __init__(self, api_client):
        self.client = api_client

    def get_account_profile(self, account_id):
        """
        Query account details according to account ID, which only contains static information.

        :param account_id: Account ID
        """
        account_profile_request = AccountProfileRequest()
        account_profile_request.set_account_id(account_id)
        response = self.client.get_response(account_profile_request)
        return response

    def get_account_balance(self, account_id, total_asset_currency):
        """
        Query account assets according to account id.

        :param account_id: Account ID
        :param total_asset_currency: The currency in which the total assets are denominated: the value refers to Currency
        in the dictionary value. If it is empty, it defaults to HKD
        """
        account_balance_request = AccountBalanceRequest()
        account_balance_request.set_account_id(account_id)
        account_balance_request.set_total_asset_currency(total_asset_currency)
        response = self.client.get_response(account_balance_request)
        return response

    def get_account_position(self, account_id, page_size=10, last_instrument_id=None):
        """
        Query the account position list according to the account ID page.

        :param account_id: Account ID
        :param page_size: Number of entries per page: default value is 10,
         and the maximum value is 100 with integers being filled.
        :param last_instrument_id: The last target id of the previous page,if not passed,
        the first page is checked by default
        """
        account_positions_request = AccountPositionsRequest()
        account_positions_request.set_account_id(account_id)
        account_positions_request.set_page_size(page_size)
        if last_instrument_id is not None:
            account_positions_request.set_last_instrument_id(last_instrument_id)
        response = self.client.get_response(account_positions_request)
        return response

    def get_app_subscriptions(self, subscription_id=None):
        """
        Paginate to query the account list and return account information.

        :param subscription_id: The order ID of the last piece of data, if no parameter is passed,
        the first 100 pieces of data are queried by default
        """
        app_subscriptions = GetAppSubscriptions()
        if subscription_id is not None:
            app_subscriptions.set_subscription_id(subscription_id)
        response = self.client.get_response(app_subscriptions)
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
