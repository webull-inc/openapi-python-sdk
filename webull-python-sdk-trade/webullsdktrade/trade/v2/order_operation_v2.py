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
from webullsdkcore.context.request_context_holder import RequestContextHolder
from webullsdktrade.request.v2.cancel_option_request import CancelOptionRequest
from webullsdktrade.request.v2.cancel_order_request import CancelOrderRequest
from webullsdktrade.request.v2.get_order_detail_request import OrderDetailRequest
from webullsdktrade.request.v2.get_order_history_request import OrderHistoryRequest
from webullsdktrade.request.v2.palce_order_request import PlaceOrderRequest
from webullsdktrade.request.v2.place_option_request import PlaceOptionRequest
from webullsdktrade.request.v2.preview_option_request import PreviewOptionRequest
from webullsdktrade.request.v2.preview_order_request import PreviewOrderRequest
from webullsdktrade.request.v2.replace_option_request import ReplaceOptionRequest
from webullsdktrade.request.v2.replace_order_request import ReplaceOrderRequest


class OrderOperationV2:
    def __init__(self, api_client):
        self.client = api_client

    def preview_order(self, account_id, preview_orders):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        preview_order_request = PreviewOrderRequest()
        preview_order_request.set_account_id(account_id)
        preview_order_request.set_new_orders(preview_orders)
        preview_order_request.finalize_order()
        response = self.client.get_response(preview_order_request)
        return response

    def place_order(self, account_id, new_orders):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        place_order_req = PlaceOrderRequest()
        place_order_req.set_account_id(account_id)
        place_order_req.set_new_orders(new_orders)
        place_order_req.finalize_order()
        place_order_req.add_custom_headers_from_order(new_orders)
        place_order_req.add_custom_headers_from_context()
        response = self.client.get_response(place_order_req)
        return response

    def replace_order(self, account_id, modify_orders):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
        """
        replace_order_request = ReplaceOrderRequest()
        replace_order_request.set_account_id(account_id)
        replace_order_request.set_modify_orders(modify_orders)
        replace_order_request.finalize_order()
        response = self.client.get_response(replace_order_request)
        return response

    def cancel_order_v2(self, account_id, client_order_id):
        """
        This interface is currently available only to individual brokerage customers in Webull Japan
        and institutional brokerage clients in Webull Hong Kong. It is not yet available to
        Webull US brokerage customers, but support will be introduced progressively in the future.
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
        Historical orders, query the records of the past 7 days. If they are group orders, will be returned together,
        and the number of orders returned on one page may exceed the page_size.

        :param account_id: Account ID
        :param page_size: Limit the number of records per query to 10 by default.
        :param start_date: Start date (if empty, the default is the last 7 days), in the format of yyyy-MM-dd.
        :param end_date: End date (if empty, the default is the last 7 days), in the format of yyyy-MM-dd.
        :param last_client_order_id: The last order ID from the previous response. For the first page query,
        this parameter is not required.
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
    def query_order_detail(self, account_id, client_order_id):
        """
        This interface is currently available only to individual and institutional clients
        of Webull Hong Kong brokerages. It is not yet supported for clients of Webull US
        and Webull Japan brokerages, but support will be gradually introduced in the future.
        Paging query pending orders.

        :param account_id: Account ID
        :param client_order_id: The 3rd party order ID.
        """
        order_detail_request = OrderDetailRequest()
        order_detail_request.set_account_id(account_id)
        order_detail_request.set_client_order_id(client_order_id)
        response = self.client.get_response(order_detail_request)
        return response

    def preview_option(self, account_id, new_orders):
        """
        This interface is currently available only to individual and institutional clients
        of Webull Hong Kong brokerages. It is not yet supported for clients of Webull US
        and Webull Japan brokerages, but support will be gradually introduced in the future.
        """
        preview_option_request = PreviewOptionRequest()
        preview_option_request.set_new_orders(new_orders)
        preview_option_request.set_account_id(account_id)
        response = self.client.get_response(preview_option_request)
        return response

    def place_option(self, account_id, new_orders):
        """
        This interface is currently available only to individual and institutional clients
        of Webull Hong Kong brokerages. It is not yet supported for clients of Webull US
        and Webull Japan brokerages, but support will be gradually introduced in the future.
        """
        place_option_request = PlaceOptionRequest()
        place_option_request.set_new_orders(new_orders)
        place_option_request.set_account_id(account_id)
        place_option_request.add_custom_headers_from_order(new_orders)
        place_option_request.add_custom_headers_from_context()
        response = self.client.get_response(place_option_request)
        return response

    def replace_option(self, account_id, modify_orders):
        """
        This interface is currently available only to individual and institutional clients
        of Webull Hong Kong brokerages. It is not yet supported for clients of Webull US
        and Webull Japan brokerages, but support will be gradually introduced in the future.
        """
        replace_option_request = ReplaceOptionRequest()
        replace_option_request.set_modify_orders(modify_orders)
        replace_option_request.set_account_id(account_id)
        response = self.client.get_response(replace_option_request)
        return response

    def cancel_option(self, account_id, client_order_id):
        """
        This interface is currently available only to individual and institutional clients
        of Webull Hong Kong brokerages. It is not yet supported for clients of Webull US
        and Webull Japan brokerages, but support will be gradually introduced in the future.
        """
        cancel_option_request = CancelOptionRequest()
        cancel_option_request.set_client_order_id(client_order_id)
        cancel_option_request.set_account_id(account_id)
        response = self.client.get_response(cancel_option_request)
        return response

    def add_custom_headers(self, headers_map: dict):
        """
        This is an optional feature; you can still make a request without setting it.
        If set, you can specify certain headers to perform specific operations.
        Note: If you set a header, call remove_custom_headers to clean up the header after the request is completed.

        Currently supported header keys and functions:
            Key：category {See Also: category}
            Function: Frequency limit rules, please refer to the document for details. currently only supports Hong Kong
        """
        if not headers_map or len(headers_map) == 0:
            return

        RequestContextHolder.get().update(headers_map)

    def remove_custom_headers(self):
        """
        Clearing headers after the request is completed.
        """
        RequestContextHolder.clear()