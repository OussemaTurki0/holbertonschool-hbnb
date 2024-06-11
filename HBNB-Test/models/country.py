from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.name = name
        self.cities = []  # List to store cities in the country

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
        })
        return data
