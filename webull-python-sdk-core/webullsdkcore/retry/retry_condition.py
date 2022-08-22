# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import jmespath
from webullsdkcore.utils import data
from webullsdkcore.utils import validation
from webullsdkcore.exception.exceptions import ClientException, ServerException
from webullsdkcore.exception import error_code
from webullsdkcore.common.api_type import DEFAULT as HTTP_API_TYPE


logger = logging.getLogger(__name__)


def _find_data_in_retry_config(key_name, request, retry_config, api_type=HTTP_API_TYPE):
    path = '"{0}"."{1}"'.format(api_type, key_name)
    return jmespath.search(path, retry_config)


class RetryCondition(object):
    BLANK_STATUS = 0
    NO_RETRY = 1
    RETRY = 2
    SHOULD_RETRY_WITH_THROTTLING_BACKOFF = 4

    def should_retry(self, retry_policy_context):
        """Decide whether the previous request should be retried."""
        pass


class NoRetryCondition(RetryCondition):
    def should_retry(self, retry_policy_context):
        return RetryCondition.NO_RETRY


class MaxRetryTimesCondition(RetryCondition):

    def __init__(self, max_retry_times):
        validation.assert_integer_positive(max_retry_times, "max_retry_times")
        self.max_retry_times = max_retry_times

    def should_retry(self, retry_policy_context):

        if retry_policy_context.retries_attempted < self.max_retry_times:
            return RetryCondition.RETRY
        else:
            logger.debug("Reached the maximum number of retry. Attempts:%d",
                         retry_policy_context.retries_attempted)
            return RetryCondition.NO_RETRY


class RetryOnExceptionCondition(RetryCondition):
    def __init__(self, retry_config):
        self.retry_config = retry_config

    def should_retry(self, retry_policy_context):
        request = retry_policy_context.original_request
        exception = retry_policy_context.exception

        if isinstance(exception, ClientException) and exception.get_error_code() == error_code.SDK_HTTP_ERROR:
            logger.debug("Retryable ClientException:%s", exception)
            return RetryCondition.RETRY

        if isinstance(exception, ServerException):
            _error_code = exception.get_error_code()
            errors = _find_data_in_retry_config(
                "RetryableNormalErrors", request, self.retry_config)
            if isinstance(errors, list) and _error_code in errors:
                logger.debug("Retryable ServerException:%s", exception)
                return RetryCondition.RETRY
            errors = _find_data_in_retry_config(
                "RetryableThrottlingErrors", request, self.retry_config)
            if isinstance(errors, list) and _error_code in errors:
                logger.debug("Retryable ThrottlingError:%s", exception)
                return RetryCondition.RETRY | RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF

        return RetryCondition.NO_RETRY


class RetryOnMethodTypeCondition(RetryCondition):
    def __init__(self, retry_config):
        self.retry_config = retry_config

    def should_retry(self, retry_policy_context):
        request = retry_policy_context.original_request
        exception = retry_policy_context.exception

        if isinstance(exception, (ClientException, ServerException)):
            method = request.get_method()
            methods = _find_data_in_retry_config(
                "RetryableMethods", request, self.retry_config)
            if isinstance(methods, list) and method in methods:
                logger.debug("Retryable MethodType:%s", method)
                return RetryCondition.RETRY

        return RetryCondition.NO_RETRY


class RetryOnHttpStatusCondition(RetryCondition):

    DEFAULT_RETRYABLE_HTTP_STATUS_LIST = [
        500, 502, 503, 504
    ]

    def __init__(self, retryable_http_status_list=None):
        if retryable_http_status_list:
            self.retryable_http_status_list = retryable_http_status_list
        else:
            self.retryable_http_status_list = self.DEFAULT_RETRYABLE_HTTP_STATUS_LIST

    def should_retry(self, retry_policy_context):
        if retry_policy_context.http_status_code in self.retryable_http_status_list:
            logger.debug(
                "Retryable HTTP error occurred. HTTP status code: %s",
                retry_policy_context.http_status_code)
            return RetryCondition.RETRY
        else:
            return RetryCondition.NO_RETRY


class MergeRetryCondition(RetryCondition):
    def __init__(self, conditions):
        self.conditions = conditions

    def should_retry(self, retry_policy_context):
        retryable = RetryCondition.BLANK_STATUS
        for condition in self.conditions:
            retryable |= condition.should_retry(retry_policy_context)
        return retryable


class MergeAndRetryCondition(RetryCondition):
    def __init__(self, conditions):
        self.conditions = conditions

    def should_retry(self, retry_policy_context):
        retryable = RetryCondition.BLANK_STATUS
        no_retry = RetryCondition.NO_RETRY
        retry_mask = RetryCondition.RETRY | RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF
        for condition in self.conditions:
            ret = condition.should_retry(retry_policy_context)
            retryable |= ret & retry_mask
            no_retry &= ret & RetryCondition.NO_RETRY
        return retryable | no_retry


class DefaultMixedRetryCondition(RetryCondition):
    def __init__(self, max_retry_times, retry_config):
        RetryCondition.__init__(self)
        self._condition = MergeRetryCondition([
            MaxRetryTimesCondition(max_retry_times),
            RetryOnMethodTypeCondition(retry_config),
            MergeAndRetryCondition([
                RetryOnExceptionCondition(retry_config),
                RetryOnHttpStatusCondition(),
            ]),
        ])

    def should_retry(self, retry_policy_context):
        return self._condition.should_retry(retry_policy_context)


class DefaultConfigRetryCondition(DefaultMixedRetryCondition):
    DEFAULT_MAX_RETRY_TIMES = 3
    RETRY_CONFIG_FILE = "retry_config.json"
    _loaded_config = None

    def __init__(self, max_retry_times=None):
        if not self._loaded_config:
            self._loaded_config = data._load_json_from_data_dir(
                self.RETRY_CONFIG_FILE)
        if max_retry_times is None:
            max_retry_times = self.DEFAULT_MAX_RETRY_TIMES
        DefaultMixedRetryCondition.__init__(
            self, max_retry_times, self._loaded_config)
