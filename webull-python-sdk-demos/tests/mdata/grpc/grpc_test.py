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

import sys
import time

from webullsdkmdata.quotes.grpc.market_data import MarketData
from webullsdkmdata.quotes.grpc.instrument import Instrument
from webullsdkquotescore.grpc.grpc_client import GrpcApiClient

your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"
optional_quotes_endpoint = "</optional_quotes_endpoint>"

# 'hk' or 'us'
region_id = '<region_id>'

grpc_client = GrpcApiClient(your_app_key, your_app_secret, region_id, host=optional_quotes_endpoint, port=443,
                            tls_enable=True)

log_format = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'
grpc_client.set_stream_logger(stream=sys.stdout, format_string=log_format)

market_data = MarketData(grpc_client)
instrument = Instrument(grpc_client)
#
if __name__ == "__main__":
    print('get_token request', '*' * 20)
    res = market_data.get_token()
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    token = res.json()['token']
    print("token : ", token)
    print('get_token request end', '*' * 20)

    print('get_history_bar request', '*' * 20)
    res = market_data.get_history_bar('00700', 'HK_STOCK', 'M1')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_history_bar request end', '*' * 20)

    time.sleep(1)
    print('get_quote request', '*' * 20)
    res = market_data.get_quote('00700', 'HK_STOCK')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_quote request end', '*' * 20)

    time.sleep(1)
    print('get_instrument request', '*' * 20)
    res = instrument.get_instrument('F', 'US_STOCK')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_instrument request end', '*' * 20)

    time.sleep(1)
    print('get_tick request', '*' * 20)
    res = market_data.get_tick('00700', 'HK_STOCK')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_tick request end', '*' * 20)

    time.sleep(1)
    print('get_snapshot_quote request', '*' * 20)
    res = market_data.get_snapshot('00700', 'HK_STOCK')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_snapshot_quote request end', '*' * 20)
