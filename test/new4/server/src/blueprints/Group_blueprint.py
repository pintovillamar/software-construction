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

from models.Group_model import GroupModel, Group

from models.User_model import User

model = GroupModel()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


GroupBlueprint = Blueprint("GroupBlueprint", __name__)

# Login 
@GroupBlueprint.route("/login", methods=["GET"])
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

@GroupBlueprint.route("/create_group", methods=["POST"])
@token_required
@cross_origin()
def create_group():
    f = request.files['file']
    filename = secure_filename(f.filename)
    # path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename
    
    data = json.loads(request.form.get('data'))

    content = model.create_group(
        data["teacher_id"],         # teacher_id
        data["name"],               # name
        data["course_id"],          # course_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    updated = rename_pic(Group.query.get(content["id"]).id)

    content = model.update_group(
        content["id"],              # id
        data["teacher_id"],         # teacher_id
        data["name"],               # name
        data["course_id"],          # course_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    f.save(updated + filename)

    return jsonify(content)

@GroupBlueprint.route("/group/<id>", methods=["GET"])
@token_required
@cross_origin()
def group(id):
    content = model.group(id)
    return jsonify(content)

@GroupBlueprint.route("/groups", methods=["GET"])
@token_required
@cross_origin()
def groups():
    content = model.groups()
    return jsonify(content)

@GroupBlueprint.route("/update_group/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_group(id):
    group_created = Group.query.get(id)

    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))

    content = model.update_group(
        id,                         # id
        data["teacher_id"],         # teacher_id
        data["name"],               # name
        data["course_id"],          # course_id
        group_created.created_at,   # created_at
        datetime.now()              # updated_at
    )

    f.save(updated)

    return jsonify(model.update_group(content))

@GroupBlueprint.route("/delete_group/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_group(id):
    return jsonify(model.delete_group(id))

def rename_pic(id):
    group_id = id
    group_id = Group.query.get(group_id).id
    teacher_id = Group.query.get(group_id).teacher_id
    name = Group.query.get(group_id).name
    course_id = Group.query.get(group_id).course_id

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_name_group = path +str(group_id)+"_"+teacher_id+"_"+name+"_"+course_id+"-"
    return new_name_group