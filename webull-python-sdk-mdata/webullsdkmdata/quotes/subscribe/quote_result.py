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

from decimal import Decimal
from webullsdkmdata.quotes.subscribe.basic_result import BasicResult
from webullsdkmdata.quotes.subscribe.ask_bid_result import AskBidResult


class QuoteResult:
    def __init__(self, pb_quote):
        self.basic = BasicResult(pb_quote.basic)
        self.asks = []
        if pb_quote.asks:
            for ask in pb_quote.asks:
                self.asks.append(AskBidResult(ask))
        self.bids = []
        if pb_quote.bids:
            for bid in pb_quote.bids:
                self.bids.append(AskBidResult(bid))

    def get_basic(self):
        return self.basic

    def get_asks(self):
        return self.asks

    def get_bids(self):
        return self.bids

    def __repr__(self):
        return "basic: %s,asks: %s,bids:%s" % (self.basic, self.asks, self.bids)

    def __str__(self):
        return self.__repr__()
