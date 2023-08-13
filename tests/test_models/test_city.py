#!/usr/bin/python3
"""
tests for city class
"""
import unittest
from models.city import City
import datetime

class CityTests(unittest.TestCase):
    """Test instances and methods from city class"""
    new_city = City()

    def test_class(self):
        """tests class existence"""
        self.assertEqual(str(type(self.new_city)), "<class 'models.city.City'>")

    def test_city_inheritance(self):
        """tests if city is a subclass of BaseModel"""
        self.assertTrue(self.new_city, City)

    def testHasAttributes(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.new_city, 'state_id'))
        self.assertTrue(hasattr(self.new_city, 'name'))
        self.assertTrue(hasattr(self.new_city, 'id'))
        self.assertTrue(hasattr(self.new_city, 'created_at'))
        self.assertTrue(hasattr(self.new_city, 'updated_at'))

    def test_types(self):
        """tests attribute type"""
        self.assertIsInstance(self.new_city.state_id, str)
        self.assertIsInstance(self.new_city.name, str)
        self.assertIsInstance(self.new_city.id, str)
        self.assertIsInstance(self.new_city.created_at, datetime.datetime)
        self.assertIsInstance(self.new_city.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()