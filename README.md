# Tree Structure API

This project is a backend application that imports a JSON file with hierarchical tree structure into a database, 
and provides an API endpoint to retrieve the next 20 elements from the tree based on a specific element ID.

WARNINGS:
- Some data docs have repeated ids, so I am generating auto incremented ids instead.
- '(...) returns the next 20 elements from the tree.' means: 20 elements whose parent is element, with a higher level 
that the given element and with a subchapter. Like Chapters 1.1 (level 2) or 1.2.3 (level 3) are for Chapter 1 (level 1).
- Since the data passed to the backend is the element id, you have to check that id from the database (file 'tree.db').
- The "Expected structure returned by the API endpoint" example cannot be fulfilled, since chapter 2 is not a child from
chapter 1.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- SQLite
- Flask
- SQLAlchemy

### Installing

- Clone the repository
    ```bash
    git clone https://github.com/<username>/tree-structure-api.git
    ```

#### Backend

- Move to the backend folder
    ```bash
    cd backend
    ```

- Create a virtual environment and activate it
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

- Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

##### Run the application
    ```bash
    python endpoint.py
    ```

##### Importing the JSON file
    ```bash
    python import_json.py
    ```
    This command will create the database and import the data from the JSON file

##### API Endpoints
- `/api/tree/<int:element_id>` : Retrieves the next 20 elements from the tree based on a specific element ID passed as a parameter.

---------------------------------------------------------------------------------

#### Frontend

- A frontend application written in React is provided in the frontend directory of the project.

- Navigate to the frontend directory and install the dependencies
```bash
cd frontend
npm install
```

- Run the development server
```bash
npm start
```

---------------------------------------------------------------------------------

## Author
Ing. Alvaro Rodriguez Scelza - https://github.com/alvaroscelza
