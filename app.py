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

@app.route('/api/person', methods=['POST'])
def create_user():
    '''Add the user to the database'''
    name = request.json.get('name')

    if not name:
        return jsonify({'message': 'name is required'}), 404

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({'message': 'Person created Successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
