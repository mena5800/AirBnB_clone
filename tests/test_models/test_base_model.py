#!/usr/bin/python3
"""Class TestBaseModel for testing BaseModel class"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Tests"""

    new_base = BaseModel()

    def testBaseModel(self):
        """test attributes of a base model instance"""
        self.new_base.name = "alx"
        self.new_base.my_number = 2
        self.new_base.save()
        new_base_json = self.new_base.to_dict()

        self.assertEqual(self.new_base.name, new_base_json['name'])
        self.assertEqual(self.new_base.my_number, new_base_json['my_number'])
        self.assertEqual('BaseModel', new_base_json['__class__'])
        self.assertEqual(self.new_base.id, new_base_json['id'])

    def testSave(self):
        """checks if save correctly updates the instance attr updated_at"""
        self.new_base.first_name = "John"
        self.new_base.save()

        self.assertIsInstance(self.new_base.id, str)
        self.assertIsInstance(self.new_base.created_at, datetime.datetime)
        self.assertIsInstance(self.new_base.updated_at, datetime.datetime)

        dict_1 = self.new_base.to_dict()

        self.new_base.first_name = "Doe"
        self.new_base.save()
        dict_2 = self.new_base.to_dict()

        self.assertEqual(dict_1['created_at'], dict_2['created_at'])
        self.assertNotEqual(dict_1['updated_at'], dict_2['updated_at'])

if __name__ == '__main__':
    unittest.main()