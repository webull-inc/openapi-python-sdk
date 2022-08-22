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

from webullsdkcore.endpoint import EndpointResolver
        
class UserCustomizedEndpointResolver(EndpointResolver):
    def __init__(self):
        EndpointResolver.__init__(self)
        self._endpoint_entry_map = {}
        
    def put_endpoint_entry(self, region_id, api_type, endpoint):
        entry_key = str(region_id) + api_type
        self._endpoint_entry_map[entry_key] = endpoint
    
    def resolve(self, request):
        key = str(request.region_id) + request.api_type
        return self._endpoint_entry_map.get(key)