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

from webullsdkcore.request import ApiRequest

class UnsubcribeRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/market-data/streaming/unsubscribe", version='v1', body_params={})

    def set_token(self, token):
        self.add_body_params("token", token)

    def set_symbols(self, symbols):
        if isinstance(symbols, str):
            self.add_body_params("symbols", symbols.split(","))
            return
        elif isinstance(symbols, list):
            self.add_body_params("symbols", symbols)
            return
        raise ValueError("not supported type")

    def set_category(self, category):
        self.add_body_params("category", category)

    def set_sub_types(self, types):
        if isinstance(types, str):
            self.add_body_params("sub_types", types.split(","))
            return
        elif isinstance(types, list):
            self.add_body_params("sub_types", types)
            return
        raise ValueError("not supported type")

    def set_unsubscribe_all(self, is_all):
        is_all = "true" if is_all else "false"
        self.add_body_params("unsubscribe_all", is_all)