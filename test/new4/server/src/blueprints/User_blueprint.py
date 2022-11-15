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

from models.User_model import UserModel, User

model = UserModel()

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

UserBlueprint = Blueprint("UserBlueprint", __name__)

# Login 
@UserBlueprint.route("/login", methods=["GET"])
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

@UserBlueprint.route("/create_user", methods=["POST"])
@token_required
@cross_origin()
def create_user():
    # photo upload process
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename
    # photo upload process

    data = json.loads(request.form.get('data'))

    content = model.create_user(
        data["name"],               # name
        data["last_name"],          # last_name
        data["dni"],                # dni
        data["email"],              # email
        data["password"],           # password
        path,                       # photo
        data["user_type_id"],       # user_type_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )
    
    updated = rename_pic(User.query.get(content["id"]).id)

    content = model.update_user(
        content["id"],              # id
        data["name"],               # name
        data["last_name"],          # last_name
        data["dni"],                # dni
        data["email"],              # email
        data["password"],           # password
        updated + filename,                    # photo
        data["user_type_id"],       # user_type_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    f.save(updated + filename)

    return jsonify(content)

@UserBlueprint.route("/user/<id>", methods=["GET"])
@token_required
@cross_origin()
def user(id):
    content = model.user(id)
    return jsonify(content)

@UserBlueprint.route("/users", methods=["GET"])
@token_required
@cross_origin()
def users(current_user):
    if current_user.user_type_id == 1:
        content = model.users()
        return jsonify(content)
    return jsonify({"message": "You are not authorized to view this page!"})
    
@UserBlueprint.route("/update_user/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_user(id):
    user_created = User.query.get(id)
    # name = request.json["name"]
    # last_name = request.json["last_name"]
    # dni = request.json["dni"]
    # email = request.json["email"]
    # password = request.json["password"]
    # photo = request.json["photo"]
    # user_type_id = request.json["user_type_id"]
    # created_at = user_created.created_at
    # updated_at = datetime.now()

    updated = rename_pic(id)

    f = request.files['file']
    filename = secure_filename(f.filename)
    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename

    data = json.loads(request.form.get('data'))

    content = model.update_user(
        id,                         # id
        data["name"],               # name
        data["last_name"],          # last_name
        data["dni"],                # dni
        data["email"],              # email
        data["password"],           # password
        path + updated,             # photo
        data["user_type_id"],       # user_type_id
        user_created.created_at,    # created_at
        datetime.now()              # updated_at
    )

    f.save(updated)

    return jsonify(model.update_user(content))

@UserBlueprint.route("/delete_user/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_user(id):
    return jsonify(model.delete_user(id))

def rename_pic(id):
    user_id = id    
    user_id = User.query.get(user_id).id
    user_name = User.query.get(user_id).name
    user_last_name = User.query.get(user_id).last_name

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_name = path +str(user_id)+"_"+user_name+"_"+user_last_name+"-"
    return new_name



