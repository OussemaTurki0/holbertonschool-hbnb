import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.user = User(email="test@example.com", first_name="John", last_name="Doe")
    
    def test_user_initialization(self):
        """Test the initialization of the User object"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertIsInstance(self.user, BaseModel)
        self.assertEqual(self.user.places, [])

    def test_user_to_dict(self):
        """Test the to_dict method of the User object"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

if __name__ == "__main__":
    unittest.main()
