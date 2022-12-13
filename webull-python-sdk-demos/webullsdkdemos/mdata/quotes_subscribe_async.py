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

# coding=utf-8

import time
from webullsdkmdata.common.category import Category
from webullsdkmdata.common.subscribe_type import SubscribeType
from webullsdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'hk' or 'us'
    region_id = '<region_id>'
    # not necessary in production env
    optional_quotes_grpc_endpoint = "<grpc_api_endpoint>"
    quotes_client = DefaultQuotesClient(
        your_app_key, your_app_secret, region_id, api_endpoint=optional_quotes_grpc_endpoint)
    quotes_client.init_default_settings(["AAPL", "TSLA"], Category.US_STOCK.name, [
        SubscribeType.BASIC_QUOTE.name, SubscribeType.SNAPSHOT.name])


    def my_quotes_message_func(client, topic, quotes):
        print("topic:%s, quotes:%s" % (topic, quotes))


    # set quotes receiving callback func
    quotes_client.on_quotes_message = my_quotes_message_func
    # not necessary in production env
    optional_quotes_host = "<quotes_endpoint>"
    # the async mode, processing in another thread
    quotes_client.connect_and_loop_start(host=optional_quotes_host)
    ticker = 30
    print("will stop processing after %s seconds" % ticker)
    time.sleep(ticker)
    quotes_client.loop_stop()
    print("processing done")
