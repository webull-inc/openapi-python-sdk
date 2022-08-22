# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

from webullsdkcore.retry.backoff_strategy import FixedDelayStrategy
from webullsdkcore.exception import error_code
from webullsdkcore.retry.retry_condition import RetryCondition, ClientException, MaxRetryTimesCondition, \
    MergeAndRetryCondition, MergeRetryCondition
from webullsdkcore.retry.retry_policy import RetryPolicy
from webullsdkcore.retry.retry_policy_context import RetryPolicyContext


class QuotesRetryPolicyContext(RetryPolicyContext):
    def __init__(self, exception, retries_attempted, rc_code):
        super().__init__(None, exception, retries_attempted, None)
        self.rc_code = rc_code

    def __str__(self):
        return "exception:%s, retries:%s, rc_code:%s" % (self.exception, self.retries_attempted, self.rc_code)

class RetryOnRcCodeCondition(RetryCondition):
    DEFAULT_RETRYABLE_RC_CODE_LIST = [
        3,
        5,
    ]

    def __init__(self, retryable_rc_code_list=None):
        if retryable_rc_code_list:
            self.retryable_rc_code_list = retryable_rc_code_list
        else:
            self.retryable_rc_code_list = self.DEFAULT_RETRYABLE_RC_CODE_LIST

    def should_retry(self, retry_policy_context):
        if retry_policy_context.rc_code in self.retryable_rc_code_list:
            return RetryCondition.RETRY
        else:
            return RetryCondition.NO_RETRY


class RetryOnExceptionCondition(RetryCondition):
    def __init__(self):
        RetryCondition.__init__(self)

    def should_retry(self, retry_policy_context):
        exception = retry_policy_context.exception
        if exception:
            if isinstance(exception, ClientException):
                if exception.get_error_code() == error_code.SDK_HTTP_ERROR:
                    return RetryCondition.RETRY
                else:
                    return RetryCondition.NO_RETRY
            return RetryCondition.RETRY
        return RetryCondition.NO_RETRY

class DefaultQuotesRetryCondition(RetryCondition):
    def __init__(self, max_retry_times=-1):
        RetryCondition.__init__(self)
        if max_retry_times < 0:
            _conditions = []
        else:
            _conditions = [MaxRetryTimesCondition(max_retry_times)]
        _merge_and_cnd = MergeAndRetryCondition(
            [RetryOnRcCodeCondition(), RetryOnExceptionCondition()])
        _conditions.append(_merge_and_cnd)
        self._condition = MergeRetryCondition(_conditions)

    def should_retry(self, retry_policy_context):
        return self._condition.should_retry(retry_policy_context)

class DefaultQuotesRetryPolicy(RetryPolicy):
    def __init__(self, max_retry_times=-1, fixed_delay=5000):
        RetryPolicy.__init__(self, DefaultQuotesRetryCondition(max_retry_times), FixedDelayStrategy(fixed_delay))