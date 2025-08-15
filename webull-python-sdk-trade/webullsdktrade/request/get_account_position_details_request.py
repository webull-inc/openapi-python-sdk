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


class AccountPositionDetailsRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/account/position/details", version='v1', method="GET", query_params={})

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_size(self, size):
        self.add_query_param("size", size)

    def set_ticker_id(self, ticker_id):
        self.add_query_param("ticker_id", ticker_id)

    def set_last_instrument_id(self, last_instrument_id):
        self.add_query_param("last_instrument_id", last_instrument_id)