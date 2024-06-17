import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        # Clear registered_emails set to avoid interference between tests
        User.registered_emails.clear()

    def test_creation(self):
        """Test user creation"""
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.places, [])
        
    def test_id(self):
        """Test ID generation"""
        user1 = User(email="ghof.amemi@gmail.com", first_name="Ghofrane", last_name="Amemi")
        user2 = User(email="someone@example.com", first_name="Someone", last_name="Else")
        self.assertNotEqual(user1.id, user2.id)  # IDs should be unique

    def test_to_dict(self):
        """Test the to_dict method"""
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_duplicate_email(self):
        """Test handling of duplicate emails"""
        User(email="test@example.com", first_name="John", last_name="Doe")
        with self.assertRaises(ValueError):
            User(email="test@example.com", first_name="Jane", last_name="Doe")

if __name__ == "__main__":
    unittest.main()
