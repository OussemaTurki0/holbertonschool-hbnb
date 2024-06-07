# models/user.py

from models.base_model.py import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()  # Initialize attributes from BaseModel
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        super().update()  # Call update method from BaseModel to update `updated_at`

	def add_place(self, place):
	"""
	Method to add a place to the list of places owned by the user.
	"""
	self.places.append(place)