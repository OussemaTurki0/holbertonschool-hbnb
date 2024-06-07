# tests/test_place.py
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Test City", latitude=0.0, longitude=0.0, host="Test Host", number_of_rooms=1, bathrooms=1, price_per_night=100, max_guests=2)

    def test_place_creation(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.name, "Test Place")
    
if __name__ == '__main__':
    unittest.main()
