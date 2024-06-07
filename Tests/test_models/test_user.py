# tests/test_user.py
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", password="test123")

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "test@example.com")
    
    def test_unique_email(self):
        users = [self.user]
        self.assertFalse(User.is_email_unique("test@example.com", users))
        self.assertTrue(User.is_email_unique("new@example.com", users))

if __name__ == '__main__':
    unittest.main()
