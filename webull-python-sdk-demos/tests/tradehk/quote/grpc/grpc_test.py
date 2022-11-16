import sys
import time

from webullsdkmdata.quotes.grpc.market_data import MarketData
from webullsdkmdata.quotes.grpc.instrument import Instrument
from webullsdkquotescore.grpc.grpc_client import GrpcApiClient

your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"
optional_quotes_endpoint = "</optional_quotes_endpoint>"

# port=9082

grpc_client = GrpcApiClient(your_app_key, your_app_secret, "hk", host=optional_quotes_endpoint, port=443,
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
    res = instrument.get_instrument('00700', 'HK_STOCK')
    print(res.path)
    print(res.request_id)
    print(res.status_code)
    print(res.msg)
    print(res.json())
    print('get_instrument request end', '*' * 20)
