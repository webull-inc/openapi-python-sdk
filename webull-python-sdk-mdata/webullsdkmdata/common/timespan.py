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
class Timespan(EasyEnum):
    M1 = (1, "1 minute")
    M5 = (2, "5 minute")
    M15 = (3, "15 minute")
    M30 = (4, "30 minute")
    M60 = (5, "60 minute")
    M120 = (6, "120 minute")
    M240 = (7, "240 minute")
    D = (8, "1 day")
    W = (9, "1 week")
    M = (10, "1 month")
    Y = (11, "1 year")