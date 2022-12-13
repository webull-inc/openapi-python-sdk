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
from threading import Lock

REQUEST_ERROR = 203

REQUEST_TIMEOUT = 408

GRPC_CONNECT_ERROR = 'grpc_connect_error'


class ExceptionContext(object):

    def __init__(self):
        self._exception_mapping = {}
        self._lock = Lock()

    def get_exception(self):
        if self._exception_mapping:
            return self._exception_mapping[GRPC_CONNECT_ERROR]
        return None

    def set_exception(self, exception):
        with self._lock:
            if exception:
                self._exception_mapping[GRPC_CONNECT_ERROR] = exception
            else:
                self._exception_mapping = {}
