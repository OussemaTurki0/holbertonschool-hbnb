import os
import sys
import unittest
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.city import City
from models.country import Country
from models.place import Place  # Adjust this based on your project structure

class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.city = City(name="TestCity")
        self.country = Country(name="TestCountry")
        self.place = Place(name="TestPlace", description="A place in the city",
                           city_id=None, user_id="test_user")

    def test_city_initialization(self):
        """Test the initialization of the City object"""
        self.assertEqual(self.city.name, "TestCity")
        self.assertIsNone(self.city.country)
        self.assertEqual(self.city.places, [])

    def test_add_place_to_city(self):
        """Test adding a place to a City"""
        self.city.add_place(self.place)
        self.assertIn(self.place, self.city.places)
        self.assertEqual(self.place.city_id, self.city.id)

    def test_set_country(self):
        """Test setting the country of a City"""
        self.city.set_country(self.country)
        self.assertEqual(self.city.country, self.country)
        self.assertIn(self.city, self.country.cities)

    def test_to_dict_method(self):
        """Test the to_dict method of the City class"""
        self.city.set_country(self.country)
        self.city.add_place(self.place)
        city_dict = self.city.to_dict()

        self.assertEqual(city_dict['name'], "TestCity")
        self.assertEqual(city_dict['country']['name'], "TestCountry")
        self.assertEqual(len(city_dict['places']), 1)
        self.assertEqual(city_dict['places'][0]['name'], "TestPlace")

if __name__ == "__main__":
    unittest.main()
