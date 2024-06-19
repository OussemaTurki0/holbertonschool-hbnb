import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.place = Place(name="Cozy Cabin", description="A quaint cabin in the woods",
                           city_id="test_city", user_id="test_user")

    def test_place_initialization(self):
        """Test the initialization of the Place object"""
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.description, "A quaint cabin in the woods")
        self.assertEqual(self.place.city_id, "test_city")
        self.assertEqual(self.place.user_id, "test_user")
        self.assertEqual(self.place.reviews, [])  # Ensure reviews list starts empty
        self.assertEqual(self.place.amenities, [])  # Ensure amenities list starts empty

    def test_add_amenity(self):
        """Test adding amenities to a Place"""
        amenity1 = Amenity(name="WiFi")
        amenity2 = Amenity(name="Hot Tub")

        self.place.add_amenity(amenity1)
        self.assertIn(amenity1.id, self.place.amenities)
        self.assertEqual(len(self.place.amenities), 1)

        # Adding the same amenity again should not duplicate it
        self.place.add_amenity(amenity1)
        self.assertEqual(len(self.place.amenities), 1)

        self.place.add_amenity(amenity2)
        self.assertIn(amenity2.id, self.place.amenities)
        self.assertEqual(len(self.place.amenities), 2)

if __name__ == "__main__":
    unittest.main()