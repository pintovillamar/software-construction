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

from models.Teacher_model import TeacherModel, Teacher

from models.User_model import User

model = TeacherModel()

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

TeacherBlueprint = Blueprint("TeacherBlueprint", __name__)

# Login 
@TeacherBlueprint.route("/login", methods=["GET"])
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

@TeacherBlueprint.route("/create_teacher", methods=["POST"])
@token_required
@cross_origin()
def create_teacher():
    f = request.files['file']
    filename = secure_filename(f.filename)
    # path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename
    
    data = json.loads(request.form.get('data'))

    content = model.create_teacher(
        data["user_id"],            # user_id
        data["type"],               # type
        data["cat"],                # cat
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    updated = rename_pic(Teacher.query.get(content["id"]).id)

    content = model.update_teacher(
        content["id"],              # id
        data["user_id"],            # user_id
        data["type"],               # type
        data["cat"],                # cat
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    f.save(updated + filename)

    return jsonify(content)

@TeacherBlueprint.route("/teacher/<id>", methods=["GET"])
@token_required
@cross_origin()
def teacher(id):
    content = model.teacher(id)
    return jsonify(content)

@TeacherBlueprint.route("/teachers", methods=["GET"])
@token_required
@cross_origin()
def teachers():
    content = model.teachers()
    return jsonify(content)

@TeacherBlueprint.route("/update_teacher/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_teacher(id):
    teacher_created = Teacher.query.get(id)

    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))

    content = model.update_teacher(
        id,                         # id
        data["user_id"],            # user_id
        data["type"],               # type
        data["cat"],                # cat
        teacher_created.created_at, # created_at
        datetime.now()              # updated_at
    )

    f.save(updated)

    return jsonify(model.update_teacher(content))

@TeacherBlueprint.route("/delete_teacher/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_teacher(id):
    return jsonify(model.delete_teacher(id))

def rename_pic(id):
    teacher_id = id
    teacher_id = Teacher.query.get(teacher_id).id
    user_id = Teacher.query.get(teacher_id).user_id
    type = Teacher.query.get(teacher_id).type
    cat = Teacher.query.get(teacher_id).cat

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_type_teacher = path +str(teacher_id)+"_"+user_id+"_"+type+"_"+cat+"-"
    return new_type_teacher