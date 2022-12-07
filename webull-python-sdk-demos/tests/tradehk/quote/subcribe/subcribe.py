import logging
import unittest

from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"
optional_quotes_endpoint = "</optional_quotes_endpoint>"

class TestDefaultQuotesClient(unittest.TestCase):

    def test_default_quotes_client(self):
        def pt_logs(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        def on_quotes_message(client, userdata, message):
            print("Received message userdata: %s,%s'" % (userdata, message))

        client = DefaultQuotesClient(your_app_key, your_app_secret, 'hk', optional_quotes_endpoint)
        client.init_default_settings('AAPL', Category.US_STOCK.name, SubscribeType.SNAPSHOT.name)
        # client.on_log = pt_logs
        client.on_quotes_message = on_quotes_message
        client.connect_and_loop_forever()
