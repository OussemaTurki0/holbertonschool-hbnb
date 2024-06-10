# models/user.py
import bcrypt
from models.base_model import BaseModel

class User(BaseModel):
    _user_emails = set()

    def __init__(self, email, first_name, last_name):
        super().__init__()  # Initialize attributes from BaseModel
        self.email = email
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        if email in User._user_emails:
            raise ValueError(f"Email '{email}' already exists.")
        User._user_emails.add(email)

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
 
    def add_review(self, place):
        review = Review(place, self, rating, comment)
        review.save()
        place.add_review(review)
        