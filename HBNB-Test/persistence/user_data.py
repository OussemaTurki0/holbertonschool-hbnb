from datetime import datetime
from models.user import User
from persistence.ipersistence_manager import IPersistenceManager


class User_Data(IPersistenceManager):
#empty dictionary to store user objects.
    def __init__(self):
        self.users = {}

    def save(self, user):
# Saves a user
        user.created_at = datetime.now()
        user.updated_at = datetime.now()
        self.users[user.user_id] = user

    def get(self, user_id):
# bring a user
        return self.users.get(user_id)

    def get_all(self):
# bring all users.
        return list(self.users.values())

    def update(self, user_id, new_user_data):
# Updates an existing user
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_user_data)
            user.updated_at = datetime.now()
            self.save(user)
            return True
        return False

    def delete(self, user_id):
# Delet an existing user
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
