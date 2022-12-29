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

class Order:
    def __init__(self, order):
        self.mpid = order.mpid
        self.size = order.size

    def get_mpid(self):
        return self.mpid

    def get_size(self):
        return self.size

    def __repr__(self):
        return "mpid:%s,size:%s" % (self.mpid, self.size)

    def __str__(self):
        return self.__repr__()
