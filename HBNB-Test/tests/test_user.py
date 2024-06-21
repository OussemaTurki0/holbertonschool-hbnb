import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import bcrypt
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        # Clear registered_emails set to avoid interference between tests
        User.registered_emails.clear()

    def test_creation(self):
        """Test user creation"""
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password123")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertTrue(bcrypt.checkpw("password123".encode('utf-8'), user.password.encode('utf-8')))
        self.assertEqual(user.places, [])
        
    def test_id(self):
        """Test ID generation"""
        user1 = User(email="ghof.amemi@gmail.com", first_name="Ghofrane", last_name="Amemi", password="password123")
        user2 = User(email="someone@example.com", first_name="Someone", last_name="Else", password="password123")
        self.assertNotEqual(user1.id, user2.id)  # IDs should be unique

    def test_to_dict(self):
        """Test the to_dict method"""
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password123")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_duplicate_email(self):
        """Test handling of duplicate emails"""
        User(email="test@example.com", first_name="John", last_name="Doe", password="password123")
        with self.assertRaises(ValueError):
            User(email="test@example.com", first_name="Jane", last_name="Doe", password="password123")

    def test_password_hashing(self):
        """Test that the password is hashed"""
        password = "securepassword"
        user = User(email="hashing@test.com", first_name="Hash", last_name="Test", password=password)
        self.assertNotEqual(user.password, password)  # The stored password should not be the plain text password
        self.assertTrue(bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')))

    def test_password_verification(self):
        """Test the verify_password method"""
        password = "anothersecurepassword"
        user = User(email="verify@test.com", first_name="Verify", last_name="Test", password=password)
        self.assertTrue(user.verify_password(password))
        self.assertFalse(user.verify_password("wrongpassword"))

if __name__ == "__main__":
    unittest.main()
