# tests/test_review.py
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review(user="Test User", place="Test Place", rating=5, comment="Great place!")

    def test_review_creation(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.rating, 5)
    
if __name__ == '__main__':
    unittest.main()
