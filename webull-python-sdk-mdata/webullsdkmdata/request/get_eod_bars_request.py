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

class GetEodBarsRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/market-data/eod-bars", version='v1', method="GET", query_params={})

    def set_instrument_ids(self, instrument_ids):
        if isinstance(instrument_ids, str):
            self.add_query_param("instrument_ids", instrument_ids)
        elif isinstance(instrument_ids, list):
            self.add_query_param("instrument_ids", ",".join(instrument_ids))

    def set_date(self, date):
        self.add_query_param("date", date)

    def set_count(self, count='1'):
        self.add_query_param("count", count)
