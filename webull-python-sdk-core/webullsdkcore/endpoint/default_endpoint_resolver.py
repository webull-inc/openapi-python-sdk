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
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

"""
This file borrowed some of its methods from a  modified fork of the
https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/endpoint/default_endpoint_resolver.py
which was part of Alibaba Group.
"""

from webullsdkcore.endpoint import EndpointResolver
from webullsdkcore.endpoint.chained_endpoint_resolver import ChainedEndpointResolver
from webullsdkcore.endpoint.local_config_regional_endpoint_resolver import LocalConfigRegionalEndpointResolver
from webullsdkcore.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver

class DefaultEndpointResolver(EndpointResolver):
    def __init__(self, customer_type, user_config=None):
        self._customer_type = customer_type
        self._user_customized_endpoint_resolver = UserCustomizedEndpointResolver()
        endpoint_resolvers = [
            self._user_customized_endpoint_resolver,
            LocalConfigRegionalEndpointResolver(user_config, customer_type=self._customer_type)
        ] 
        self._resolver = ChainedEndpointResolver(endpoint_resolvers)

    def resolve(self, request):
        return self._resolver.resolve(request)

    def put_endpoint_entry(self, region_id, api_type, endpoint):
        self._user_customized_endpoint_resolver.put_endpoint_entry(region_id, api_type, endpoint)