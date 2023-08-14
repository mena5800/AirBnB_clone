#!/usr/bin/python3
"""
Unittest for state
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Tests instances and methods in State class """

    new_state = State()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.new_state)),
                         "<class 'models.state.State'>")

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.new_state, State)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.new_state, 'name'))
        self.assertTrue(hasattr(self.new_state, 'id'))
        self.assertTrue(hasattr(self.new_state, 'created_at'))
        self.assertTrue(hasattr(self.new_state, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.new_state.name, str)
        self.assertIsInstance(self.new_state.id, str)
        self.assertIsInstance(self.new_state.created_at, datetime.datetime)
        self.assertIsInstance(self.new_state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
