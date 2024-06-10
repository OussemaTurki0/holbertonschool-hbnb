import sys, os
current_path = os.path.abspath(os.path.dirname(__file__))
models_directory = os.path.join(current_path, '..', '..', 'Models')
sys.path.append(models_directory)


import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def test_create_country_with_name(self):
        country = Country("Tunisia")
        self.assertEqual(country.name, "Tunisia")

if __name__ == "__main__":
    unittest.main()
