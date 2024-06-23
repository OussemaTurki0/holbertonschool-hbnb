import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.amenity import Amenity
from persistence.amenity_data import Amenity_Data


class TestAmenityData(unittest.TestCase):

    def setUp(self):
        self.data = Amenity_Data()

    def test_save_amenity(self):
        amenity = Amenity(name='WiFi')
        self.data.save(amenity)
        self.assertIn(amenity.amenity_id, self.data.amenities)

    def test_get_amenity(self):
        amenity = Amenity(name='WiFi')
        self.data.save(amenity)
        fetched = self.data.get(amenity.amenity_id)
        self.assertEqual(fetched.name, 'WiFi')

    def test_update_amenity(self):
        amenity = Amenity(name='WiFi')
        self.data.save(amenity)
        update_data = {'name': 'Updated WiFi'}
        self.data.update(amenity.amenity_id, update_data)
        updated = self.data.get(amenity.amenity_id)
        self.assertEqual(updated.name, 'Updated WiFi')

    def test_delete_amenity(self):
        amenity = Amenity(name='WiFi')
        self.data.save(amenity)
        self.data.delete(amenity.amenity_id)
        self.assertIsNone(self.data.get(amenity.amenity_id))


if __name__ == '__main__':
    unittest.main()