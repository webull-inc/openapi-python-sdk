# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import socks
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

optional_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
optional_quotes_grpc_endpoint = "<quotes_grpc_endpoint>"
proxy_host = "127.0.0.1"
proxy_port = 9080

# 'hk' or 'us'
region_id = '<region_id>'


class TestDefaultQuotesClient(unittest.TestCase):

    def test_default_quotes_client(self):
        def pt_logs(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        def on_message(client, userdata, message):
            print("Received message '" + str(message.payload) + "' on topic '"
                  + message.topic + "' with QoS " + str(message.qos))

        client = DefaultQuotesClient(your_app_key, your_app_secret, region_id,
                                     api_endpoint=optional_quotes_grpc_endpoint)
        client.proxy_set(proxy_type=socks.SOCKS5, proxy_addr=proxy_host, proxy_port=proxy_port)
        client.init_default_settings('00700', Category.HK_STOCK.name, SubscribeType.SNAPSHOT.name)
        client.on_log = pt_logs
        client.on_message = on_message
        client.connect_and_loop_forever()
