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
from unittest.mock import patch

import webullsdktradeeventscore.events_pb2 as pb
from webullsdktradeeventscore.signature_composer import calc_signature


class TestSignature(unittest.TestCase):

    @patch("webullsdkcore.utils.common.get_iso_8601_date")
    @patch("webullsdkcore.utils.common.get_uuid")
    def test_calc_signature(self, mock_get_uuid, mock_get_iso_8601_date):
        mock_get_iso_8601_date.return_value = "2022-01-04T03:55:31Z"
        mock_get_uuid.return_value = "my-uuid"
        app_key = "app_key _mocked"
        app_secret = "app_secret_mocked"
        request = pb.SubscribeRequest()
        signature, metadata = calc_signature(app_key, app_secret, request)
        print(signature, metadata)

        request = pb.SubscribeRequest(
            subscribeType=1,
            timestamp=100000000,
            accounts=["account_0"],
        )
        signature, metadata = calc_signature(app_key, app_secret, request)
        print(signature, metadata)

        request = pb.SubscribeRequest(
            accounts=["account_0", "", " "],
        )
        signature, metadata = calc_signature(app_key, app_secret, request)
        print(signature, metadata)
