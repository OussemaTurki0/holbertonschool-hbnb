from datetime import datetime
import uuid


class User:
    def __init__(self, username, email, password):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
#returns user as a dict
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
