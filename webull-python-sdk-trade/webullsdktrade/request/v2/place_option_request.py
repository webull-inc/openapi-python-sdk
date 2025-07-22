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


class PlaceOptionRequest(ApiRequest):
    def __init__(self):
        super().__init__("/openapi/account/orders/option/place", version='v1', method="POST", body_params={})

    def set_new_orders(self, new_orders):
        self.add_body_params("new_orders", new_orders)

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_custom_header(self, new_orders):

        if not new_orders:
            return

        if isinstance(new_orders, list) and new_orders[0]:
            first_order = new_orders[0]
            orders_list = first_order.get("orders", [])
            if isinstance(orders_list, list):
                for sub_order in orders_list:
                    if (sub_order and isinstance(sub_order, dict)
                            and sub_order.get("instrument_type") == "OPTION"):
                        instrument_type = sub_order.get("instrument_type")
                        option_type = sub_order.get("option_type")
                        market = sub_order.get("market")
                        category = market + "_" + "EQUITY" + "_" + option_type + "_" + instrument_type
                        if category is not None:
                            self.add_header("category", category)