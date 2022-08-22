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

class QuotesTopic(object):
    def __init__(self, instrument_id, data_type, interval):
        self.instrument_id = instrument_id
        self.data_type = int(data_type)
        self.interval = int(interval)

    def get_instrument_id(self):
        return self.instrument_id

    def get_data_type(self):
        return self.data_type

    def get_interval(self):
        return self.interval

    def __repr__(self):
        return "%s-%s-%s" % (self.instrument_id, self.data_type, self.interval)

    def __str__(self):
        return self.__repr__()
