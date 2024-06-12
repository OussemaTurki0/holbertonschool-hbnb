import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place(name="Test Place", description="A test place", city_id="1", user_id="1")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "A test place")
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "1")

if __name__ == '__main__':
    unittest.main()
