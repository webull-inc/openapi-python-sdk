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
class ClientException(Exception):
    def __init__(self, code, msg=""):
        Exception.__init__(self)
        self.error_code = code
        self.error_msg = msg
        
    def __str__(self):
        return "%s %s" % (self.error_code, self.error_msg)

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

class ServerException(Exception):
    def __init__(self, code, msg="", http_status = None, request_id = None):
        Exception.__init__(self)
        self.error_code = code
        self.error_msg = msg
        self.http_status = http_status
        self.request_id = request_id

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

    def get_http_status(self):
        return self.http_status

    def get_request_id(self):
        return self.request_id

    def __str__(self):
        return "HTTP Status: %s, Code: %s, Msg: %s, RequestID: %s" \
    % (str(self.http_status), self.error_code, self.error_msg, self.request_id)