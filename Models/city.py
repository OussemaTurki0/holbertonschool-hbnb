# models/city.py

from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country

    def update(self, name=None):
        if name is not None:
            self.name = name
        super().update()
