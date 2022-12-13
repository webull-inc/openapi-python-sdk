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

from enum import Enum

class EasyEnum(Enum):
    def __str__(self):
        return self.name
    
    @classmethod
    def from_string(cls, s):
        for item in cls:
            if item.name == s:
                return item
        raise ValueError(cls.__name__ + ' has no value matching ' + s)