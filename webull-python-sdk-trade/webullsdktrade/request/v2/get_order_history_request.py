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

from webullsdkcore.request import ApiRequest


class OrderHistoryRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/openapi/account/orders/history", version='v1', method="GET", body_params={})

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_page_size(self, page_size):
        self.add_query_param("page_size", page_size)

    def set_start_date(self, start_date):
        self.add_query_param("start_date", start_date)

    def set_last_client_order_id(self, last_client_order_id):
        self.add_query_param("last_client_order_id", last_client_order_id)