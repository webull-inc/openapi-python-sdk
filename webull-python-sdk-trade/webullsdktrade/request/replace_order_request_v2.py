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
from webullsdkcore.request import ApiRequest


class ReplaceOrderRequestV2(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/order/replace", version='v1', method="POST", body_params={})
        self._stock_order = {}
        self.add_body_params("stock_order", self._stock_order)

    def add_stock_order_params(self, k, v):
        self._stock_order[k] = v

    def set_account_id(self, account_id):
        self.add_body_params("account_id", account_id)

    def set_close_contracts(self, close_contracts):
        if isinstance(close_contracts, list) and all(isinstance(item, dict) for item in close_contracts):
            self.add_stock_order_params("close_contracts", close_contracts)

    def set_stock_order(self, stock_order):
        self._stock_order.update({k: v for k, v in stock_order.items() if v is not None and k != 'self'})
        if 'close_contracts' in stock_order and stock_order['close_contracts'] is not None:
            self.set_close_contracts(stock_order['close_contracts'])