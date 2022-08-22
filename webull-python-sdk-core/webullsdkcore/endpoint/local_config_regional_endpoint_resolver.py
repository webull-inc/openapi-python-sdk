# Copyright 1999-2015 Alibaba Group Holding Ltd.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8

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
        self._region_ids = obj["regions"]
        self._default_region = obj["default_region"]
        self._region_code_mapping = obj["region_code_mapping"]
        self._endpoint_pattern = obj["regional_endpoint_pattern"]

    def _read_from_default_file(self):
        with open(ENDPOINT_JSON) as fp:
            return json.load(fp)
    
    def resolve(self, request):
        pattern = self._endpoint_pattern.get(request.api_type)
        if pattern is not None:
            if request.region_id:
                region_holder_val = self._region_code_mapping.get(request.region_id)
            else:
                region_holder_val = self._region_code_mapping.get(self._default_region)
            if region_holder_val is not None:
                return pattern.replace("[Region]", region_holder_val)
        return None