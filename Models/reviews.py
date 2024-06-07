# models/review.py

from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place, user, rating, comment):
        super().__init__()
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment

    def update(self, rating=None, comment=None):
        if rating is not None:
            self.rating = rating
        if comment is not None:
            self.comment = comment
        super().update()
