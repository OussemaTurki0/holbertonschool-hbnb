import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review(user_id="1", place_id="1", text="A review")
        self.assertEqual(review.user_id, "1")
        self.assertEqual(review.place_id, "1")
        self.assertEqual(review.text, "A review")

if __name__ == '__main__':
    unittest.main()
