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
from webullsdktrade.request.get_trade_calendar_request import TradeCalendarRequest


class TradeCalendar:

    def __init__(self, api_client):
        self.client = api_client

    def get_trade_calendar(self, market, start, end):
        """
        Get the trading calendar for the specified market.
        Trading days are obtained by excluding weekends and holidays, and the dates of temporary market closures are
        not excluded.

        :param market: Markets, enumeration
        :param start: Start date
        :param end: End date
        """
        trade_calendar_request = TradeCalendarRequest()
        trade_calendar_request.set_market(market)
        trade_calendar_request.set_start(start)
        trade_calendar_request.set_end(end)
        response = self.client.get_response(trade_calendar_request)
        return response
