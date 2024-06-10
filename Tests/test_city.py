import sys, os
current_path = os.path.abspath(os.path.dirname(__file__))
models_directory = os.path.join(current_path, '..', '..', 'Models')
sys.path.append(models_directory)


import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    def test_create_city_with_name_and_country(self):
        country = Country("Tunisia")
        city = City("Sidi Bou Said", country)
        self.assertEqual(city.name, "Sidi Bou Said")

if __name__ == "__main__":
    unittest.main()
