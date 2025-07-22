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

class BatchHistoricalBarsRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/market-data/batch-bars", version='v1', method="POST")

    def set_symbols(self, symbol):
        self.add_body_params("symbols", symbol)

    def set_category(self, category):
        self.add_body_params("category", category)

    def set_timespan(self, timespan):
        self.add_body_params("timespan", timespan)

    def set_count(self, count='200'):
        self.add_body_params("count", count)
