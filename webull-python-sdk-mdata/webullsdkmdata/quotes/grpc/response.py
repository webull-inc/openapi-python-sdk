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
import json
from google.protobuf import json_format
from webullsdkmdata.quotes.grpc.response_code import ResponseCode


class Response(object):

    def __init__(self, result, data_obj):
        self.status_code = ResponseCode.OK if ResponseCode.SUCCEEDED == result.code else result.code
        self.msg = result.msg
        self.request_id = result.requestId
        self.path = result.path
        self._payload = None
        if data_obj and result.payload:
            data_obj.ParseFromString(result.payload)
            self._payload = data_obj
        if self.status_code != ResponseCode.OK:
            raise RuntimeError(self.status_code, self.msg)

    def json(self):
        if self._payload:
            return json.loads(json_format.MessageToJson(self._payload))
