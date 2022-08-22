# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from webullsdktradeus.common.entrust_type import OrderEntrustType
from webullsdktradeus.common.order_params_exception import OrderParamsException
from webullsdktradeus.common.order_side import OrderSide
from webullsdktradeus.common.order_tif import OrderTIF
from webullsdktradeus.common.order_type import OrderType
from webullsdktradeus.common.trailing_type import TrailingType


class StockOrder:
    def __init__(self, client_order_id, instrument_id, side, tif, order_type, entrust_type, extended_hours_trading=False,
                 limit_price=None, stop_price=None, trailing_type=None, trailing_stop_step=None, qty=None, amount=None):
        self.client_order_id = client_order_id
        self.instrument_id = instrument_id
        self.side = side
        self.tif = tif
        self.order_type = order_type
        self.entrust_type = entrust_type
        self.extended_hours_trading = extended_hours_trading
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.trailing_type = trailing_type
        self.trailing_stop_step = trailing_stop_step
        self.qty = qty
        self.amount = amount
        self._verify_stock_order_params()

    def _verify_stock_order_params(self):
        # 1 judge entrust type
        if self.entrust_type == OrderEntrustType.QTY.name:
            if self.qty is None:
                raise OrderParamsException("'qty' is required when 'entrust_type' is 'QTY'. ")
        elif self.entrust_type == OrderEntrustType.AMOUNT.name:
            if self.amount is None:
                raise OrderParamsException("'amount' is required when 'entrust_type' is 'AMOUNT'. ")
        else:
            raise OrderParamsException("please pass 'entrust_type' according to the enumeration format")
        # 2  judge order type
        if self.order_type == OrderType.MARKET.name:
            if self.limit_price is not None:
                raise OrderParamsException("no need to pass in 'limit_price' parameter")
            elif self.stop_price is not None:
                raise OrderParamsException("no need to pass in 'stop_price' parameter")
            elif self.trailing_type is not None:
                raise OrderParamsException("no need to pass in 'trailing_type' parameter")
            elif self.trailing_stop_step is not None:
                raise OrderParamsException("no need to pass in 'trailing_stop_step' parameter")
        elif self.order_type == OrderType.LIMIT.name:
            if self.limit_price is None:
                raise OrderParamsException("'limit_price' is required when 'order_type' is 'LIMIT'. ")
            elif self.stop_price is not None:
                raise OrderParamsException("no need to pass in 'stop_price' parameter")
            elif self.trailing_type is not None:
                raise OrderParamsException("no need to pass in 'trailing_type' parameter")
            elif self.trailing_stop_step is not None:
                raise OrderParamsException("no need to pass in 'trailing_stop_step' parameter")
        elif self.order_type == OrderType.STOP_LOSS.name:
            if self.stop_price is None:
                raise OrderParamsException("'stop_price' is required when 'order_type' is 'STOP_LOSS'. ")
            elif self.limit_price is not None:
                raise OrderParamsException("no need to pass in 'limit_price' parameter")
            elif self.trailing_type is not None:
                raise OrderParamsException("no need to pass in 'trailing_type' parameter")
            elif self.trailing_stop_step is not None:
                raise OrderParamsException("no need to pass in 'trailing_stop_step' parameter")
        elif self.order_type == OrderType.STOP_LOSS_LIMIT.name:
            if self.limit_price is None or self.stop_price is None:
                raise OrderParamsException("'limit_price' and 'stop_price' are required when 'order_type' is 'STOP_LOSS_LIMIT'. ")
            elif self.trailing_type is not None:
                raise OrderParamsException("no need to pass in 'trailing_type' parameter")
            elif self.trailing_stop_step is not None:
                raise OrderParamsException("no need to pass in 'trailing_stop_step' parameter")
        elif self.order_type == OrderType.TRAILING_STOP_LOSS.name:
            if self.trailing_type is None or self.trailing_stop_step is None:
                raise OrderParamsException("'trailing_type' and 'trailing_stop_step' are required when 'order_type' is 'TRAILING_STOP_LOSS'. ")
            elif self.limit_price is not None:
                raise OrderParamsException("no need to pass in 'limit_price' parameter")
            elif self.stop_price is not None:
                raise OrderParamsException("no need to pass in 'stop_price' parameter")
            elif self.trailing_type not in (TrailingType.AMOUNT.name, TrailingType.PERCENTAGE.name):
                raise OrderParamsException("please pass 'trailing_type' according to the enumeration format")
        # 3 judge tif of stock order, only support GTC\ DAY
        if self.tif not in (OrderTIF.GTC.name, OrderTIF.DAY.name):
            raise OrderParamsException("please pass 'tif' according to the enumeration format and only supports 'GTC'&'DAY'")

    def get_stock_order_params(self):
        return {k: v for (k, v) in self.__dict__.items() if v is not None}


class OptionOrder:
    def __init__(self, client_order_id, side, tif, order_type, option_strategy,
                 limit_price=None, stop_price=None, qty=None, amount=None,
                 instrument_id=None, legs=None):
        self.client_order_id = client_order_id
        self.side = side
        self.tif = tif
        self.order_type = order_type
        self.option_strategy = option_strategy
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.qty = qty
        self.amount = amount
        self.instrument_id = instrument_id
        self.legs = [] if legs is None else legs
        self._verify_option_params()

    def _verify_option_params(self):
        if self.side not in (OrderSide.SELL.name, OrderSide.BUY.name):
            raise OrderParamsException("please pass 'side' according to the enumeration format and only supports 'SELL'&'BUY'")
        if self.tif not in (OrderTIF.GTC.name, OrderTIF.DAY.name):
            raise OrderParamsException("please pass 'tif' according to the enumeration format and only supports 'GTC'&'DAY'")
        if self.order_type == OrderType.LIMIT.name:
            if self.limit_price is None:
                raise OrderParamsException("'limit_price' is required when 'order_type' is 'LIMIT'. ")
            elif self.stop_price is not None:
                raise OrderParamsException("no need to pass in 'stop_price' parameter")
        elif self.order_type == OrderType.STOP_LOSS_LIMIT.name:
            if self.limit_price is None or self.stop_price is None:
                raise OrderParamsException("'limit_price' and 'stop_price' are required when 'order_type' is 'STOP_LOSS_LIMIT'. ")

    def append_leg(self, instrument_type, instrument_id, side, qty):
        self.legs.append(
            {"instrument_type": instrument_type,
             "instrument_id": instrument_id,
             "side": side,
             "qty": qty})

    def set_instrument_id(self, instrument_id):
        self.instrument_id = instrument_id

    def get_option_order_params(self):
        if len(self.legs) != 0:
            return {k: v for (k, v) in self.__dict__.items() if v is not None}
        return {k: v for (k, v) in self.__dict__.items() if v is not None and k != "legs"}


class CryptoOrder:
    def __init__(self, client_order_id, instrument_id, side, tif, order_type, entrust_type,
                 limit_price=None, qty=None, amount=None):
        self.client_order_id = client_order_id
        self.instrument_id = instrument_id
        self.side = side
        self.tif = tif
        self.order_type = order_type
        self.entrust_type = entrust_type
        self.limit_price = limit_price
        self.qty = qty
        self.amount = amount
        self._verify_stock_order_params()

    def _verify_stock_order_params(self):
        # 1 judge entrust type
        if self.entrust_type == OrderEntrustType.QTY.name:
            if self.qty is None:
                raise OrderParamsException("'qty' is required when 'entrust_type' is 'QTY'. ")
        elif self.entrust_type == OrderEntrustType.AMOUNT.name:
            if self.amount is None:
                raise OrderParamsException("'amount' is required when 'entrust_type' is 'AMOUNT'. ")
        else:
            raise OrderParamsException("please pass 'entrust_type' according to the enumeration format")
        # 2 judge order type
        if self.order_type == OrderType.MARKET.name:
            if self.limit_price is not None:
                raise OrderParamsException("no need to pass in 'limit_price' parameter")
        elif self.order_type == OrderType.LIMIT.name:
            if self.limit_price is None:
                raise OrderParamsException("'limit_price' is required when 'order_type' is 'LIMIT'. ")
        else:
            raise OrderParamsException("please pass 'order_type' according to the enumeration format and only support 'MARKET'&'LIMIT'. ")
        # 3 judge tif of cryptoOrder, only support GTC\ DAY
        if self.tif not in (OrderTIF.IOC.name, OrderTIF.DAY.name):
            raise OrderParamsException("please pass 'tif' according to the enumeration format and only supports 'IOC'&'DAY'")

    def get_crypto_order_params(self):
        return {k: v for (k, v) in self.__dict__.items() if v is not None}

