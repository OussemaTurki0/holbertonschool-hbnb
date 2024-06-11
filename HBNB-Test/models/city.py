from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.name = name
        self.country_id = country_id
        self.places = []  # List to store places in the city

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_id': self.country_id,
        })
        return data
