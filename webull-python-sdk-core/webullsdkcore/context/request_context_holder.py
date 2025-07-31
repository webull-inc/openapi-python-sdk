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

import threading

class RequestContextHolder:
    _thread_local = threading.local()

    @classmethod
    def get(cls) -> dict:
        # Initializes the headers dictionary for the current thread.
        if not hasattr(cls._thread_local, 'headers'):
            cls._thread_local.headers = {}
        return cls._thread_local.headers

    @classmethod
    def clear(cls):
        # Delete the current thread's headers field to prevent threads from reusing residual data.
        if hasattr(cls._thread_local, 'headers'):
            del cls._thread_local.headers
