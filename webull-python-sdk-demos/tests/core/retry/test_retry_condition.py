# coding=utf-8
import unittest
from webullsdkcore.retry.retry_policy_context import RetryPolicyContext
from webullsdkcore.retry.retry_condition import *
from webullsdkcore.request import ApiRequest
from webullsdkcore.exception.exceptions import ClientException, ServerException
from webullsdkcore.exception import error_code


class TestRetryCondition(unittest.TestCase):

    def test_no_retry(self):
        retry_condition = NoRetryCondition()
        context = RetryPolicyContext(None, None, None, None)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx", method='GET'), ClientException(error_code.SDK_HTTP_ERROR), 10,
                                     None)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)

    def test_max_retry_times(self):
        retry_condition = MaxRetryTimesCondition(1)
        context = RetryPolicyContext(None, None, 0, None)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)
        context.retries_attempted = 1
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)

    def test_retry_on_exception(self):
        retry_config = {
            "api": {
                "RetryableThrottlingErrors": [
                    "TOO_MANY_REQUESTS",
                ],
                "RetryableNormalErrors": [
                    "SERVICE_NOT_AVAILABLE",
                    "GATEWAY_TIMEOUT",
                    "INTERNAL_ERROR",
                ]
            }
        }
        retry_condition = RetryOnExceptionCondition(retry_config)
        context = RetryPolicyContext(None, ClientException(error_code.SDK_HTTP_ERROR), None, None)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)
        context.exception = ClientException(error_code.SDK_INVALID_PARAMETER)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context.exception = ServerException("INTERNAL_ERROR")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)
        context.exception = ServerException("INCORRECT_SIGN")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)

    def test_retry_on_methodtype(self):
        retry_config = {
            "api": {
                "RetryableMethods": [
                    "GET"
                ]
            }
        }
        retry_condition = RetryOnMethodTypeCondition(retry_config)
        context = RetryPolicyContext(ApiRequest("/xxx"), RuntimeError(), None, None)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context.exception = ClientException("")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context.exception = ServerException("")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context.original_request = ApiRequest("/xxx", method="get")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context.original_request = ApiRequest("/xxx", method="GET")
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)

    def test_retry_on_http_status(self):
        retry_condition = RetryOnHttpStatusCondition()
        context = RetryPolicyContext(None, None, None, 417)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context = RetryPolicyContext(None, None, None, 200)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context = RetryPolicyContext(None, None, None, 401)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context = RetryPolicyContext(None, None, None, 501)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.NO_RETRY)
        context = RetryPolicyContext(None, None, None, 500)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)
        context = RetryPolicyContext(None, None, None, 502)
        self.assertEqual(retry_condition.should_retry(context), RetryCondition.RETRY)

    def test_default_config_retry(self):
        retry_condition = DefaultConfigRetryCondition(max_retry_times=1)
        context = RetryPolicyContext(ApiRequest("/xxx"), ClientException(error_code.SDK_INVALID_PARAMETER), 0, None)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx"), ClientException(error_code.SDK_HTTP_ERROR), 0, None)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context.original_request.set_method('GET')
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.retries_attempted = 1
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx", method='GET'), ServerException("UNKNOWN_XXX_ERR"), 0, 500)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.retries_attempted = 1
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context.retries_attempted = 0
        context.original_request.set_method('POST')
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx", method='GET'), ServerException("INTERNAL_ERROR"), 0, 501)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.exception = ServerException("TOO_MANY_REQUESTS")
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        self.assertEqual(retry_condition.should_retry(context) & RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF,
                         RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)
