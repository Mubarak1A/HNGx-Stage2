"""A simple REST API app capable of CRUD operations."""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#creating database file with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_api.db'
db = SQLAlchemy(app)

class Person(db.Model):
    '''Create Person Model'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        '''initialize class varible name'''
        self.name = name

#create db tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Home page route function"""
    return '<h1> HNGx-Stage 2 CRUD project task! </h1>'


@app.route('/api', methods=['POST'])
def create_person():
    '''Add the user to the database'''
    name = request.json.get('name')

    if not name:
        return jsonify({'message': 'name is required'}), 404

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({'message': 'Person created Successfully'}), 201


@app.route('/api/person/<int:user_id>', methods=['GET'])
def get_person(user_id):
    '''Read and return user details from Database'''
    person = Person.query.get(user_id)

    if not person:
        return jsonify({'message': 'person not found'}), 404

    return jsonify({'id': person.id, 'name': person.name})


@app.route('/api/person/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    '''Update user details on Database'''
    person = Person.query.get(user_id)

    if not person:
        return jsonify({'message': 'person not found'}), 404

    new_name = request.json.get('name')

    if not new_name:
        return jsonify({'message': 'New name is required'}), 400

    Person.name = new_name
    db.session.commit()

    return jsonify({'message': 'Person updated successfully'}), 200


@app.route('/api/person/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    '''Delete User from Database'''
    person = Person.query.get(user_id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()

    return jsonify({'message': 'Person deleted successfully'}), 204


@app.route('/api/persons', methods=['GET'])
def get_person_by_name():
    '''Retreive users with a name'''
    name = request.args.get('name')

    if not name:
        return jsonify({'message': 'Name parameter is required'}), 400

    persons = Person.query.filter_by(name=name).all()

    if not persons:
        return jsonify({'message': 'No persons found with the provided name'}), 404

    persons_data = [{'id': person.id, 'name': person.name} for person in persons]

    return jsonify(persons_data)


if __name__ == '__main__':
    app.run(debug=True)
