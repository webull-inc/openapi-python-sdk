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


class TradeSecurityDetailRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/security", version='v1', method="GET", query_params={})

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_symbol(self, symbol):
        self.add_query_param("symbol", symbol)

    def set_market(self, market):
        self.add_query_param("market", market)

    def set_instrument_super_type(self, instrument_super_type):
        self.add_query_param("instrument_super_type", instrument_super_type)

    def set_instrument_type(self, instrument_type):
        self.add_query_param("instrument_type", instrument_type)

    def set_strike_price(self, strike_price):
        self.add_query_param("strike_price", strike_price)

    def set_init_exp_date(self, init_exp_date):
        self.add_query_param("init_exp_date", init_exp_date)
