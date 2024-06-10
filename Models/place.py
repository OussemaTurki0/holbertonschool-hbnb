# models/place.py

from models.base_model import BaseModel
from models.user import User

class Place(BaseModel):
    def __init__(self, name, description, address, city, latitude, longitude, host, number_of_rooms,
                 bathrooms, price_per_night, max_guests, amenities=[]):
        super().__init__()
        self.amenities = []
        self.reviews = []
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().update()

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def set_host(self, host):
        if not isinstance(host, User):
            raise ValueError("Host must be a User object")
        self.host_id = host
