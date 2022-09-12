import json
from flask import request
from ..models  import User
from .. import db

from . import auth

@auth.route('/user', methods=[ 'POST'])
def get_user():
    db.create_all()
    request_data = request.get_json()
    user = User(email = request_data['email'],
                username = request_data['username'],
                password = request_data['password'])
    db.session.add(user)
    db.session.commit()
    data ={'email': request_data['email'], 'username': request_data['username']}
    json_data = json.dumps(data)
    return json_data