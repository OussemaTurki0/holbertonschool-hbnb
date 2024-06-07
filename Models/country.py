# models/country.py

from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, name=None):
        if name is not None:
            self.name = name
        super().update()
