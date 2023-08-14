#!/usr/bin/python3
"""
Unit tests for amenity
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances and methods in amenity class"""

    new_place = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.new_place)),
                         "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.new_place, Place)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.new_place, 'city_id'))
        self.assertTrue(hasattr(self.new_place, 'user_id'))
        self.assertTrue(hasattr(self.new_place, 'name'))
        self.assertTrue(hasattr(self.new_place, 'description'))
        self.assertTrue(hasattr(self.new_place, 'number_rooms'))
        self.assertTrue(hasattr(self.new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.new_place, 'max_guest'))
        self.assertTrue(hasattr(self.new_place, 'price_by_night'))
        self.assertTrue(hasattr(self.new_place, 'latitude'))
        self.assertTrue(hasattr(self.new_place, 'longitude'))
        self.assertTrue(hasattr(self.new_place, 'amenity_ids'))
        self.assertTrue(hasattr(self.new_place, 'id'))
        self.assertTrue(hasattr(self.new_place, 'created_at'))
        self.assertTrue(hasattr(self.new_place, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.new_place.city_id, str)
        self.assertIsInstance(self.new_place.user_id, str)
        self.assertIsInstance(self.new_place.name, str)
        self.assertIsInstance(self.new_place.description, str)
        self.assertIsInstance(self.new_place.number_rooms, int)
        self.assertIsInstance(self.new_place.number_bathrooms, int)
        self.assertIsInstance(self.new_place.max_guest, int)
        self.assertIsInstance(self.new_place.price_by_night, int)
        self.assertIsInstance(self.new_place.latitude, float)
        self.assertIsInstance(self.new_place.longitude, float)
        self.assertIsInstance(self.new_place.amenity_ids, list)
        self.assertIsInstance(self.new_place.id, str)
        self.assertIsInstance(self.new_place.created_at, datetime.datetime)
        self.assertIsInstance(self.new_place.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
