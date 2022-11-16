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

import threading
import logging

logger = logging.getLogger(__name__)


class TaskTimer(object):

    def __init__(self, function, delay=10, args=None, kwargs=None):
        self._lock = threading.RLock()
        self._delay = delay
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self._timer: threading.Timer = None

    def run(self):
        if not callable(self._function):
            raise AttributeError()

        with self._lock:
            if self.is_running():
                logger.error("Executing task, please try again later, current thread name:%s", threading.currentThread().name)
                return
            self.start()

    def start(self):
        self._timer = threading.Timer(self._delay, self.hook, self._args, self._kwargs)
        self._timer.start()

    def hook(self, *args, **kwargs):
        self._function(*args, **kwargs)
        self.start()

    def is_running(self):
        return self._timer and self._timer.is_alive()

    def cancel(self):
        with self._lock:
            if self.is_running():
                self._timer.cancel()
                self._timer = None
