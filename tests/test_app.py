''''Module to test app file'''

import json
import pytest
from app import app, db, Person

@pytest.fixture
def client():
    ''''format default client var from pytest library'''
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_create_person(client):
    '''Test Create_user: Check if the person was added to the database'''
    with app.app_context():
        data = {'name': 'John Doe'}
        response = client.post('/api', json=data)

        assert response.status_code == 201

        person = Person.query.first()
        assert person.name == 'John Doe'

def test_get_person(client):
    ''''Test get_person route function'''
    # Add a person to the database for testing
    with app.app_context():
        person = Person(name='Alice')
        db.session.add(person)
        db.session.commit()

        response = client.get('/api/1')

        assert response.status_code == 200

        data = json.loads(response.data.decode('utf-8'))
        assert data['id'] == 1
        assert data['name'] == 'Alice'

def test_get_person_not_found(client):
    ''''Test get_person error handling'''
    with app.app_context():
        response = client.get('/api/999')

        assert response.status_code == 404

        data = json.loads(response.data.decode('utf-8'))
        assert data['message'] == 'person not found'

def test_update_person(client):
    '''Test update_person route function'''
    # Add a person to the database for testing
    with app.app_context():
        person = Person(name='Bob')
        db.session.add(person)
        db.session.commit()

        new_data = {'name': 'Robert'}
        response = client.put('/api/1', json=new_data)

        assert response.status_code == 200

        updated_person = Person.query.get(1)
        assert updated_person.name == 'Bob'

def test_update_person_not_found(client):
    '''Test update_person error handling'''
    with app.app_context():
        new_data = {'name': 'Updated Name'}
        response = client.put('/api/999', json=new_data)

        assert response.status_code == 404

        data = json.loads(response.data.decode('utf-8'))
        assert data['message'] == 'person not found'

def test_delete_person(client):
    ''''Test delete_person route function'''
    # Add a person to the database for testing
    with app.app_context():
        person = Person(name='Carol')
        db.session.add(person)
        db.session.commit()

        response = client.delete('/api/1')

        assert response.status_code == 204

        deleted_person = Person.query.get(1)
        assert deleted_person is None

def test_delete_person_not_found(client):
    ''''Test delete person error handling'''
    response = client.delete('/api/999')

    assert response.status_code == 404

    with app.app_context():
        data = json.loads(response.data.decode('utf-8'))
        assert data['message'] == 'Person not found'
