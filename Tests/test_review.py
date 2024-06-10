import sys, os
current_path = os.path.abspath(os.path.dirname(__file__))
models_directory = os.path.join(current_path, '..', '..', 'Models')
sys.path.append(models_directory)


import unittest
from models.review import Review
from models.place import Place
from models.user import User
from models.city import City
from models.country import Country

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User("reviewer@email.com", "Reviewer", "Name")
        self.country = Country("USA")
        self.city = City("San Francisco", self.country)
        self.place = Place("Test Place", "Description", "Address", self.city, 37.7749, 122.4194, self.user, 1, 1, 100, 2)

    def test_create_review_with_valid_attributes(self):
        review = Review(self.place, self.user, 5, "Great place!")
        self.assertEqual(review.rating, 5)

    def test_invalid_rating_raises_error(self):
        with self.assertRaises(ValueError):
            Review(self.place, self.user, 6, "Great place!")

if __name__ == "__main__":
    unittest.main()
