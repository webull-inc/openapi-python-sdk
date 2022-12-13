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


class ExpirationCycle(EasyEnum):
    DAILY = (1, 'day')
    WEEKLY = (2, 'week')
    MONTHLY = (3, 'month')
    QUATERLY = (4, 'season')
    END_OF_MONTH = (5, 'end of month')
    YEARLY = (6, 'year')
