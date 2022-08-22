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

# coding=utf-8

from webullsdkcore.common.easy_enum import EasyEnum

class OptionStrategyType(EasyEnum):
    BUY_WRITES = (1, "BUY_WRITES")
    PROTECTIVE_CALLS = (2, "PROTECTIVE_CALLS")
    LONG_STRADDLES = (3, "LONG_STRADDLES")
    LONG_STRANGLES = (4, "LONG_STRANGLES")
    COVERED_PUTS = (5, "COVERED_PUTS")
    PROTECTIVE_PUTS = (6, "PROTECTIVE_PUTS")
    CREDIT_SPREADS = (7, "CREDIT_SPREADS")
    DEBIT_SPREADS = (8, "DEBIT_SPREADS")
    CALENDAR_SPREADS = (9, "CALENDAR_SPREADS")
    LONG_BUTTERFLY = (10, "LONG_BUTTERFLY")
    SHORT_BUTTERFLY = (11, "SHORT_BUTTERFLY")
    LONG_CONDOR = (12, "LONG_CONDOR")
    SHORT_CONDOR = (13, "SHORT_CONDOR")
    COLLAR = (14, "COLLAR")
    LONG_IRON_BUTTERFLY = (15, "LONG_IRON_BUTTERFLY")
    SHORT_IRON_BUTTERFLY = (16, "SHORT_IRON_BUTTERFLY")
    LONG_IRON_CONDOR = (17, "LONG_IRON_CONDOR")
    SHORT_IRON_CONDOR = (18, "SHORT_IRON_CONDOR")

