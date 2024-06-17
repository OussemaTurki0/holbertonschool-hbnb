from models.base_model import BaseModel


class User(BaseModel):
    registered_emails = set()

    def __init__(self, email, first_name, last_name, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        if email in User.registered_emails:
            raise ValueError("Email already registered")
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []  # List to store places associated with the user
        self.reviews = []   # Initialize reviews
        User.registered_emails.add(email)


    # Method to add a hosted place
    def add_hosted_place(self, place):
        if place.user_id!= self.id:
            raise ValueError("Cannot add a place hosted by another user")
        self.places.append(place)
        place.user_id = self.id  # Maintain referential integrity

    # Method to add a review
    def add_review(self, place_id, text):
        review = Review(self.id, place_id, text)
        self.reviews.append(review)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'places': [place.to_dict() for place in self.places],  # Serialize hosted places
            'reviews': [review.to_dict() for review in self.reviews],  # Serialize reviews
        })
        return data
