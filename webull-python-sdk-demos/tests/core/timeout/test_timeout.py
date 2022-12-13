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

import unittest
from webullsdkcore.client import ApiClient
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest

# 'hk' or 'us'
region_id = '<region_id>'


class TestTimeout(unittest.TestCase):

    def test_timeout(self):
        # Set the connection timeout to 3 seconds and the read timeout to 6 seconds.
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id=region_id,
                           connect_timeout=3,
                           timeout=6)

        request = GetInstrumentsRequest()
        # Set the connection timeout of the request to 2 seconds and the read timeout to 4 seconds, only valid for the current request.
        request.set_connect_timeout(2)
        request.set_read_timeout(4)
        request.set_category("HK_STOCK")
        request.set_symbols("00700")
        client.get_response(request)
