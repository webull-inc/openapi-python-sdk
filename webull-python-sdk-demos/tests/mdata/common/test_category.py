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