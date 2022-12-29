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

from decimal import Decimal
from webullsdkmdata.quotes.subscribe.order_result import Order
from webullsdkmdata.quotes.subscribe.broker_result import Broker


class AskBidResult:
    def __init__(self, ask_bid):
        self.price = Decimal(ask_bid.price) if ask_bid.price else None
        self.size = ask_bid.size
        self.order = []
        if ask_bid.order:
            for order in ask_bid.order:
                self.order.append(Order(order))
        self.broker = []
        if ask_bid.broker:
            for broker in ask_bid.broker:
                self.broker.append(Broker(broker))

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def get_order(self):
        return self.order

    def get_broker(self):
        return self.broker

    def __repr__(self):
        return "price:%s,size:%s,order:%s,broker:%s" % (self.price, self.size, self.order, self.broker)

    def __str__(self):
        return self.__repr__()
