import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from persistence.user_data import User_Data

class TestUserData(unittest.TestCase):

    def setUp(self):
        self.data = User_Data()

    def test_save_user(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        self.data.save(user)
        self.assertIn(user.user_id, self.data.users)

    def test_get_user(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        self.data.save(user)
        fetched = self.data.get(user.user_id)
        self.assertEqual(fetched.username, 'testuser')

    def test_update_user(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        self.data.save(user)
        update_data = {'username': 'updateduser'}
        self.data.update(user.user_id, update_data)
        updated = self.data.get(user.user_id)
        self.assertEqual(updated.username, 'updateduser')

    def test_delete_user(self):
        user = User(username='testuser', email='testuser@example.com',
                    password='password')
        self.data.save(user)
        self.data.delete(user.user_id)
        self.assertIsNone(self.data.get(user.user_id))


if __name__ == '__main__':
    unittest.main()