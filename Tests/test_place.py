import sys, os
current_path = os.path.abspath(os.path.dirname(__file__))
models_directory = os.path.join(current_path, '..', '..', 'Models')
sys.path.append(models_directory)


import unittest
from models.place import Place
from models.user import User
from models.city import City
from models.country import Country

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User("host@email.com", "Host", "Name")
        self.country = Country("Tunisia")
        self.city = City("Sidi Bou Said", self.country)

    def test_create_place_with_valid_attributes(self):
        place = Place("Test Place", "Description", "Address", self.city, 37.7749, 122.4194, self.user, 1, 1, 100, 2)
        self.assertEqual(place.name, "Test Place")

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Place("Invalid Price", "Description", "Address", self.city, 37.7749, 122.4194, self.user, 1, 1, -100, 2)

if __name__ == "__main__":
    unittest.main()
