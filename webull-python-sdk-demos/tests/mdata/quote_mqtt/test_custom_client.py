import threading
import time

from webullsdkcore.client import ApiClient
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType

from webullsdkmdata.request.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkquotescore.quotes_client import QuotesClient
from webullsdktradehk.api import API


class CustomClient:
    def __init__(self, app_key, app_secret, api_endpoint=None, region_id=None):
        self._token = None
        self._token_mutex = threading.Lock()
        self._condition = threading.Condition()
        self._app_key = app_key
        self._app_secret = app_secret
        self._api_endpoint = api_endpoint
        self.subscribe_client = QuotesClient(app_key, app_secret, region_id)
        if region_id:
            self._api_client = ApiClient(app_key, app_secret, region_id)
            if api_endpoint:
                self._api_client.add_endpoint(region_id, api_endpoint)
        else:
            self._api_client = ApiClient(app_key, app_secret)

    def _on_quotes_subscribe(self, client, api_client, token):
        with self._token_mutex:
            self._token = token
            with self._condition:
                print("Notification can continue")
                self._condition.notify()

    def _get_token(self, client, api_client):
        request = GetStreamingTokenRequest()
        request.set_endpoint(self._api_endpoint)
        response = api_client.get_response(request)
        return response.json()["token"]

    def _quote_msg(self, client, userdata, level, buf):
        print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

    def on_connect(self, host, wait_time=60):
        with self._condition:
            self.subscribe_client.on_refresh_token = self._get_token
            self.subscribe_client.on_log = self._quote_msg
            self.subscribe_client.on_quotes_subscribe = self._on_quotes_subscribe
            self.subscribe_client.connect_and_loop_async(host=host)
            print("Wait for the connection to succeed")
            self._condition.wait(wait_time)

    def subscribe(self, symbols, category, sub_types):
        if self._token is None:
            raise Exception("Token is Null")
        api = API(self._api_client)
        return api.market_data.create_subscription_rel(self._token, symbols, category, sub_types)

    def unsubscribe(self, symbols, category, sub_types, unsubscribe_all=False):
        if self._token is None:
            raise Exception("Token is Null")
        api = API(self._api_client)
        return api.market_data.remove_subscription_rel(self._token, symbols, category, sub_types, unsubscribe_all)


if __name__ == '__main__':
    custom_client = CustomClient("<your_app_key>", "<your_app_secret>", "<api_endpoint>", "hk")
    custom_client.on_connect("<quote_endpoint>")

    # subscribe
    custom_client.subscribe(['AAPL', 'GOOG'], Category.US_STOCK.name,
                            [SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name])

    time.sleep(30)

    # unsubscribe
    custom_client.unsubscribe(['AAPL'], Category.US_STOCK.name,
                              [SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name])
