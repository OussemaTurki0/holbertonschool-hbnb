from datetime import datetime
from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country=None, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.name = name
        self.country = country
        self.places = []  # List to store places in the city

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            place.city_id = self.id
            self.updated_at = datetime.now()

    def remove_place(self, place):
        if place in self.places:
            self.places.reimove(place)
            place.city_id = None
            self.updated_at = datetime.now()

    def set_country(self, country):
        if self.country != country:
            if self.country is not None:
                self.country.remove_city(self)  # Remove from the old country
            self.country = country
            if country is not None:
                country.add_city(self)  # Add to the new country
            self.updated_at = datetime.now()  # Update timestamp

    def to_dict(self, include_country=True):
        data = super().to_dict()
        country_dict = self.country.to_dict(include_cities=False) if self.country and include_country else None
        data.update({
            'name': self.name,
            'country': country_dict,
            'places': [place.to_dict() for place in self.places]
        })
        return data
