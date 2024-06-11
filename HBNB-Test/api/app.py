# Import necessary modules and classes
from flask import Flask, jsonify, request
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country
from persistence.data_manager import DataManager
from models.user import User
import sys

# Append the models directory to the system path
sys.path.append('/home/oussema/HBNB-Test/models')

# Create a Flask application
app = Flask(__name__)
# Create a DataManager instance
data_manager = DataManager()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # Get the JSON data from the request
    data = request.get_json()
    # Create a new User instance with the data
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    # Save the user to the data manager
    data_manager.save(user)
    # Return the user data as JSON with a status code of 201 (created)
    return jsonify(user.to_dict()), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    # Get all user IDs from the data manager and fetch each user
    users = [data_manager.get(user_id, 'User') for user_id in data_manager.data['User']]
    # Return the list of users as JSON with a status code of 200 (OK)
    return jsonify(users), 200

# Route to get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Get the user with the given ID from the data manager
    user = data_manager.get(user_id, 'User')
    # If the user exists, return it as JSON with a status code of 200 (OK)
    if user:
        return jsonify(user), 200
    # If the user does not exist, return an error message as JSON with a status code of 404 (Not Found)
    else:
        return jsonify({'error': 'User not found'}), 404

# Route to update a user by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    # Get the JSON data from the request
    data = request.get_json()
    # Create a new User instance with the updated data and the same ID
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], id=user_id)
    # Update the user in the data manager
    data_manager.update(user)
    # Return the updated user data as JSON with a status code of 200 (OK)
    return jsonify(user.to_dict()), 200

# Route to delete a user by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Delete the user with the given ID from the data manager
    data_manager.delete(user_id, 'User')
    # Return an empty response with a status code of 204 (No Content)
    return '', 204

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
