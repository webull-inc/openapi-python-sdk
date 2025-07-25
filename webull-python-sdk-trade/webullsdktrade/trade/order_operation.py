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
from webullsdktrade.request.cancel_order_request import CancelOrderRequest
from webullsdktrade.request.get_open_orders_request import OpenOrdersListRequest
from webullsdktrade.request.get_order_detail_request import OrderDetailRequest
from webullsdktrade.request.get_today_orders_request import TodayOrdersListRequest
from webullsdktrade.request.palce_order_request import PlaceOrderRequest
from webullsdktrade.request.place_order_request_v2 import PlaceOrderRequestV2
from webullsdktrade.request.replace_order_request import ReplaceOrderRequest
from webullsdktrade.request.replace_order_request_v2 import ReplaceOrderRequestV2
from webullsdktrade.request.v2.cancel_option_request import CancelOptionRequest
from webullsdktrade.request.v2.place_option_request import PlaceOptionRequest
from webullsdktrade.request.v2.preview_option_request import PreviewOptionRequest
from webullsdktrade.request.v2.replace_option_request import ReplaceOptionRequest


class OrderOperation:
    def __init__(self, api_client):
        self.client = api_client

    def place_order(self, account_id, qty, instrument_id, side, client_order_id, order_type,
                    extended_hours_trading, tif, limit_price=None, stop_price=None,
                    trailing_type=None, trailing_stop_step=None, category=None):
        """
        This interface is used by customers in Hong Kong to place orders, and supports placing orders in two markets:
        Hong Kong stocks, and A shares (China Connect).

        :param account_id: Account ID
        :param qty: The amount of the equities to place an order, integer, the maximum value supported is 1000000 shares
        :param instrument_id: Instrument ID.
        :param side: Buy and sell direction.
        :param client_order_id: Third-party order ID, and the maximum length of this field is 40.
        :param order_type: Order Type.
        :param extended_hours_trading: Whether to allow pre-market and post-market trading.
        Market orders can only be false, and limit orders can be true or false..
        :param tif: Order validity period.
        :param limit_price: Order_type is LIMIT, STOP_LOSS_LIMIT, ENHANCED_LIMIT,
         AT_AUCTION_LIMIT (at-auction limit order) and needs to be passed.
        :param stop_price: When order_type is STOP_LOSS (stop-loss order), STOP_LOSS_LIMIT (stop-loss limit price),
        it needs to pass.
        :param trailing_type: Spread type of trailing stop order, trailing stop order to be transmitted.
        :param trailing_stop_step: Spread value of trailing stop order, trailing stop order to be transmitted
        """
        place_order_request = PlaceOrderRequest()
        place_order_request.set_account_id(account_id)
        place_order_request.set_stock_order(client_order_id=client_order_id, instrument_id=instrument_id, qty=qty,
                                            side=side, tif=tif, extended_hours_trading=extended_hours_trading,
                                            order_type=order_type, limit_price=limit_price, stop_price=stop_price,
                                            trailing_type=trailing_type, trailing_stop_step=trailing_stop_step)
        place_order_request.set_custom_header(category)
        response = self.client.get_response(place_order_request)
        return response

    def replace_order(self, account_id, qty, instrument_id, side, client_order_id, order_type,
                      extended_hours_trading, tif, limit_price=None, stop_price=None,
                      trailing_type=None, trailing_stop_step=None):
        """
        Modify order.

        :param account_id: Account ID
        :param qty: The amount of the equities to place an order, integer, the maximum value supported is 1000000 shares
        :param instrument_id: Instrument ID.
        :param side: Buy and sell direction.
        :param client_order_id: Third-party order ID, and the maximum length of this field is 40.
        :param order_type: Order Type.
        :param extended_hours_trading: Whether to allow pre-market and post-market trading.
         Market orders can only be false, and limit orders can be true or false..
        :param tif: Order validity period.
        :param limit_price: Order_type is LIMIT, STOP_LOSS_LIMIT, ENHANCED_LIMIT,
        AT_AUCTION_LIMIT (at-auction limit order) and needs to be passed.
        :param stop_price: When order_type is STOP_LOSS (stop-loss order),
        STOP_LOSS_LIMIT (stop-loss limit price), it needs to pass.
        :param trailing_type: Spread type of trailing stop order, trailing stop order to be transmitted.
        :param trailing_stop_step: Spread value of trailing stop order, trailing stop order to be transmitted
        """
        replace_order_request = ReplaceOrderRequest()
        replace_order_request.set_account_id(account_id)
        replace_order_request.set_stock_order(client_order_id=client_order_id, instrument_id=instrument_id, qty=qty,
                                              side=side, tif=tif, extended_hours_trading=extended_hours_trading,
                                              order_type=order_type, limit_price=limit_price, stop_price=stop_price,
                                              trailing_type=trailing_type, trailing_stop_step=trailing_stop_step)
        response = self.client.get_response(replace_order_request)
        return response

    def place_order_v2(self, account_id, stock_order):
        place_order_request = PlaceOrderRequestV2()
        place_order_request.set_account_id(account_id)
        place_order_request.set_stock_order(stock_order)
        place_order_request.set_custom_header(stock_order)
        response = self.client.get_response(place_order_request)
        return response

    def replace_order_v2(self, account_id, stock_order):
        replace_order_request = ReplaceOrderRequestV2()
        replace_order_request.set_account_id(account_id)
        replace_order_request.set_stock_order(stock_order)
        response = self.client.get_response(replace_order_request)
        return response

    def cancel_order(self, account_id, client_order_id):
        """
        Cancel order.

        :param account_id: Account ID
        :param client_order_id: Third-party order ID, and the maximum length of this field is 40.
        """
        cancel_order_request = CancelOrderRequest()
        cancel_order_request.set_account_id(account_id)
        cancel_order_request.set_client_order_id(client_order_id)
        response = self.client.get_response(cancel_order_request)
        return response

    def list_today_orders(self, account_id, page_size=10, last_client_order_id=None):
        """
        Paging query all orders of the day, the number of data returned each time can be specified,
        the maximum value is 100.

        :param account_id: Account ID
        :param page_size: For the number of entries per page, the default value is 10,
        and the maximum value is 100. Integers can be filled.

        :param last_client_order_id: The 3rd party order ID is not passed,
         and the default check is conducted on the first page.
        """
        today_orders_list_request = TodayOrdersListRequest()
        today_orders_list_request.set_account_id(account_id)
        today_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            today_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(today_orders_list_request)
        return response

    def list_open_orders(self, account_id, page_size=10, last_client_order_id=None):
        """
        Paging query pending orders.

        :param account_id: Account ID
        :param page_size: For the number of entries per page, the default value is 10, and the maximum value is 100.
         Integers can be filled.
        :param last_client_order_id: The 3rd party order ID is not passed,
        and the default check is conducted on the first page.
        """
        open_orders_list_request = OpenOrdersListRequest()
        open_orders_list_request.set_account_id(account_id)
        open_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            open_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(open_orders_list_request)
        return response

    def query_order_detail(self, account_id, client_order_id):
        """
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
        This interface is exclusively available for Webull Hong Kong brokerage clients.
        Currently, it does not support Webull Japan or Webull U.S. clients,
        but support will be gradually introduced in the future.
        """
        preview_option_request = PreviewOptionRequest()
        preview_option_request.set_new_orders(new_orders)
        preview_option_request.set_account_id(account_id)
        response = self.client.get_response(preview_option_request)
        return response

    def place_option(self, account_id, new_orders):
        """
        This interface is exclusively available for Webull Hong Kong brokerage clients.
        Currently, it does not support Webull Japan or Webull U.S. clients,
        but support will be gradually introduced in the future.
        """
        place_option_request = PlaceOptionRequest()
        place_option_request.set_new_orders(new_orders)
        place_option_request.set_account_id(account_id)
        place_option_request.set_custom_header(new_orders)
        response = self.client.get_response(place_option_request)
        return response

    def replace_option(self, account_id, modify_orders):
        """
        This interface is exclusively available for Webull Hong Kong brokerage clients.
        Currently, it does not support Webull Japan or Webull U.S. clients,
        but support will be gradually introduced in the future.
        """
        replace_option_request = ReplaceOptionRequest()
        replace_option_request.set_modify_orders(modify_orders)
        replace_option_request.set_account_id(account_id)
        response = self.client.get_response(replace_option_request)
        return response

    def cancel_option(self, account_id, client_order_id):
        """
        This interface is exclusively available for Webull Hong Kong brokerage clients.
        Currently, it does not support Webull Japan or Webull U.S. clients,
        but support will be gradually introduced in the future.
        """
        cancel_option_request = CancelOptionRequest()
        cancel_option_request.set_client_order_id(client_order_id)
        cancel_option_request.set_account_id(account_id)
        response = self.client.get_response(cancel_option_request)
        return response