import os
import sys
import unittest

# Add the parent directory to the sys.path to import modules correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import your models
from models.country import Country
from models.city import City  # Adjust this based on your project structure

class TestCountry(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.country = Country(name="TestCountry")
        self.city = City(name="TestCity", country=None)  # Example city for testing

    def test_country_initialization(self):
        """Test the initialization of the Country object"""
        self.assertEqual(self.country.name, "TestCountry")
        self.assertEqual(self.country.cities, [])

    def test_add_city_to_country(self):
        """Test adding a city to a Country"""
        self.country.add_city(self.city)
        self.assertIn(self.city, self.country.cities)
        self.assertEqual(self.city.country, self.country)

    def test_remove_city_from_country(self):
        """Test removing a city from a Country"""
        self.country.add_city(self.city)
        self.country.remove_city(self.city)
        self.assertNotIn(self.city, self.country.cities)
        self.assertIsNone(self.city.country)

    def test_to_dict_method(self):
        """Test the to_dict method of the Country class"""
        country_dict = self.country.to_dict()
        self.assertEqual(country_dict['name'], "TestCountry")
        self.assertEqual(country_dict['cities'], [])

if __name__ == "__main__":
    unittest.main()
