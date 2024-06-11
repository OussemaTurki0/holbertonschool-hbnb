from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, city_id, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.name = name
        self.description = description
        self.city_id = city_id
        self.user_id = user_id
        self.reviews = []  # List to store reviews for the place
        self.amenities = []  # List to store amenities for the place

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'description': self.description,
            'city_id': self.city_id,
            'user_id': self.user_id,
        })
        return data
