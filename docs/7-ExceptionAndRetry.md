# Exception and retry mechanism

## Abnormal

### ClientException
ClientException represents an explicit client error, such as the following error codes:

| Error Code                |     Description       |
|----------------------|--------------------|
| SDK.SDK_INVALID_PARAMETER | An invalid parameter value was used, and an error was detected before the request was sent to the server. |
| SDK.SDK_ENDPOINT_RESOLVING_ERROR | Could not find a suitable Endpoint to send the request to the server | 
| SDK.SDK_INVALID_REQUEST | A Request object is used that the framework cannot handle |

### ServerException

For the request result of **status_code != 200**, the server will provide a clear error_code as the error code during the use of the HTTP API. These failed or incorrect requests are represented by the SDK through ServerException.

For the error code and cause of ServerException, please refer to the server documentation of the HTTP API.


## Retry mechanism

Different business scenarios may require different retry policies. The SDK presets retry policies and allows custom extensions and settings.

### HTTP API

#### Default mechanism
1. No retry by default
2. After the number of retries is set, qualified requests will be retried, and unqualified requests will not be retried. The code example to enable retry is as follows:

```python
from webullsdkcore.client import ApiClient

# Set the maximum number of retries to 3
client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk", auto_retry=True,
                   max_retry_num=3)
```
The descriptions of judging default retry condition:
1. Do not retry when exceeding the maximum number of retries.
2. Do no retry when it's not a GET request.
3. Client IOError will be retried, and non-specific ClientException will not be retried.
4. The specific error code of the server (below) will be retried, and the non-specific error code will not be retried.
    - TOO_MANY_REQUESTS
    - SERVICE_NOT_AVAILABLE
    - GATEWAY_TIMEOUT
    - INTERNAL_ERROR 
5. Do not retry for other errors and exceptions.

### Quote subscription

#### Default mechanism
1. By default, requests that meet the conditions will be retried, and requests that do not meet the conditions will not be retried. There is no limit to the number of retries. The retry interval is 5 seconds. The code example of custom retry is as follows:

```python
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient
from webullsdkcore.retry.retry_policy import NO_RETRY_POLICY

# No Retry setting
quotes_client = DefaultQuotesClient("<your_app_key>", "<your_app_secret>", "<region_id>", retry_policy=NO_RETRY_POLICY)
```
The default retry condition judgment description:
1. Client IOError will be retried, and non-specific ClientException will not be retried.
2. The specific error code of the mqtt protocol (as follows) is retried, and the non-specific error code is not retried.
    - 3 (Server Unavailable)
    - 5 (Authorization error)
3. Retry when there are other errors and exceptions.

### Trade Events Subscription

#### Default mechanism
1. By default, requests that meet the conditions will be retried, and requests that do not meet the conditions will not be retried. There is no limit to the number of retries. The retry interval is 5 seconds. The code example of custom retry is as follows:

```python
from webullsdktradeeventscore.events_client import EventsClient
from webullsdkcore.retry.retry_policy import NO_RETRY_POLICY

# No Retry setting
client = EventsClient("<your_app_key>", "<your_app_secret>", "hk", retry_policy=NO_RETRY_POLICY)
```
The default retry condition judgment description:
1. The specific error code of the grpc protocol (as follows) is retried, and the non-specific error code is not retried.
    - 2 （UNKNOWN)
    - 13 (INTERNAL)
    - 14 (UNAVAILABLE)
2. Do not retry for other errors and exceptions.


## Custom retry strategy

Custom retry policy, mainly implemented by extending `RetryPolicy`

`RetryPolicy` realizes the conditional judgment of whether to retry through `RetryCondition`, and realizes the backoff strategy of retry interval through BackoffStrategy.

The following code demonstrates the implementation of `RetryOnRcCodeCondition`:

```python
# RetryCondition is implemented according to the error code of the mqtt protocol.
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
```

The following code demonstrates the implementation of `ExponentialBackoffStrategy`.

```python
# A Simple Exponential Backoff Strategy
class ExponentialBackoffStrategy(BackoffStrategy): 
    MAX_RETRY_LIMIT = 30
    
    def __init__(self, base_delay_in_milliseconds, max_delay_in_milliseconds):
        self.base_delay_in_milliseconds = base_delay_in_milliseconds
        self.max_delay_in_milliseconds = max_delay_in_milliseconds

    def compute_delay_before_next_retry(self, retry_policy_context):
        retries = min(self.MAX_RETRY_LIMIT, retry_policy_context.retries_attempted)
        delay = min(self.max_delay_in_milliseconds, self.base_delay_in_milliseconds << retries)
        return delay
```

The following code demonstrates a simple `RetryPolicy` implementation:

```python
class MyRetryPolicy(RetryPolicy):
    def __init__(self):
        RetryPolicy.__init__(self, RetryOnRcCodeCondition(), ExponentialBackoffStrategy())
```