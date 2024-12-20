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

class GetCorpActionRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/instrument/corp-action", version='v1', method="GET", query_params={})

    def set_instrument_ids(self, instrument_ids):
        if isinstance(instrument_ids, str):
            self.add_query_param("instrument_ids", instrument_ids)
        elif isinstance(instrument_ids, list):
            self.add_query_param("instrument_ids", ",".join(instrument_ids))

    def set_event_types(self, event_types):
        if isinstance(event_types, str):
            self.add_query_param("event_types", event_types)
        elif isinstance(event_types, list):
            self.add_query_param("event_types", ",".join(event_types))

    def set_start_date(self, start_date):
        self.add_query_param("start_date", start_date)

    def set_end_date(self, end_date):
        self.add_query_param("end_date", end_date)

    def set_page_number(self, page_number):
        self.add_query_param("page_number", page_number)

    def set_page_size(self, page_size):
        self.add_query_param("page_size", page_size)

    def set_last_update_time(self, last_update_time):
        self.add_query_param("last_update_time", last_update_time)
