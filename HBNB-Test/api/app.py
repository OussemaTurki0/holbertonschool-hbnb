# Import necessary modules and classes
from flask import Flask, jsonify, request
from models.user import User
from models.place import Place
from persistence.data_manager import DataManager
import requests

# Create a Flask application
app = Flask(__name__)
# Create a DataManager instance
data_manager = DataManager()

#-------------------------------------------------------------------------------------------------------------------------
# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing data'}), 400

    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    response = requests.post('http://your-api-url/users', json=user.to_dict())
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get('http://your-api-url/users')
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# Route to get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f'http://your-api-url/users/{user_id}')
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# Route to update a user by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    response = requests.put(f'http://your-api-url/users/{user_id}', json=user.to_dict())
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# Route to delete a user by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = requests.delete(f'http://your-api-url/users/{user_id}')
    return '', response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# POST /places
@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(name=data['name'], description=data['description'])
    response = requests.post('http://your-api-url/places', json=place.to_dict())
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# GET /places
@app.route('/places', methods=['GET'])
def get_places():
    response = requests.get('http://your-api-url/places')
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# GET /places/<place_id>
@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    response = requests.get(f'http://your-api-url/places/{place_id}')
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# PUT /places/<place_id>
@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = Place(name=data['name'], description=data['description'])
    response = requests.put(f'http://your-api-url/places/{place_id}', json=place.to_dict())
    return jsonify(response.json()), response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# DELETE /places/<place_id>
@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    response = requests.delete(f'http://your-api-url/places/{place_id}')
    return '', response.status_code

#-------------------------------------------------------------------------------------------------------------------------
# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
