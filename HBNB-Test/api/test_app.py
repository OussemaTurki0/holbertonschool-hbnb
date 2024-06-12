from app import app, data_manager
from models.user import User
from models.place import Place

def test_create_user(client):
    response = client.post('/users', json={
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['email'] == 'test@example.com'
    assert data['first_name'] == 'Test'
    assert data['last_name'] == 'User'

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_user(client):
    user = User(id='1', email='test@example.com', first_name='Test', last_name='User')
    data_manager.save(user)
    response = client.get('/users/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['email'] == 'test@example.com'
    assert data['first_name'] == 'Test'
    assert data['last_name'] == 'User'

def test_update_user(client):
    user = User(id='1', email='test@example.com', first_name='Test', last_name='User')
    data_manager.save(user)
    response = client.put('/users/1', json={
        'email': 'updated@example.com',
        'first_name': 'Updated',
        'last_name': 'User'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['email'] == 'updated@example.com'
    assert data['first_name'] == 'Updated'
    assert data['last_name'] == 'User'

def test_delete_user(client):
    user = User(id='1', email='test@example.com', first_name='Test', last_name='User')
    data_manager.save(user)
    response = client.delete('/users/1')
    assert response.status_code == 204

def test_create_place(client):
    response = client.post('/places', json={
        'name': 'Test Place',
        'description': 'A nice place to visit'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Place'
    assert data['description'] == 'A nice place to visit'

def test_get_places(client):
    response = client.get('/places')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_place(client):
    place = Place(id='1', name='Test Place', description='A nice place to visit')
    data_manager.save(place)
    response = client.get('/places/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Test Place'
    assert data['description'] == 'A nice place to visit'

def test_update_place(client):
    place = Place(id='1', name='Test Place', description='A nice place to visit')
    data_manager.save(place)
    response = client.put('/places/1', json={
        'name': 'Updated Place',
        'description': 'An updated nice place to visit'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Place'
    assert data['description'] == 'An updated nice place to visit'

def test_delete_place(client):
    place = Place(id='1', name='Test Place', description='A nice place to visit')
    data_manager.save(place)
    response = client.delete('/places/1')
    assert response.status_code == 204
