# coding=utf-8

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
