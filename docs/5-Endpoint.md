# Domain

Endpoint refers to the network domain of the requested service, such as `api.webull.hk` corresponding to the HTTP API service.

Different services will use different domain, such as `quotes-api.webull.hk`corresponding to market data services.

The `region_id` is also related to the Endpoint. For example, the `region_id` corresponding to the above two domain is hk (representing Hong Kong).

In the process of using the SDK, the Endpoint has been managed by default. Generally, the developer only needs to set the region_id correctly, and there is no need to set the Endpoint separately.

## HTTP API

There are two main ways for users to customize Endpoint

1. Set through ApiClient and take effect globally. The sample code is as follows.

```python
from webullsdkcore.client import ApiClient

client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="<region_id>")
client.add_endpoint("<region_id>", "<endpoint>")
```

2. Set by Request, and it only takes effect for the current Request. The sample code is as follows.

```python
from webullsdkmdata.request.get_instruments_request import GetInstrumentsRequest

request = GetInstrumentsRequest()
request.set_endpoint("<endpoint>")
```

## Quote subscription

1. By setting the api_endpoint parameter, the user can implement the Endpoint of the custom Http API. The sample code is as follows.

```python
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

quotes_client = DefaultQuotesClient(
       "<your_app_key>", "<your_app_secret>", "<region_id>", api_endpoint="<api_endpoint>")
```

2. By setting the host and port parameters, the user can implement the Endpoint of the custom MQTT protocol. The sample code is as follows.

```python
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

quotes_client = DefaultQuotesClient(
       "<your_app_key>", "<your_app_secret>", "<region_id>")

quotes_client.connect_and_loop_start(host="<host>", port="<port>")
```

## Trade Events Subscription

By setting the parameters of host and port, the user can implement the endpoint of the custom grpc protocol. The sample code is as follows.

```python
from webullsdktradeeventscore.events_client import EventsClient

events_client = EventsClient("<your_app_key>", "<your_app_secret>",'hk', host="<host>", port="<port>")
```