# API Documentation

This documentation provides information on how to use the API for managing persons. The API supports CRUD (Create, Read, Update, Delete) operations on persons.

## Base URL

The base URL for all endpoints is: `https://hngx-stage2-161q.onrender.com`

## Endpoints

### 1. Create a New Person

**Endpoint:** `/api/person`
**Method:** `POST`
**Request Format:**
{
    "name": "John Doe"
}
**Response Format (Success):**
{
    "message": "Person created successfully"
}
**Response Format (Error):**
{
    "message": "Name is required"
}

### 2. Get Person by ID

**Endpoint:** `/api/person/<user_id>`
**Method:** `GET`

**Response Format (Success):**
{
    "id": 1,
    "name": "John Doe"
}
**Response Format (Error):**
{
    "message": "Person not found"
}

### 3. Update Person Details
**Endpoint:** `/api/person/<user_id>`
**Method:** `PUT`
**Request Format:**
{
    "name": "Updated Name"
}

**Response Format (Success):**
{
    "message": "Person updated successfully"
}
**Response Format (Error):**
{
    "message": "Person not found"
}

### 4. Delete a Person
**Endpoint:** `/api/person/<user_id>`
**Method:** `DELETE`

**Response Format (Success):**
{`
    "message": "Person deleted successfully"
}
**Response Format (Success):**
{
    "message": "Person not found"
}

# Modelling Diagrams:
## UML DIAGRAM
<img src="/imgs/UML.png", max-width: 300px">
## E-R DIAGRAM
<img src="/imgs/E-R.png", max-width: 300px">
