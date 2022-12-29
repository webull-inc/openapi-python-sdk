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

import unittest
from webullsdkcore.utils import common
from webullsdkmdata.common.category import Category

class TestCategory(unittest.TestCase):
    def test_access(self):
        self.assertNotEqual(Category.US_STOCK, "US_STOCK") 
        self.assertEqual(Category.US_STOCK.name, "US_STOCK")
        self.assertEqual(Category.US_STOCK, Category.from_string("US_STOCK"))
        try:
            Category.from_string("Unknown Category")
        except ValueError as ve:
            print(ve)