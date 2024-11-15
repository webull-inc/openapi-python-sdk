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
import json
# coding=utf-8
from typing import List

from webullsdkcore.request import ApiRequest


class CloseContract:
    def __init__(self, contract_id: str, quantity: str):
        self.contract_id = contract_id
        self.quantity = quantity

    def to_dict(self):
        return {
            "contract_id": self.contract_id,
            "quantity": self.quantity
        }

class PlaceOrderRequest(ApiRequest):
    def __init__(self):
        super().__init__("/openapi/account/orders/place", version='v1', method="POST", body_params={})
        self._new_orders = []
        self._current_order = {}
        self.add_body_params("new_orders", self._new_orders)

    def add_new_order_params(self, key, value):
        self._current_order[key] = value

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_close_contracts(self, close_contracts: List[CloseContract]):
        if not isinstance(close_contracts, list):
            raise TypeError("close_contracts must be a list of CloseContract objects.")
        self.add_new_order_params("close_contracts", [contract.to_dict() for contract in close_contracts])

    def set_new_orders(self, current_order):
        self._current_order.update({k: v for k, v in current_order.items() if v is not None and k != 'self'})
        if 'close_contracts' in current_order and current_order['close_contracts'] is not None:
            self.set_close_contracts(current_order['close_contracts'])

    def finalize_order(self):
        if self._current_order:
            self._new_orders.append(self._current_order)
            self._current_order = {}
        else:
            raise ValueError("No order fields have been set.")
