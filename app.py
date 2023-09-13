"""A simple REST API app capable of CRUD operations."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Home page route function"""
    return '<h1> HNGx-Stage 2 CRUD project task! </h1>'

if __name__ == '__main__':
    app.run(debug=True)
