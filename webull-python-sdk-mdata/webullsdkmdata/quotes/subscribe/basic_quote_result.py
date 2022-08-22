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

from decimal import Decimal
from webullsdkmdata.quotes.subscribe.basic_result import BasicResult


class BasicQuoteResult:
    def __init__(self, pb_quote):
        self.basic = BasicResult(pb_quote.basic)
        self.ask_size = Decimal(
            pb_quote.ask_size) if pb_quote.ask_size else None
        self.ask_price = Decimal(
            pb_quote.ask_price) if pb_quote.ask_price else None
        self.bid_size = Decimal(
            pb_quote.bid_size) if pb_quote.bid_size else None
        self.bid_price = Decimal(
            pb_quote.bid_price) if pb_quote.bid_price else None

    def get_basic(self):
        return self.basic

    def get_ask_size(self):
        return self.ask_size

    def get_ask_price(self):
        return self.ask_price

    def get_bid_size(self):
        return self.bid_size

    def get_bid_price(self):
        return self.bid_price

    def __repr__(self):
        return "%s, ask_size:%s, ask_price:%s, bid_size:%s, bid_price:%s" \
            % (self.basic, self.ask_size, self.ask_price, self.bid_size, self.bid_price)

    def __str__(self):
        return self.__repr__()
