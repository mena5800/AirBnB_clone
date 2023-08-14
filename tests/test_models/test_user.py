#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
import datetime


class UserTests(unittest.TestCase):
    """tests instances and methods from user class"""

    new_user = User()

    def test_class_exists(self):
        """tests class existence"""
        self.assertEqual(str(type(self.new_user)),
                         "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.new_user, User)

    def testHasAttributes(self):
        """test attributes existence"""
        self.assertTrue(hasattr(self.new_user, 'email'))
        self.assertTrue(hasattr(self.new_user, 'password'))
        self.assertTrue(hasattr(self.new_user, 'first_name'))
        self.assertTrue(hasattr(self.new_user, 'last_name'))
        self.assertTrue(hasattr(self.new_user, 'id'))
        self.assertTrue(hasattr(self.new_user, 'created_at'))
        self.assertTrue(hasattr(self.new_user, 'updated_at'))

    def test_types(self):
        """test attribute type"""
        self.assertIsInstance(self.new_user.first_name, str)
        self.assertIsInstance(self.new_user.last_name, str)
        self.assertIsInstance(self.new_user.email, str)
        self.assertIsInstance(self.new_user.password, str)
        self.assertIsInstance(self.new_user.id, str)
        self.assertIsInstance(self.new_user.created_at, datetime.datetime)
        self.assertIsInstance(self.new_user.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
