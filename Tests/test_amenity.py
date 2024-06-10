import sys, os
current_path = os.path.abspath(os.path.dirname(__file__))
models_directory = os.path.join(current_path, '..', '..', 'Models')
sys.path.append(models_directory)


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
