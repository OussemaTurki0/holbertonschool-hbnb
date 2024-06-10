# models/city.py

from models.base_model import BaseModel
from models.city import Country

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country
        self.places = []

    def update(self, name=None):
        if name is not None:
            self.name = name
        super().update()

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            self.country.add_city(self)
            self.updated_at = datetime.now()

    def remove_place(self, place):
        if place in self.places:
            self.places.remove(place)
            self.country.remove_city(self)
            self.updated_at = datetime.now()
