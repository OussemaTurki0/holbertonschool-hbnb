# tests/test_amenity.py
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(name="Wi-Fi")

    def test_amenity_creation(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "Wi-Fi")
    
if __name__ == '__main__':
    unittest.main()
