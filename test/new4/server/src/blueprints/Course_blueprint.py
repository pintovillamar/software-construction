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

from models.Course_model import CourseModel, Course

from models.User_model import User

model = CourseModel()

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
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated

CourseBlueprint = Blueprint("CourseBlueprint", __name__)

# Login 
@CourseBlueprint.route("/login", methods=["GET"])
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

@CourseBlueprint.route("/create_course", methods=["POST"])
@token_required
@cross_origin()
def create_course():
    f = request.files['file']
    filename = secure_filename(f.filename)
    # path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename

    data = json.loads(request.form.get('data'))

    content = model.create_course(
        data["name"],               # name
        data["des"],                # des
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    updated = rename_pic(Course.query.get(content["id"]).id)

    content = model.update_course(
        content["id"],              # id
        data["name"],               # name
        data["des"],                # des
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    f.save(updated + filename)

    return jsonify(content)

@CourseBlueprint.route("/course/<id>", methods=["GET"])
@token_required
@cross_origin()
def course(id):
    content = model.course(id)
    return jsonify(content)

@CourseBlueprint.route("/courses", methods=["GET"])
@token_required
@cross_origin()
def courses():
    content = model.courses()
    return jsonify(content)

@CourseBlueprint.route("/update_course/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_course(id):
    course_created = Course.query.get(id)

    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))

    content = model.update_course(
        id,                         # id
        data["name"],               # name
        data["des"],                # des
        course_created.created_at,  # created_at
        datetime.now()              # updated_at
    )

    f.save(updated)

    return jsonify(model.update_course(content))

@CourseBlueprint.route("/delete_course/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_course(id):
    return jsonify(model.delete_course(id))

def rename_pic(id):
    courser_id = id
    courser_id = Course.query.get(courser_id).id
    name = Course.query.get(courser_id).name
    des = Course.query.get(courser_id).des

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_name_course = path +str(courser_id)+"_"+name+"_"+des+"-"
    return new_name_course