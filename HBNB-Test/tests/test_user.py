import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_unique_id(self):
        user1 = User(email="test1@example.com", first_name="John", last_name="Doe")
        user2 = User(email="test2@example.com", first_name="Jane", last_name="Doe")
        self.assertNotEqual(user1.id, user2.id)

if __name__ == '__main__':
    unittest.main()
