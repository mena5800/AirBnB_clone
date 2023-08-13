#!/usr/bin/python3
"""
Unit tests for review
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Tests instances and methods for Review class"""

    new_review = Review()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.new_review)), "<class 'models.review.Review'>")

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.new_review, Review)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.new_review, 'place_id'))
        self.assertTrue(hasattr(self.new_review, 'user_id'))
        self.assertTrue(hasattr(self.new_review, 'text'))
        self.assertTrue(hasattr(self.new_review, 'id'))
        self.assertTrue(hasattr(self.new_review, 'created_at'))
        self.assertTrue(hasattr(self.new_review, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.new_review.place_id, str)
        self.assertIsInstance(self.new_review.user_id, str)
        self.assertIsInstance(self.new_review.text, str)
        self.assertIsInstance(self.new_review.id, str)
        self.assertIsInstance(self.new_review.created_at, datetime.datetime)
        self.assertIsInstance(self.new_review.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()