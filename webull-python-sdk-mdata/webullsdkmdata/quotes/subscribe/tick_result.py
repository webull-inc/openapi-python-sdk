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

from decimal import Decimal
from webullsdkmdata.quotes.subscribe.basic_result import BasicResult


class TickResult:
    def __init__(self, pb_tick):
        self.basic = BasicResult(pb_tick.basic)
        self.time = pb_tick.time
        self.price = Decimal(pb_tick.price) if pb_tick.price else None
        self.volume = pb_tick.volume if pb_tick.volume else None
        self.side = pb_tick.side if pb_tick.side else None

    def get_basic(self):
        return self.basic

    def get_price(self):
        return self.price

    def get_volume(self):
        return self.volume

    def get_time(self):
        return self.time

    def get_side(self):
        return self.side

    def __repr__(self):
        return "%s, price:%s, volume:%s, time:%s, side:%s" \
               % (self.basic, self.price, self.volume, self.time, self.side)

    def __str__(self):
        return self.__repr__()
