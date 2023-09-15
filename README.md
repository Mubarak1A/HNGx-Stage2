# HNGx-Stage2
HNGx (ZuriBoard) intership Stage Two Task.
# Task Breakdown: 
Develop a REST API with Basic CRUD Operation
# Objective: 
Build a simple REST API capable of CRUD operations on a resource, say, a "person". The chosen programming language should interface with any chosen database of your choice.
1. REST API Development:
    Develop an API with endpoints for:
        - CREATE: Adding a new person.  =>/api
        - READ: Fetching details of a person.  => /api/user_id
        - UPDATE: Modifying details of an existing person => /api/user_id
        - DELETE: Removing a person => /api/user_id
Ensure all interactions with the database are secure and free from common vulnerabilities (e.g., SQL injections).
2. Database Modelling: (Bonus)
    UML Diagram: Design and present a UML (Unified Modeling Language) diagram that represents the structure and relationships of your API's classes and models.
3. Testing:
    Using tools like Postman or (scripts written in Python using the requests library) that tests each CRUD operation in your API.
    This  should:
        - Add a new person (e.g., "Mark Essien").
        - Fetch details of a person
        - Modify the details of an existing person.
        - Remove a person
4. Dynamic Parameter Handling:
    Your API should be flexible enough to handle dynamic input. If we provide a name (or other details), your backend should be able to process operations using that name.
    Example: If we pass "Mark Essien", we should be able to perform all CRUD operations on "Mark Essien".
    Add validation – field should only be strings; integers or any other data type should not be allowed.
5. Hosting
    Using the same Server used in the Stage One task (or another server, if possible), modify it accordingly to  host your endpoint with a URL like this https://theirdomain.com/api
Test extensively with various testing tools to make sure it is accessible before submitting

# Modelling Diagrams:
## UML DIAGRAM
<img src="/imgs/UML.png">
## E-R DIAGRAM
<img src="/imgs/E-R.png">
