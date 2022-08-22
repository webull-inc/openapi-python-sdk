# coding=utf-8

import unittest
from webullsdkmdata.quotes.subscribe.basic_result import BasicResult
from webullsdkmdata.quotes.subscribe.message_pb2 import BasicData


class TestBasicResult(unittest.TestCase):
    def test_new_result(self):
        basic = BasicData()
        basic.symbol = 'AAPL'
        basic.instrument_id = "10000001"
        basic.timestamp = "1645096836059"
        result = BasicResult(basic)
        print("result:", result, ",utc time:", result.get_timestamp_as_utc())
