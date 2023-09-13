"""A simple REST API app capable of CRUD operations."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#creating database file with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_api.db'
db = SQLAlchemy(app)

class Person(db):
    '''Create Person Model'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        '''initialize class varible name'''
        self.name = name

@app.route('/')
def index():
    """Home page route function"""
    return '<h1> HNGx-Stage 2 CRUD project task! </h1>'

if __name__ == '__main__':
    app.run(debug=True)
