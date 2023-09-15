''''Module to test app file'''

import json
import pytest
from app import app, db, Person

@pytest.fixture
def client():
    ''''format default client var from pytest library'''
    app.config['TESTING'] = True
    client = app.test_client()
    db.create_all()
    yield client
    db.drop_all()

def test_create_person(client):
    '''Test Create_user: Check if the person was added to the database'''
    data = {'name': 'John Doe'}
    response = client.post('/api', json=data)

    assert response.status_code == 201

    person = Person.query.first()
    assert person.name == 'John Doe'

def test_get_person(client):
    ''''Test get_person route function'''
    # Add a person to the database for testing
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
    response = client.get('/api/999')

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'

def test_update_person(client):
    '''Test update_person route function'''
    # Add a person to the database for testing
    person = Person(name='Bob')
    db.session.add(person)
    db.session.commit()

    new_data = {'name': 'Robert'}
    response = client.put('/api/1', json=new_data)

    assert response.status_code == 200

    # Check if the person's name was updated
    updated_person = Person.query.get(1)
    assert updated_person.name == 'Robert'

def test_update_person_not_found(client):
    '''Test update_person error handling'''
    new_data = {'name': 'Updated Name'}
    response = client.put('/api/999', json=new_data)

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'

def test_delete_person(client):
    ''''Test delete_person route function'''
    # Add a person to the database for testing
    person = Person(name='Carol')
    db.session.add(person)
    db.session.commit()

    response = client.delete('/api/1')

    assert response.status_code == 204

    # Check if the person was deleted from the database
    deleted_person = Person.query.get(1)
    assert deleted_person is None

def test_delete_person_not_found(client):
    ''''Test delete person error handling'''
    response = client.delete('/api/999')

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'
