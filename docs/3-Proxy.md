# Proxy configuration

## HTTP API

Support setting HTTP/HTTPS proxy through environment variables
1. Set the environment variable HTTP_PROXY
2. Set the environment variable HTTPS_PROXY

The following code demonstrates setting up an HTTPS proxy and actively turning off certificate verification (because the proxy's certificate in the example is self-signed).

```python
import os
from webullsdkcore.client import ApiClient

proxy_host = "127.0.0.1"
proxy_port = 8888
# Set the proxy for HTTPS to 127.0.0.1:8888
os.environ['HTTPS_PROXY'] = proxy_host + ":" + str(proxy_port)
# Set verify to False, which means that the certificate provided by the proxy will not be verified
client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk", verify=False)
```

## Quotes Subscription

Support setting Socks proxy by calling `proxy_set` method. The following code demonstrates setting Socks5 proxy.

```python
import socks
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

proxy_host = "127.0.0.1"
proxy_port = 9080
quotes_client = DefaultQuotesClient("<your_app_key>", "<your_app_secret>", "hk")

# Set socks5 proxy to 127.0.0.1:9080
quotes_client.proxy_set(proxy_type=socks.SOCKS5, proxy_addr=proxy_host, proxy_port=proxy_port)
```


## Trade Events Subscription

Similar to the HTTP API, and it supports setting the proxy through environment variables.
1. Set the environment variable grpc_proxy
2. Set the environment variable https_proxy
3. Set the environment to connect http_proxy

Priority from 1 to 3
