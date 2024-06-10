# models/country.py

from models.base_model import BaseModel
from models.city import City

class Country(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, name=None):
        if name is not None:
            self.name = name
        super().update()

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            city.country = self     # Update the City's reference to this Country

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            city.country = None     # Remove the reference to this Country
