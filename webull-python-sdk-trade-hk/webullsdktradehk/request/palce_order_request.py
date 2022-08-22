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
import inspect

from webullsdkcore.request import ApiRequest

class PlaceOrderRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/order/place", version='v1', method="POST", body_params={})
        self._stock_order = {}
        self.add_body_params("stock_order", self._stock_order)

    def add_stock_order_params(self, k, v):
        self._stock_order[k] = v

    def set_category(self, category):
        self.add_body_params("category", category)

    def set_account_id(self, account_id):
        self.add_body_params("account_id", account_id)

    def set_client_order_id(self, client_order_id):
        self.add_stock_order_params("client_order_id", client_order_id)

    def set_side(self, side):
        self.add_stock_order_params("side", side)

    def set_tif(self, tif):
        self.add_stock_order_params("tif", tif)

    def set_extended_hours_trading(self, extended_hours_trading):
        self.add_stock_order_params("extended_hours_trading", extended_hours_trading)

    def set_instrument_id(self, instrument_id):
        self.add_stock_order_params("instrument_id", instrument_id)

    def set_order_type(self, order_type):
        self.add_stock_order_params("order_type", order_type)

    def set_limit_price(self, limit_price):
        self.add_stock_order_params("limit_price", limit_price)

    def set_qty(self, quantity):
        self.add_stock_order_params("qty", quantity)

    def set_stop_price(self, stop_price):
        self.add_stock_order_params("stop_price", stop_price)

    def set_trailing_type(self, trailing_type):
        self.add_stock_order_params("trailing_type", trailing_type)

    def set_trailing_stop_step(self, trailing_stop_step):
        self.add_stock_order_params("trailing_stop_step", trailing_stop_step)

    def set_stock_order(self, client_order_id,  instrument_id, qty, side, tif, extended_hours_trading,
                        order_type, limit_price, stop_price, trailing_type,trailing_stop_step):
        self._stock_order.update({k: v for k, v in locals().items() if v is not None and k != 'self'})








