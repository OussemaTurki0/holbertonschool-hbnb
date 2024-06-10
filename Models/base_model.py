# Import the uuid module to generate unique identifiers.
import uuid

# Import the datetime class from the datetime module to handle date and time.
from datetime import datetime

# Define the BaseModel class.
class BaseModel:
    # Initialize a new instance of the BaseModel class.
    def __init__(self):
        # Set the id attribute to a new unique UUID (converted to a string).
        self.id = str(uuid.uuid4())
        # Set the created_at attribute to the current date and time when the instance is created.
        self.created_at = datetime.now()
        # Set the updated_at attribute to the current date and time when the instance is created.
        self.updated_at = datetime.now()

    # Define the save method to update the updated_at attribute to the current date and time.
    def save(self):
        self.updated_at = datetime.now()

    # Define the to_dict method to return a dictionary representation of the instance.
    def to_dict(self):
        return self.__dict__
