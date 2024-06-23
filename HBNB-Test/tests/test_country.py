import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.country import Country

class TestCountry(unittest.TestCase):

    def test_country_creation(self):
        country = Country(name='Tunisia')
        self.assertEqual(country.name, 'Tunisia')
        self.assertIsNotNone(country.country_id)
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)

    def test_to_dict(self):
        country = Country(name='Tunisia')
        country_dict = country.to_dict()
        self.assertEqual(country_dict['name'], 'Tunisia')
        self.assertEqual(country_dict['country_id'], country.country_id)


if __name__ == '__main__':
    unittest.main()
