# Log

## HTTP API

The following code demonstrates a custom format, using stream for output.

```python
from webullsdkcore.client import ApiClient

client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk")
log_format='%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'
client.set_stream_logger(stream=sys.stdout, format_string=log_format)
```

The following code demonstrates a custom format, using a file for output.

```python
from webullsdkcore.client import ApiClient

client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk")
log_format='%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'
log_file_path='<my_file_path>'
client.set_file_logger(path=log_file_path, format_string=log_format)
```

## Quotes Subscription

The following code demonstrates simple processing of log data using print through the callback function on_log.

```python
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

quotes_client = DefaultQuotesClient("<your_app_key>", "<your_app_secret>", "hk")
def _on_log_func(client, userdata, level, log_data_buf):
    print("level:%s, buf:%s" % (level, log_data_buf))
quotes_client.on_log = _on_log_func
```

## Trade Events Subscription

The following code demonstrates simple processing of log data using print through the callback function on_log.

```python
from webullsdktradeeventscore.events_client import EventsClient

events_client = EventsClient("<your_app_key>", "<your_app_secret>", "hk")
def _on_log_func(level, log_data_buf):
    print("level:%s, buf:%s" % (level, log_data_buf))
enents_client.on_log = _on_log_func
```
