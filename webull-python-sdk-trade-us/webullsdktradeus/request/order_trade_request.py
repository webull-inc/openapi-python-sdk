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
from webullsdkcore.request import ApiRequest

from webullsdktradeus.common.order_entity import StockOrder, OptionOrder, CryptoOrder


class OrderTradeRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/order/place", method="POST", body_params={})

    def set_category(self, category):
        self.add_body_params("category", category)

    def set_account_id(self, account_id):
        self.add_body_params("account_id", account_id)

    def set_stock_order(self, client_order_id, instrument_id, side, tif, order_type, entrust_type,
                        extended_hours_trading=False, limit_price=None, stop_price=None, trailing_type=None,
                        trailing_stop_step=None, qty=None, amount=None):
        stock_order = StockOrder(client_order_id, instrument_id, side, tif, order_type, entrust_type,
                                 extended_hours_trading, limit_price, stop_price, trailing_type,
                                 trailing_stop_step, qty, amount)
        stock_order_params = stock_order.get_stock_order_params()
        self.add_body_params("stock_order", stock_order_params)

    def set_option_order(self, client_order_id, side, tif, order_type, option_strategy, limit_price=None,
                         stop_price=None, qty=None, amount=None, instrument_id=None, legs=None):
        option_order = OptionOrder(client_order_id, side, tif, order_type, option_strategy, limit_price, stop_price,
                                   qty, amount, instrument_id, legs)
        option_order_params = option_order.get_option_order_params()
        self.add_body_params("option_order", option_order_params)

    def set_crypto_order(self, client_order_id, instrument_id, side, tif, order_type, entrust_type,limit_price=None,
                         qty=None, amount=None):
        crypto_order = CryptoOrder(client_order_id, instrument_id, side, tif, order_type, entrust_type, limit_price,
                                   qty, amount)
        crypto_order_params = crypto_order.get_crypto_order_params()
        self.add_body_params("crypto_order", crypto_order_params)





