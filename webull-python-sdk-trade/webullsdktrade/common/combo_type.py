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


class ComboType(EasyEnum):
    MASTER = (1, 'Master order')
    STOP_LOSS_PROFIT = (2, 'Stop loss Profit')
    STOP_LOSS = (3, 'Stop loss')
    STOP_PROFIT = (4, 'Stop profit')
    OTO = (5, 'One trigger others')
    OCO = (6, 'One cancel others')
    OTOCO = (7, "OTO + OCO")
    NORMAL = (8, "Normal order")
    BROKEN = (9, "Broken order")
    BROKEN_INT = (10, "Broken order integer part")
    BROKEN_DEC = (11, "Broken order fractional part")
