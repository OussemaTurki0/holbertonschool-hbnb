import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.review import Review
from models.base_model import BaseModel  # Import BaseModel

class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.review = Review(user_id="test_user", place_id="test_place", text="Great experience!")

    def test_review_initialization(self):
        """Test the initialization of the Review object"""
        self.assertEqual(self.review.user_id, "test_user")
        self.assertEqual(self.review.place_id, "test_place")
        self.assertEqual(self.review.text, "Great experience!")

    def test_to_dict(self):
        """Test the to_dict method of the Review object"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['user_id'], "test_user")
        self.assertEqual(review_dict['place_id'], "test_place")
        self.assertEqual(review_dict['text'], "Great experience!")
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

if __name__ == "__main__":
    unittest.main()
