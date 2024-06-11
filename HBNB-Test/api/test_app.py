import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Define a test user data
        user_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        # Send a POST request to the '/users' endpoint with the test user data
        response = self.app.post('/users', json=user_data)

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Assert that the response data contains the user data
        self.assertEqual(response.json, user_data)
