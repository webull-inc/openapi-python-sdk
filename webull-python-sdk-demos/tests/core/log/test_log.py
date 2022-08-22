# coding=utf-8
import unittest
import sys
from webullsdkcore.client import ApiClient
from webullsdkcore.request import ApiRequest

PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestLog(unittest.TestCase):

    def test_set_stream_logger(self):
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk")
        log_format = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'
        client.set_stream_logger(stream=sys.stdout, format_string=log_format)
        request = ApiRequest("/sign", protocol="http")
        request.add_query_param("k1", " zhong国=&")
        request.add_query_param("k2", "v2")
        request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client.get_response(request)

    def test_set_file_logger(self):
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id="hk")
        log_format = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'
        log_file_path = '<log_file_path>'
        client.set_file_logger(path=log_file_path, format_string=log_format)
        request = ApiRequest("/sign", protocol="http")
        request.add_query_param("k1", " zhong国=&")
        request.add_query_param("k2", "v2")
        request.set_endpoint(PRE_OPENAPI_ENDPOINT)
        client.get_response(request)
