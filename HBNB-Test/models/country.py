from datetime import datetime
from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.name = name
        self.cities = []  # List to store cities in the country

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            city.country = self     # Update the City's reference to this Country
            self.updated_at = datetime.now()  # Update timestamp

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            city.country = None     # Remove the reference to this Country
            self.updated_at = datetime.now()  # Update timestamp

    def to_dict(self, include_cities=True):
        data = super().to_dict()
        if include_cities:
            cities_list = [city.to_dict(include_country=False) for city in self.cities]
        else:
            cities_list = None
        data.update({
            'name': self.name,
            'cities': cities_list
        })
        return data
