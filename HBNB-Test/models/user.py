from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []  # List to store places associated with the user

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
        })
        return data
