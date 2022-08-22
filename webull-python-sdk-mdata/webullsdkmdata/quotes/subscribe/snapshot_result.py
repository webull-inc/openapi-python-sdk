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


class SnapshotResult:
    def __init__(self, pb_snapshot):
        self.basic = BasicResult(pb_snapshot.basic)
        self.open = Decimal(pb_snapshot.open) if pb_snapshot.open else None
        self.high = Decimal(pb_snapshot.high) if pb_snapshot.high else None
        self.low = Decimal(pb_snapshot.low) if pb_snapshot.low else None
        self.price = Decimal(pb_snapshot.price) if pb_snapshot.price else None
        self.pre_close = Decimal(
            pb_snapshot.pre_close) if pb_snapshot.pre_close else None
        self.volume = Decimal(
            pb_snapshot.volume) if pb_snapshot.volume else None
        self.change = Decimal(
            pb_snapshot.change) if pb_snapshot.change else None
        self.change_ratio = Decimal(
            pb_snapshot.change_ratio) if pb_snapshot.change_ratio else None
        self.ask_size = Decimal(
            pb_snapshot.ask_size) if pb_snapshot.ask_size else None
        self.ask_price = Decimal(
            pb_snapshot.ask_price) if pb_snapshot.ask_price else None
        self.bid_size = Decimal(
            pb_snapshot.bid_size) if pb_snapshot.bid_size else None
        self.bid_price = Decimal(
            pb_snapshot.bid_price) if pb_snapshot.bid_price else None

    def get_basic(self):
        return self.basic

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_price(self):
        return self.price

    def get_pre_close(self):
        return self.pre_close

    def get_volume(self):
        return self.volume

    def get_change(self):
        return self.change

    def get_change_ratio(self):
        return self.change_ratio

    def get_ask_size(self):
        return self.ask_size

    def get_ask_price(self):
        return self.ask_price

    def get_bid_size(self):
        return self.bid_size

    def get_bid_price(self):
        return self.bid_price

    def __repr__(self):
        return "%s, open:%s, high:%s, low:%s, price:%s, pre_close:%s, volume:%s, change:%s, change_ratio:%s, ask_size:%s, ask_price:%s, bid_size:%s, bid_price:%s" \
            % (self.basic, self.open, self.high, self.low, self.price, self.pre_close, self.volume, self.change, self.change_ratio, self.ask_size, self.ask_price, self.bid_size, self.bid_price)

    def __str__(self):
        return self.__repr__()
