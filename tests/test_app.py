''''Module to test app file'''

import json
import pytest
from app import app, db, Person

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    db.create_all()
    yield client
    db.drop_all()

def test_create_person(client):
    data = {'name': 'John Doe'}
    response = client.post('/api/person', json=data)

    assert response.status_code == 201

    # Check if the person was added to the database
    person = Person.query.first()
    assert person.name == 'John Doe'

def test_get_person(client):
    # Add a person to the database for testing
    person = Person(name='Alice')
    db.session.add(person)
    db.session.commit()

    response = client.get('/api/person/1')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['id'] == 1
    assert data['name'] == 'Alice'

def test_get_person_not_found(client):
    response = client.get('/api/person/999')  # Non-existent ID

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'

def test_update_person(client):
    # Add a person to the database for testing
    person = Person(name='Bob')
    db.session.add(person)
    db.session.commit()

    new_data = {'name': 'Robert'}
    response = client.put('/api/person/1', json=new_data)

    assert response.status_code == 200

    # Check if the person's name was updated
    updated_person = Person.query.get(1)
    assert updated_person.name == 'Robert'

def test_update_person_not_found(client):
    new_data = {'name': 'Updated Name'}
    response = client.put('/api/person/999', json=new_data)  # Non-existent ID

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'

def test_delete_person(client):
    # Add a person to the database for testing
    person = Person(name='Carol')
    db.session.add(person)
    db.session.commit()

    response = client.delete('/api/person/1')

    assert response.status_code == 204

    # Check if the person was deleted from the database
    deleted_person = Person.query.get(1)
    assert deleted_person is None

def test_delete_person_not_found(client):
    response = client.delete('/api/person/999')  # Non-existent ID

    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Person not found'
