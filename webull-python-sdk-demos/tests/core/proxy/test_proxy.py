import os
import unittest
import sys
import socket
from webullsdkcore.client import ApiClient
from webullsdkcore.request import ApiRequest

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


def _check_port_opened(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except Exception as e:
        print(e)
        return False


class TestProxy(unittest.TestCase):

    def test_with_proxy(self):
        proxy_host = "127.0.0.1"
        proxy_port = 8888
        if _check_port_opened(proxy_host, proxy_port):
            os.environ['HTTPS_PROXY'] = proxy_host + ":" + str(proxy_port)
            # verify = False => no ssl certs verification
            client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", verify=False)
        else:
            client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        client.set_stream_logger(stream=sys.stderr)
        request = ApiRequest("/market-data/streaming/token", version="v1")
        request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        self.assertIsNone(request.get_headers().get('Accept-Encoding'))
        client.get_response(request)
        self.assertEqual(request.get_headers()['Accept-Encoding'], 'gzip')
