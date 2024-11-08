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
from webullsdktrade.request.get_trade_instrument_detail_request import TradeInstrumentDetailRequest
from webullsdktrade.request.get_trade_security_detail_request import TradeSecurityDetailRequest
from webullsdktrade.request.get_tradeable_instruments_request import TradeableInstrumentRequest


class TradeInstrument:

    def __init__(self, api_client):
        self.client = api_client

    def get_trade_instrument_detail(self, instrument_id):
        """
        Query the information of traded symbol.

        :param instrument_id: Symbol ID
        """
        instrument_detail_request = TradeInstrumentDetailRequest()
        instrument_detail_request.set_instrument_id(instrument_id)
        response = self.client.get_response(instrument_detail_request)
        return response

    def get_trade_security_detail(self, symbol, market, instrument_super_type, instrument_type, strike_price, init_exp_date):
        """
        Query the information of traded symbol.

        :param symbol: The ticker symbol or code representing a specific financial instrument or security.
        :param market: e.g. US, HK.
        :param instrument_super_type: Asset Class (e.g. EQUITY, OPTION.)
        :param instrument_type: Type of underlying equity，required when querying for options information (e.g., WARRANT, UNITS, ETF, CALL_OPTION, PUT_OPTION).
        :param strike_price: Option Strike Price, required when querying for options information.
        :param init_exp_date: Option Expiration Date, Format: yyyy-MM-dd, required when querying for options information.
        """
        security_detail_request = TradeSecurityDetailRequest()
        security_detail_request.set_symbol(symbol)
        security_detail_request.set_market(market)
        security_detail_request.set_instrument_super_type(instrument_super_type)
        security_detail_request.set_instrument_type(instrument_type)
        security_detail_request.set_strike_price(strike_price)
        security_detail_request.set_init_exp_date(init_exp_date)
        response = self.client.get_response(security_detail_request)
        return response

    def get_tradeable_instruments(self, last_instrument_id=None, page_size=10):
        """
        Only for Webull JP

        Paging query tradable instruments.

        :param last_security_id: Pagination-specific id, if not passed, the first page will be searched by default

        :param page_size: Number of entries per page: default value is 10,
        and the maximum value is 100 with integers being filled.
        """
        tradeable_instruments_request = TradeableInstrumentRequest()
        if last_instrument_id is not None:
            tradeable_instruments_request.set_last_instrument_id(last_instrument_id)
        tradeable_instruments_request.set_page_size(page_size)
        response = self.client.get_response(tradeable_instruments_request)
        return response
