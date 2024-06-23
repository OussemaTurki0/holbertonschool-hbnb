from datetime import datetime
from models.review import Review
from persistence.ipersistence_manager import IPersistenceManager


class Review_Data(IPersistenceManager):
#empty dictionary to store review objects.
    def __init__(self):
        self.reviews = {}

    def save(self, review):
#Saves a review
        review.created_at = datetime.now()
        review.updated_at = datetime.now()
        self.reviews[review.review_id] = review

    def get(self, review_id):
#bring a review
        return self.reviews.get(review_id)

    def get_all(self):
#bring all reviews
        return list(self.reviews.values())

    def update(self, review_id, new_review_data):
#Updates an existing review
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                setattr(review, key, value)
            review.updated_at = datetime.now()
            self.save(review)
            return True
        return False

    def delete(self, review_id):
#Deletes an existing review
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False
