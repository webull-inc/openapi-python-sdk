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
import grpc
from webullsdkcore.retry.retry_policy import RetryPolicy
from webullsdkcore.retry.backoff_strategy import FixedDelayStrategy
from webullsdkcore.retry.retry_condition import RetryCondition, MaxRetryTimesCondition, MergeRetryCondition
from webullsdkcore.retry.retry_policy_context import RetryPolicyContext

class SubscribeRetryPolicyContext(RetryPolicyContext):
    def __init__(self, exception, retries_attempted, grpc_status_code):
        super().__init__(None, exception, retries_attempted, None)
        self.grpc_status_code = grpc_status_code

    def __str__(self):
        return "exception:%s, retries:%s, grpc_status_code:%s" % (self.exception, self.retries_attempted, self.grpc_status_code)

class RetryOnGrpcStatusCondition(RetryCondition):
    DEFAULT_RETRYABLE_GRPC_STATUS_LIST = [
        grpc.StatusCode.UNAVAILABLE,
        grpc.StatusCode.INTERNAL,
        grpc.StatusCode.UNKNOWN
    ]

    def __init__(self, retryable_grpc_status_list=None):
        if retryable_grpc_status_list:
            self.retryable_grpc_status_list = retryable_grpc_status_list
        else:
            self.retryable_grpc_status_list = self.DEFAULT_RETRYABLE_GRPC_STATUS_LIST

    def should_retry(self, retry_policy_context):
        if retry_policy_context.grpc_status_code in self.retryable_grpc_status_list:
            return RetryCondition.RETRY
        else:
            return RetryCondition.NO_RETRY

class DefaultSubscribeRetryCondition(RetryCondition):
    def __init__(self, max_retry_times=-1):
        RetryCondition.__init__(self) 
        if max_retry_times < 0:
            _conditions = []
        else:
            _conditions = [MaxRetryTimesCondition(max_retry_times)]
        _conditions.append(RetryOnGrpcStatusCondition())
        self._condition = MergeRetryCondition(_conditions)

    def should_retry(self, retry_policy_context):
        return self._condition.should_retry(retry_policy_context)
            
class DefaultSubscribeRetryPolicy(RetryPolicy):
    def __init__(self, max_retry_times=-1, fixed_delay=5000):
        RetryPolicy.__init__(self, DefaultSubscribeRetryCondition(max_retry_times), FixedDelayStrategy(fixed_delay))