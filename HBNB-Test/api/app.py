# Import necessary modules and classes
from flask import Flask, jsonify, request
from models.user import User
from models.place import Place
from persistence.data_manager import DataManager

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
    data_manager.save(user)
    return jsonify(user.to_dict()), 201

#-------------------------------------------------------------------------------------------------------------------------
# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = [data_manager.get(user_id, 'User') for user_id in data_manager.data['User']]
    return jsonify(users), 200

#-------------------------------------------------------------------------------------------------------------------------
# Route to get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, 'User')
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

#-------------------------------------------------------------------------------------------------------------------------
# Route to update a user by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get(user_id, 'User')
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    data_manager.update(user)
    return jsonify(user.to_dict()), 200

#-------------------------------------------------------------------------------------------------------------------------
# Route to delete a user by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    data_manager.delete(user_id, 'User')
    return '', 204

#-------------------------------------------------------------------------------------------------------------------------
# POST /places
@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(name=data['name'], description=data['description'])
    data_manager.save(place)
    return jsonify(place.to_dict()), 201

#-------------------------------------------------------------------------------------------------------------------------
# GET /places
@app.route('/places', methods=['GET'])
def get_places():
    places = [data_manager.get(place_id, 'Place') for place_id in data_manager.data['Place']]
    return jsonify(places), 200

#-------------------------------------------------------------------------------------------------------------------------
# GET /places/<place_id>
@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if place:
        return jsonify(place), 200
    else:
        return jsonify({'error': 'Place not found'}), 404

#-------------------------------------------------------------------------------------------------------------------------
# PUT /places/<place_id>
@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = data_manager.get(place_id, 'Place')
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    place.name = data['name']
    place.description = data['description']
    data_manager.update(place)
    return jsonify(place.to_dict()), 200

#-------------------------------------------------------------------------------------------------------------------------
# DELETE /places/<place_id>
@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    data_manager.delete(place_id, 'Place')
    return '', 204

#-------------------------------------------------------------------------------------------------------------------------
# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
