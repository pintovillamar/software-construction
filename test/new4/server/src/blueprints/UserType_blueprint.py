from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.UserType_model import UserTypeModel, UserType

from models.User_model import User

# tokens 
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["id"]).first()
            print(current_user)
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated

model = UserTypeModel()

UserTypeBlueprint = Blueprint("UserTypeBlueprint", __name__)

# Login
@UserTypeBlueprint.route("/login", methods=["GET"])
@cross_origin()
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})
    
    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})

    if user.password == auth.password:
        token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(minutes = 30)}, app.config["SECRET_KEY"])
        
        return jsonify({'token': token})
    
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})

@UserTypeBlueprint.route("/create_user_type", methods=["POST"])
@token_required
@cross_origin()
def create_user_type():
    name = request.json["name"]
    description = request.json["description"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_user_type(name, description, created_at, updated_at))

@UserTypeBlueprint.route("/user_type/<id>", methods=["GET"])
@token_required
@cross_origin()
def user_type(id):
    content = model.user_type(id)
    return jsonify(content)

@UserTypeBlueprint.route("/user_types", methods=["GET"])
@token_required
@cross_origin()
def user_types():
    content = model.user_types()
    return jsonify(content)

@UserTypeBlueprint.route("/update_user_type/<id>", methods=["PUT"])
@cross_origin()
@token_required
def update_user_type(id):
    # user = User.query.get(std_id.usr_id)
    user_created = UserType.query.get(id)
    name = request.json["name"]
    description = request.json["description"]
    created_at = user_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_user_type(id, name, description,created_at ,updated_at))

@UserTypeBlueprint.route("/delete_user_type/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_user_type(id):
    return jsonify(model.delete_user_type(id))
