import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.place import Place
from persistence.place_data import Place_Data

class TestPlaceData(unittest.TestCase):

    def setUp(self):
        self.data = Place_Data()

    def test_save_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.data.save(place)
        self.assertIn(place.place_id, self.data.places)

    def test_get_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.data.save(place)
        fetched = self.data.get(place.place_id)
        self.assertEqual(fetched.name, 'Test Place')

    def test_update_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.data.save(place)
        update_data = {'name': 'Updated Place'}
        self.data.update(place.place_id, update_data)
        updated = self.data.get(place.place_id)
        self.assertEqual(updated.name, 'Updated Place')

    def test_delete_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.data.save(place)
        self.data.delete(place.place_id)
        self.assertIsNone(self.data.get(place.place_id))


if __name__ == '__main__':
    unittest.main()