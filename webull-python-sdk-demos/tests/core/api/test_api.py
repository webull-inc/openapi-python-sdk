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
import sys
from webullsdkcore.client import ApiClient
from webullsdkcore.request import ApiRequest

OPENAPI_ENDPOINT = "<api_endpoint>"


class TestApiClient(unittest.TestCase):

    def test_api(self):
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        client.set_stream_logger(stream=sys.stderr)
        request = ApiRequest("/market-data/streaming/token", version="v1")
        request.set_endpoint(OPENAPI_ENDPOINT)
        self.assertIsNone(request.get_headers().get('Accept-Encoding'))
        client.get_response(request)
        self.assertEqual(request.get_headers()['Accept-Encoding'], 'gzip')
