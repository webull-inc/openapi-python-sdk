# coding=utf-8

import logging
import unittest
from webullsdktradeeventscore.events_client import EventsClient
from webullsdkcore.retry.retry_policy import NO_RETRY_POLICY, RetryPolicy
from webullsdkcore.retry.retry_condition import MaxRetryTimesCondition
from webullsdkcore.retry.backoff_strategy import FixedDelayStrategy, NoDelayStrategy
from webullsdktradeeventscore.default_retry_policy import DefaultSubscribeRetryPolicy
from unittest.mock import patch

PRE_HOST = "hk-openapi-events-api.uat.webullbroker.com"


class TestClient(unittest.TestCase):

    def test_error_appkey(self):
        client = EventsClient("app_key_mocked", "app_secret_mocked", host=PRE_HOST, retry_policy=NO_RETRY_POLICY)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["<your_account_id>"])
        except:
            pass

    def test_error_appkey_and_retry(self):
        retry_policy = RetryPolicy(MaxRetryTimesCondition(3), FixedDelayStrategy(1000))
        client = EventsClient("app_key_mocked", "app_secret_mocked", host=PRE_HOST, retry_policy=retry_policy)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["<your_account_id>"])
        except:
            pass

    def test_error_accounts(self):
        client = EventsClient("<your_app_key>", "app_secret_mocked", host=PRE_HOST)
        client.enable_logger()
        try:
            client.do_subscribe(["account_mocked"])
        except:
            pass
        try:
            client.do_subscribe("invalid_account_0,account_1")
        except:
            pass
        try:
            client.do_subscribe([])
        except:
            pass

    @patch("webullsdkcore.utils.common.get_uuid")
    def test_replay_connection(self, mock_get_uuid):
        mock_get_uuid.return_value = "the_same_nonce_value"
        retry_policy = RetryPolicy(MaxRetryTimesCondition(10), NoDelayStrategy())
        client = EventsClient("<your_app_key>", "app_secret_mocked", host=PRE_HOST, retry_policy=retry_policy)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["account_mocked"])
        except:
            pass

    def test_normal(self):
        client = EventsClient("<your_app_key>", "<your_app_secret>", host=PRE_HOST)
        client.on_log = self._on_log
        client.do_subscribe(["<your_account_id>"])

    @staticmethod
    def _on_log(level, log_content):
        print(logging.getLevelName(level), log_content)
