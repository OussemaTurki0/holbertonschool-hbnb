import unittest
import sys
import os
from models.review import Review
from persistence.review_data import Review_Data


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestReviewData(unittest.TestCase):

    def setUp(self):
        self.data = Review_Data()

    def test_save_review(self):
        review = Review(user_id='1', place_id='1', rating=5,
                        comment='Great place!')
        self.data.save(review)
        self.assertIn(review.review_id, self.data.reviews)

    def test_get_review(self):
        review = Review(user_id='1', place_id='1', rating=5,
                        comment='Great place!')
        self.data.save(review)
        fetched = self.data.get(review.review_id)
        self.assertEqual(fetched.comment, 'Great place!')

    def test_update_review(self):
        review = Review(user_id='1', place_id='1', rating=5,
                        comment='Great place!')
        self.data.save(review)
        update_data = {'comment': 'Updated comment'}
        self.data.update(review.review_id, update_data)
        updated = self.data.get(review.review_id)
        self.assertEqual(updated.comment, 'Updated comment')

    def test_delete_review(self):
        review = Review(user_id='1', place_id='1', rating=5,
                        comment='Great place!')
        self.data.save(review)
        self.data.delete(review.review_id)
        self.assertIsNone(self.data.get(review.review_id))


if __name__ == '__main__':
    unittest.main()