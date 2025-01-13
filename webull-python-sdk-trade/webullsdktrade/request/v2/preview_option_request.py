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


class PreviewOptionRequest(ApiRequest):
    def __init__(self):
        super().__init__("/openapi/account/orders/option/preview", version='v1', method="POST", body_params={})

    def set_new_orders(self, new_orders):
        self.add_body_params("new_orders", new_orders)

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)