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

    def testStoreBaseModel1(self):
        """ Test save, reload and update methods """
        self.new_base.my_name = "Nam1"
        self.new_base.save()
        base_dict = self.new_base.to_dict()
        all_objs = storage.all()

        key = base_dict['__class__'] + "." + base_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(base_dict['my_name'], "Nam1")

        create = base_dict['created_at']
        update = base_dict['updated_at']

        self.new_base.my_name = "Nam2"
        self.new_base.save()
        base_dict = self.new_base.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = base_dict['created_at']
        update2 = base_dict['updated_at']

        self.assertEqual(create, create2)
        self.assertNotEqual(update, update2)
        self.assertEqual(base_dict['my_name'], "Nam2")

    def testHasAttributes(self):
        """test attr existence"""
        self.assertEqual(hasattr(FileStorage, '__objects'), True)
        self.assertEqual(hasattr(FileStorage, '__file_path'), True)

    def testsave(self):
        """test JSON existence"""
        self.new_base.save()
        self.assertEqual(storage.all(), storage.__objects)
        self.assertEqual(os.path.exists(storage.__file_path), True)

    def testreload(self):
        """test reload """
        self.new_base.save()
        self.assertEqual(os.path.exists(storage.__file_path), True)
        all_objects = storage.all()
        FileStorage.__objects = {}
        self.assertNotEqual(all_objects, FileStorage.__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(all_objects[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ test save self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ Test 'new' method """
        var1 = self.new_base.to_dict()
        new_key = var1['__class__'] + "." + var1['id']
        storage.save()
        with open("file.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])


if __name__ == '__main__':
    unittest.main()
