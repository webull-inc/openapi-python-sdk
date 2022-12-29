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

from webullsdkcore.common.easy_enum import EasyEnum


class ExchangeCode(EasyEnum):
    HKG = (1, 'Hong Kong Stock Exchange')
    NAS = (2, 'NASDAQ Capital Market')
    NYSE = (3, 'New York Stock Exchange')
    ASE = (4, 'NYSE MKT')
    PSE = (5, 'NYSE Archipelago Exchange')
    BAT = (6, 'BATS Exchanges')
    NMS = (7, "NASDAQ Global Market")
    NSQ = (8, "NASDAQ Global Select Market")
    OTC = (9, "Over The Counter Bulletin Board")
    PK = (10, "Pink Sheets")
    OPRA = (11, "Option Pricing Reporting Authority")
    CCC = (12, "Cryptocurrency")
    HKW = (13, "Hong Kong Warrant Exchange")
