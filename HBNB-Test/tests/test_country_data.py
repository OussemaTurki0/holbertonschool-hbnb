import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.country import Country
from persistence.country_data import Country_Data


class TestCountryData(unittest.TestCase):

    def setUp(self):
        self.data = Country_Data()

    def test_save_country(self):
        country = Country(name='Tunisia')
        self.data.save(country)
        self.assertIn(country.country_id, self.data.countries)

    def test_get_country(self):
        country = Country(name='Tunisia')
        self.data.save(country)
        fetched = self.data.get(country.country_id)
        self.assertEqual(fetched.name, 'Tunisia')

    def test_update_country(self):
        country = Country(name='Tunisia')
        self.data.save(country)
        update_data = {'name': 'Updated Country'}
        self.data.update(country.country_id, update_data)
        updated = self.data.get(country.country_id)
        self.assertEqual(updated.name, 'Updated Country')

    def test_delete_country(self):
        country = Country(name='Tunisia')
        self.data.save(country)
        self.data.delete(country.country_id)
        self.assertIsNone(self.data.get(country.country_id))


if __name__ == '__main__':
    unittest.main()