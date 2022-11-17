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

from concurrent.futures import Future

import webullsdkcore.utils.common as core_common
from webullsdkquotescore.grpc.pb import gateway_pb2 as pb


class Msg():

    def __init__(self, msg_type, path=None, payload=None):
        self._msg_type = msg_type
        self._payload = payload
        self._path = path
        self._future = None
        if self._msg_type == pb.Payload:
            self._future = Future()
        self._request_id = core_common.get_uuid()

    def get_future(self):
        return self._future

    def get_msg_type(self):
        return self._msg_type

    def get_payload(self):
        return self._payload

    def get_path(self):
        return self._path

    def get_request_id(self):
        return self._request_id
