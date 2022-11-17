import logging
import threading
import time

from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType
from webullsdkmdata.quotes.grpc.pb import quote_pb2
from webullsdkmdata.quotes.grpc.response import Response
from webullsdkmdata.quotes.subscribe.basic_quote_decoder import BasicQuoteDecoder
from webullsdkmdata.quotes.subscribe.payload_type import PAYLOAD_TYPE_SHAPSHOT, PAYLOAD_TYPE_BASIC_QUOTE
from webullsdkmdata.quotes.subscribe.snapshot_decoder import SnapshotDecoder
from webullsdkmdata.request.grpc.get_streaming_token_request import GetStreamingTokenRequest
from webullsdkmdata.request.grpc.quotes_subscribe_request import SubscribeRequest
from webullsdkmdata.request.grpc.quotes_unsubscribe_request import UnsubcribeRequest

from webullsdkquotescore.quotes_client import QuotesClient


class CustomClient:
    def __init__(self, app_key, app_secret, host=None, region_id=None):
        self._token = None
        self._token_mutex = threading.Lock()
        self._condition = threading.Condition()
        self._app_key = app_key
        self._app_secret = app_secret
        self._host = host
        self.subscribe_client = QuotesClient(app_key, app_secret, region_id, host)
        self.subscribe_client.register_payload_decoder(
            PAYLOAD_TYPE_BASIC_QUOTE, BasicQuoteDecoder())
        self.subscribe_client.register_payload_decoder(PAYLOAD_TYPE_SHAPSHOT, SnapshotDecoder())
        self._grpc_client = self.subscribe_client.grpc_client

    def _on_quotes_subscribe(self, client, api_client, token):
        with self._token_mutex:
            self._token = token
            with self._condition:
                print("Notification can continue")
                self._condition.notify()

    def _get_token(self, client, api_client):
        request = GetStreamingTokenRequest()
        result = self._grpc_client.get_response(request.get_path(), request.serialize())
        response = Response(result, quote_pb2.TokenResponse())
        return response.json()['token']

    def _quote_msg(self, client, userdata, level, buf):
        print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

    def on_connect(self, wait_time=1000):
        with self._condition:
            self.subscribe_client.on_refresh_token = self._get_token
            self.subscribe_client.on_log = self._quote_msg
            self.subscribe_client.on_quotes_subscribe = self._on_quotes_subscribe
            self.subscribe_client.connect_and_loop_async()
            print("Wait for the connection to succeed")
            self._condition.wait(wait_time)

    def subscribe(self, symbols, category, sub_types):
        if self._token is None:
            raise Exception("Token is Null")
        print("token", self._token)
        request = SubscribeRequest(self._token, symbols, category, sub_types)
        result = self._grpc_client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())

    def unsubscribe(self, symbols, category, sub_types, unsubscribe_all=False):
        if self._token is None:
            raise Exception("Token is Null")
        request = UnsubcribeRequest(self._token, symbols, category, sub_types, unsubscribe_all)
        result = self._grpc_client.get_response(request.get_path(), request.serialize())
        return Response(result, quote_pb2.SubscribeResponse())


your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"
optional_quotes_endpoint = "</optional_quotes_endpoint>"

if __name__ == '__main__':
    custom_client = CustomClient(your_app_key,
                                 your_app_secret,
                                 optional_quotes_endpoint,
                                 "hk")
    custom_client.on_connect()

    try:
        # subscribe
        res = custom_client.subscribe(['00700'], Category.HK_STOCK.name,
                                      [SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name])
        print(res.path)
        print(res.request_id)
        print(res.status_code)
        print(res.msg)
        print(res.json())
    except Exception as e:
        print(e)

    time.sleep(30)

    print("unsubscribe")
    res = custom_client.unsubscribe(symbols=None, category=Category.HK_STOCK.name,
                                    sub_types=[SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name],
                                    unsubscribe_all=True)

    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
