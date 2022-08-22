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
import uuid
from webullsdktradehk.common.order_side import OrderSide
from webullsdktradehk.common.order_tif import OrderTIF
from webullsdktradehk.common.order_type import OrderType
from webullsdktradehk.request.cancel_order_request import CancelOrderRequest
from webullsdktradehk.request.get_open_orders_request import OpenOrdersListRequest
from webullsdktradehk.request.get_order_detail_request import OrderDetailRequest
from webullsdktradehk.request.get_today_orders_request import TodayOrdersListRequest
from webullsdktradehk.request.palce_order_request import PlaceOrderRequest
from webullsdktradehk.request.replace_order_request import ReplaceOrderRequest


class OrderOperation:
    def __init__(self, api_client):
        self.client = api_client

    def place_order(self, account_id, qty, instrument_id, side, client_order_id, order_type,
                    extended_hours_trading, tif, limit_price=None, stop_price=None,
                    trailing_type=None, trailing_stop_step=None):
        place_order_request = PlaceOrderRequest()
        place_order_request.set_account_id(account_id)
        place_order_request.set_stock_order(client_order_id=client_order_id, instrument_id=instrument_id, qty=qty,
                                            side=side, tif=tif, extended_hours_trading=extended_hours_trading,
                                            order_type=order_type, limit_price=limit_price, stop_price=stop_price,
                                            trailing_type=trailing_type, trailing_stop_step=trailing_stop_step)
        response = self.client.get_response(place_order_request)
        return response

    def replace_order(self, account_id, qty, instrument_id, side, client_order_id, order_type,
                      extended_hours_trading, tif, limit_price=None, stop_price=None,
                      trailing_type=None, trailing_stop_step=None):
        replace_order_request = ReplaceOrderRequest()
        replace_order_request.set_account_id(account_id)
        replace_order_request.set_stock_order(client_order_id=client_order_id, instrument_id=instrument_id, qty=qty,
                                              side=side, tif=tif, extended_hours_trading=extended_hours_trading,
                                              order_type=order_type, limit_price=limit_price, stop_price=stop_price,
                                              trailing_type=trailing_type, trailing_stop_step=trailing_stop_step)
        response = self.client.get_response(replace_order_request)
        return response

    def cancel_order(self, account_id, client_order_id):
        cancel_order_request = CancelOrderRequest()
        cancel_order_request.set_account_id(account_id)
        cancel_order_request.set_client_order_id(client_order_id)
        response = self.client.get_response(cancel_order_request)
        return response

    def list_today_orders(self, account_id, page_size=10, last_client_order_id=None):
        today_orders_list_request = TodayOrdersListRequest()
        today_orders_list_request.set_account_id(account_id)
        today_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            today_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(today_orders_list_request)
        return response

    def list_open_orders(self, account_id, page_size=10, last_client_order_id=None):
        open_orders_list_request = OpenOrdersListRequest()
        open_orders_list_request.set_account_id(account_id)
        open_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            open_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(open_orders_list_request)
        return response

    def query_order_detail(self, account_id, client_order_id):
        order_detail_request = OrderDetailRequest()
        order_detail_request.set_account_id(account_id)
        order_detail_request.set_client_order_id(client_order_id)
        response = self.client.get_response(order_detail_request)
        return response
