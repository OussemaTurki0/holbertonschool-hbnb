from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())  # Unique identifier for each instance
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()  # Update the updated_at timestamp

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
