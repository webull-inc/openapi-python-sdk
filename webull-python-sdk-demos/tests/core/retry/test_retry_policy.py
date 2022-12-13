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
from webullsdkcore.retry import retry_policy
from webullsdkcore.retry.retry_policy_context import RetryPolicyContext
from webullsdkcore.retry.retry_condition import *
from webullsdkcore.request import ApiRequest
from webullsdkcore.exception.exceptions import ClientException, ServerException
from webullsdkcore.exception import error_code


class TestRetryPolicy(unittest.TestCase):

    def test_default_policy(self):
        policy = retry_policy.get_default_retry_policy(1)
        context = RetryPolicyContext(ApiRequest("/xxx"), ClientException(error_code.SDK_INVALID_PARAMETER), 0, None)
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx"), ClientException(error_code.SDK_HTTP_ERROR), 0, None)
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context.original_request.set_method('GET')
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(policy.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.retries_attempted = 1
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx", method='GET'), ServerException("UNKNOWN_XXX_ERR"), 0, 500)
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(policy.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.retries_attempted = 1
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context.retries_attempted = 0
        context.original_request.set_method('POST')
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, RetryCondition.NO_RETRY)
        context = RetryPolicyContext(ApiRequest("/xxx", method='GET'), ServerException("INTERNAL_ERROR"), 0, 501)
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(policy.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        context.retryable = policy.should_retry(context)
        millis = policy.compute_delay_before_next_retry(context)
        self.assertTrue(millis >= 100)
        context.exception = ServerException("TOO_MANY_REQUESTS")
        self.assertEqual(policy.should_retry(context) & RetryCondition.NO_RETRY, 0)
        self.assertEqual(policy.should_retry(context) & RetryCondition.RETRY, RetryCondition.RETRY)
        self.assertEqual(policy.should_retry(context) & RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF,
                         RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)
        context.retryable = policy.should_retry(context)
        millis = policy.compute_delay_before_next_retry(context)
        self.assertTrue(millis > 100)
