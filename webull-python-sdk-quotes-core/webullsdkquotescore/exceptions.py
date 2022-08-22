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

class ConnectException(Exception):
    def __init__(self, rc_code, msg=""):
        Exception.__init__(self)
        self.error_code = rc_code
        self.error_msg = msg

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

    def __str__(self):
        return "rc code: %s, msg: %s" % (self.error_code, self.error_msg)


class ExitedException(ConnectException):
    def __init__(self):
        ConnectException.__init__(
            self, 0, "exited exception which used to stop processing manually")


class LoopException(Exception):
    def __init__(self, loop_code, msg=""):
        Exception.__init__(self)
        self.error_code = loop_code
        self.error_msg = msg

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg

    def __str__(self):
        return "loop code: %s, msg: %s" % (self.error_code, self.error_msg)
