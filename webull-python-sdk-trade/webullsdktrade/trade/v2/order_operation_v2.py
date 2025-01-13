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
from webullsdktrade.request.v2.cancel_order_request import CancelOrderRequest
from webullsdktrade.request.v2.get_order_detail_request import OrderDetailRequest
from webullsdktrade.request.v2.get_order_history_request import OrderHistoryRequest
from webullsdktrade.request.v2.palce_order_request import PlaceOrderRequest
from webullsdktrade.request.v2.preview_order_request import PreviewOrderRequest
from webullsdktrade.request.v2.replace_order_request import ReplaceOrderRequest


class OrderOperationV2:
    def __init__(self, api_client):
        self.client = api_client

    def preview_order(self, account_id, preview_orders):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        preview_order_request = PreviewOrderRequest()
        preview_order_request.set_account_id(account_id)
        preview_order_request.set_new_orders(preview_orders)
        preview_order_request.finalize_order()
        response = self.client.get_response(preview_order_request)
        return response

    def place_order(self, account_id, new_orders):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        place_order_req = PlaceOrderRequest()
        place_order_req.set_account_id(account_id)
        place_order_req.set_new_orders(new_orders)
        place_order_req.finalize_order()
        response = self.client.get_response(place_order_req)
        return response

    def replace_order(self, account_id, modify_orders):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        replace_order_request = ReplaceOrderRequest()
        replace_order_request.set_account_id(account_id)
        replace_order_request.set_modify_orders(modify_orders)
        replace_order_request.finalize_order()
        response = self.client.get_response(replace_order_request)
        return response

    def cancel_order_v2(self, account_id, client_order_id):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        cancel_order_request = CancelOrderRequest()
        cancel_order_request.set_account_id(account_id)
        cancel_order_request.set_client_order_id(client_order_id)
        response = self.client.get_response(cancel_order_request)
        return response

    def get_order_detail(self, account_id, client_order_id):
        """
        This interface is exclusively available for Webull Hong Kong brokerage clients.
         Currently, it does not support Webull Japan or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        order_detail_request = OrderDetailRequest()
        order_detail_request.set_account_id(account_id)
        order_detail_request.set_client_order_id(client_order_id)
        response = self.client.get_response(order_detail_request)
        return response

    def get_order_history_request(self, account_id, page_size=None, start_date=None, end_date=None, last_client_order_id=None):
        """
         This interface is exclusively available for Webull Japan brokerage clients.
         Currently, it does not support Webull Hong Kong or Webull U.S. clients,
         but support will be gradually introduced in the future.
        """
        order_history_request = OrderHistoryRequest()
        order_history_request.set_account_id(account_id=account_id)
        if page_size:
            order_history_request.set_page_size(page_size=page_size)
        if start_date:
            order_history_request.set_start_date(start_date=start_date)
        if end_date:
            order_history_request.set_end_date(end_date=end_date)
        if last_client_order_id:
            order_history_request.set_last_client_order_id(last_client_order_id=last_client_order_id)
        response = self.client.get_response(order_history_request)
        return response
