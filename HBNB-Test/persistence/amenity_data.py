from datetime import datetime
from models.amenity import Amenity
from persistence.ipersistence_manager import IPersistenceManager


class Amenity_Data(IPersistenceManager):
#empty dictionary to store amenity objects.
    def __init__(self):
        self.amenities = {}

    def save(self, amenity):
# Saves an amenity
        amenity.created_at = datetime.now()
        amenity.updated_at = datetime.now()
        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
# bring an amenity
        return self.amenities.get(amenity_id)

    def get_all(self):
# bring all amenities
        return list(self.amenities.values())

    def update(self, amenity_id, new_amenity_data):
# Updates an existing amenity
        if amenity_id in self.amenities:
            amenity = self.amenities[amenity_id]
            for key, value in new_amenity_data.items():
                setattr(amenity, key, value)
            amenity.updated_at = datetime.now()
            self.save(amenity)
            return True
        return False

    def delete(self, amenity_id):
# Deletes an existing amenity
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False