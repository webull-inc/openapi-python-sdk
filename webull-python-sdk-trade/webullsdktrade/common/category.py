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


class Category(EasyEnum):
    US_STOCK = (1, 'US STOCK')
    US_OPTION = (2, 'US OPTION')
    HK_STOCK = (3, 'HK STOCK')
    CRYPTO = (4, 'CRYPTO')
    US_ETF = (5, 'US ETF')
    HK_ETF = (6, 'HK ETF')
    CN_STOCK = (7, "CN STOCK")
    NFT = (8, "NFT")
    US_CFDONSTOCK = (9, "US CFDON STOCK")
    JP_STOCK = (10, "JP STOCK")
    JP_ETF = (11, "JP ETF")
