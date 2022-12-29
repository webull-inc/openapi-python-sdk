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
https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/endpoint/local_config_regional_endpoint_resolver.py
which was part of Alibaba Group.
"""

import json
import os
import webullsdkcore
from webullsdkcore.endpoint import EndpointResolver

ENDPOINT_JSON = os.path.join(os.path.dirname(webullsdkcore.__file__), "data", "endpoints.json")


class LocalConfigRegionalEndpointResolver(EndpointResolver):
    def __init__(self, config_json_str=None):
        EndpointResolver.__init__(self)
        if config_json_str:
            obj = json.loads(config_json_str)
        else:
            obj = self._read_from_default_file()
        self._init_config(obj)

    def _init_config(self, obj):
        self._default_region = obj["default_region"]
        self._region_mapping = obj["region_mapping"]

    def _read_from_default_file(self):
        with open(ENDPOINT_JSON) as fp:
            return json.load(fp)

    def resolve(self, request):
        if request.region_id:
            region_code_mapping = self._region_mapping.get(request.region_id)
        else:
            region_code_mapping = self._region_code_mapping.get(self._default_region)
        if region_code_mapping:
            return region_code_mapping.get(request.api_type)
        return None
