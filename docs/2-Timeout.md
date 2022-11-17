# Timeout mechanism

## HTTP API

The timeout setting of the HTTP API is relatively flexible. The priority of the settings decreases in turn: Request object -> Client object -> Default value.

The default connection timeout is 5 seconds and the read timeout is 10 seconds.

The following code demonstrates how to customize the timeout setting.

```python
from webullsdkcore.client import ApiClient
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest
# Set the connection timeout to 3 seconds and the read timeout to 6 seconds.
client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret", region_id="hk", connect_timeout=3,
                   timeout=6)

request = GetInstrumentsRequest()
# Set the connection timeout of the request to 2 seconds and the read timeout to 4 seconds, only valid for the current request.
request.set_connect_timeout(2)
request.set_read_timeout(4)
```

## Quote subscription

Market subscription is a long connection based on `MQTT v3.1.1`. The default connection timeout is 5 seconds, and the read timeout is 60 seconds (the connection will be maintained through the heartbeat packet within 60 seconds). Currently, there is no method for customizing the timeout configuration.

## Trade Events Subscription / Quotes API

The trading events subscription is based on the long connection of `Server Streaming` implemented by `grpc`. Currently, there is no way to customize the timeout configuration. The timeout is managed by [python's grpc libs](https://grpc.io/docs/languages/python/basics/) by default.