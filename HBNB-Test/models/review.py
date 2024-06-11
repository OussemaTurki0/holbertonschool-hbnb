from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, text, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        self.user_id = user_id
        self.place_id = place_id
        self.text = text

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
        })
        return data
