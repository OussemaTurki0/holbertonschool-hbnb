import os
import sys
import unittest

# Add the parent directory to the sys.path to import modules correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Amenity model
from models.amenity import Amenity
from models.base_model import BaseModel  # Import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity(name="Swimming Pool")

    def test_amenity_initialization(self):
        """Test the initialization of the Amenity object"""
        self.assertEqual(self.amenity.name, "Swimming Pool")
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIn('id', self.amenity.to_dict())
        self.assertIn('created_at', self.amenity.to_dict())
        self.assertIn('updated_at', self.amenity.to_dict())

    def test_amenity_to_dict(self):
        """Test the to_dict method of the Amenity object"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Swimming Pool")
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

if __name__ == "__main__":
    unittest.main()
