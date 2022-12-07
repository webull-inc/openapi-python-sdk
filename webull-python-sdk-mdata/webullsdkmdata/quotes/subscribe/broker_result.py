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


class Broker:
    def __init__(self, pb_broker):
        self.bid = Decimal(pb_broker.bid) if pb_broker.bid else None
        self.name = pb_broker.name if pb_broker.name else None

    def get_bid(self):
        return self.bid

    def get_name(self):
        return self.name

    def __repr__(self):
        return "name:%s,bid:%s" % (self.name, self.bid)

    def __str__(self):
        return self.__repr__()
