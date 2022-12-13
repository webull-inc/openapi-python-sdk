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

from webullsdkmdata.quotes.grpc.pb import quote_pb2
from webullsdkmdata.request.grpc.base_request import GRPCBaseRequest


class SubscribeRequest(GRPCBaseRequest):
    def __init__(self, token, symbols, category, types):

        if not isinstance(symbols, str) and not isinstance(types, list):
            raise ValueError("not supported symbols")

        if not isinstance(types, str) and not isinstance(types, list):
            raise ValueError("not supported type")

        request = quote_pb2.SubscribeRequest(
            token=token,
            symbols=symbols if isinstance(symbols, list) else symbols.split(","),
            category=category,
            sub_types=types if isinstance(types, list) else types.split(","),
        )
        GRPCBaseRequest.__init__(self, "/market-data/streaming/subscribe", request, version='v1')
