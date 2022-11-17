import logging
import time
from threading import Lock

import grpc
import webullsdkquotescore
from webullsdkcore import compat
from webullsdkcore.retry.retry_condition import RetryCondition
from webullsdkquotescore.grpc.grpc_retry_policy import SubscribeRetryPolicyContext

logger = logging.getLogger(__name__)


class Retry(object):

    def __init__(self, retry_policy, host):
        self._retries = 0
        self._final_exception = None
        self._retry_context = SubscribeRetryPolicyContext(self._final_exception, self._retries, None)
        self._lock = Lock()
        self._retry_policy = retry_policy
        self._host = host

    def should_recover(self, exception):
        with self._lock:
            if isinstance(exception, grpc.RpcError):
                state = exception._state
                self._final_exception = exception
                self._retry_context = SubscribeRetryPolicyContext(None, self._retries, state.code)
                msg = "gRPC error code:%s, error msg:%s, details:%s. Host:%s SDK-Version:%s " % (
                    state.code, state.details, state.debug_error_string, self._host, webullsdkquotescore.__version__)
                logger.error(compat.ensure_string(msg))

            else:
                self._final_exception = exception
                self._retry_context = SubscribeRetryPolicyContext(exception, self._retries, None)
                msg = "gRPC exception Host:%s SDK-Version:%s" % (
                    self._host, webullsdkquotescore.__version__)
                logger.error(compat.ensure_string(msg))

            retryable = self._retry_policy.should_retry(self._retry_context)
            if retryable & RetryCondition.NO_RETRY:
                return False
            self._retry_context.retryable = retryable
            time_to_wait = self._retry_policy.compute_delay_before_next_retry(self._retry_context)
            time.sleep(time_to_wait / 1000.0)
            self._retries += 1
            self._retry_context.retries_attempted = self._retries
            return True
