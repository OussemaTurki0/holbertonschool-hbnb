import unittest
import sys
import os
from models.city import City
from persistence.city_data import City_Data

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCityData(unittest.TestCase):

    def setUp(self):
        self.data = City_Data()

    def test_save_city(self):
        city = City(name='Sousse', country_id='1')
        self.data.save(city)
        self.assertIn(city.city_id, self.data.cities)

    def test_get_city(self):
        city = City(name='Sousse', country_id='1')
        self.data.save(city)
        fetched = self.data.get(city.city_id)
        self.assertEqual(fetched.name, 'Sousse')

    def test_update_city(self):
        city = City(name='Sousse', country_id='1')
        self.data.save(city)
        update_data = {'name': 'Updated City'}
        self.data.update(city.city_id, update_data)
        updated = self.data.get(city.city_id)
        self.assertEqual(updated.name, 'Updated City')

    def test_delete_city(self):
        city = City(name='Sousse', country_id='1')
        self.data.save(city)
        self.data.delete(city.city_id)
        self.assertIsNone(self.data.get(city.city_id))


if __name__ == '__main__':
    unittest.main()