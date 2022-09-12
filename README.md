### Prerequisites
Install the following softwares for the application to run locally:
* Pipenv or virtualenvwrapper for setting up your environment variables.
    * **pip3 install venv** on your bash terminal to install.
    * run **python3 -m venv venv && source venv/bin/activate** to activate the environment.
* Install Flask.
    * run **pip3 install -r requirements.txt** command to your terminal to install.
    * run **FLASK_APP=run.py flask run** to start the application.

## Features
Endpoint that takes user name, email and password, stores in a database and returns the user email and name

* On your terminal run **curl -X POST -H "Content-Type: application/json"     -d '{"username": "john Doe", "email": "john.doe@example.com", "password":"pass123"}'     http://127.0.0.1:5000/user**
