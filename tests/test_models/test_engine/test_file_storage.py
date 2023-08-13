#!/usr/bin/python3
""" Tests for File Storage module """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json

class FileStorageTests(unittest.TestCase):
    """test for file storage class"""
    new_base = BaseModel()

    def testClassInstance(self):
        """test instance"""
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload methods """
        self.new_base.full_name = "Base 1"
        self.new_base.save()
        base_dict = self.new_base.to_dict()
        all_objects = storage.all()

        key = base_dict['__class__'] + "." + base_dict['id']
        self.assertEqual(key in all_objects, True)

    def testHasAttributes(self):
        """test attr existence"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)

    def testsave(self):
        """test JSON existence"""
        self.new_base.save()
        self.assertEqual(storage.all(), storage._FileStorage__objects)
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)


if __name__ == '__main__':
    unittest.main()