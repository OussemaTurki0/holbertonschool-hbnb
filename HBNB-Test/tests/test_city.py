import unittest
import sys
import os
from models.city import City

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCity(unittest.TestCase):

    def test_city_creation(self):
        city = City(name='Sousse', country_id='1')
        self.assertEqual(city.name, 'Sousse')
        self.assertIsNotNone(city.city_id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_to_dict(self):
        city = City(name='Sousse', country_id='1')
        city_dict = city.to_dict()
        self.assertEqual(city_dict['name'], 'Sousse')
        self.assertEqual(city_dict['city_id'], city.city_id)


if __name__ == '__main__':
    unittest.main()