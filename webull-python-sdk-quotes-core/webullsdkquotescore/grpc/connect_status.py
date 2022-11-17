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
from threading import RLock


class ConnectStatus(object):
    INIT = 0

    READY = 1

    RUNNING = 2

    RETRY = 4

    CLOSE = 5

    def __init__(self):
        self.status = ConnectStatus.INIT
        self._lock = RLock()

    def set_ready(self):
        with self._lock:
            self.status = ConnectStatus.READY

    def set_running(self):
        with self._lock:
            self.status = ConnectStatus.RUNNING

    def set_retry(self):
        with self._lock:
            self.status = ConnectStatus.RETRY

    def set_close(self):
        with self._lock:
            self.status = ConnectStatus.CLOSE

    def is_close(self):
        return self.status == ConnectStatus.CLOSE

    def is_running(self):
        return self.status == ConnectStatus.RUNNING
