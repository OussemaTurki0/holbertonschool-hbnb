# Import the datetime class from the datetime module to handle date and time.
from datetime import datetime

# Define the Amenity class.
class Amenity:
    # Initialize a new instance of the Amenity class with a name attribute.
    def __init__(self, name):
        # Set the name attribute to the provided name value.
        self.name = name
        # Set the created_at attribute to the current date and time.
        self.created_at = datetime.now()
        # Set the updated_at attribute to the current date and time.
        self.updated_at = datetime.now()

    # Define the __repr__ method to provide a string representation of an Amenity instance.
    def __repr__(self):
        # Return a formatted string that includes the name attribute.
        return f"Amenity(name='{self.name}')"
