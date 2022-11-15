from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from conn import app

from external import convertToJson

import jwt
from functools import wraps

from datetime import datetime, timedelta

from datetime import datetime

from models.Student_model import StudentModel
from models.User_model import User

model = StudentModel()

StudentBlueprint = Blueprint("StudentBlueprint", __name__)

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

# Login 
@StudentBlueprint.route("/login", methods=["GET"])
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

@StudentBlueprint.route("/create_student", methods=["POST"])
@cross_origin()
@token_required
def create_student():
    # get user id to use it and and transform photo to
    # vector using flask_face_recognition
    user_id = request.json["user_id"]
    user = User.query.get(user_id)

    url = "http://localhost:81/openfaceAPI"
    files = {'file': open(user.photo, 'rb')}
    vector = requests.post(url, files=files)
    vector = convertToJson(vector.text)

    content = model.create_student(
        user_id,                    # user_id
        request.json["regular"],    # regular
        request.json["year"],       # year
        str(vector),                # vector
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    return jsonify(content)

@StudentBlueprint.route("/student/<id>", methods=["GET"])
@token_required
@cross_origin()
def student(id):
    content = model.student(id)
    return jsonify(content)

@StudentBlueprint.route("/students", methods=["GET"])
@token_required
@cross_origin()
def students():
    content = model.students()
    return jsonify(content)

@StudentBlueprint.route("/update_student/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_student(id):
    content = model.update_student(
        id,                         # id
        request.json['user_id'],    # user_id
        request.json['vector'],     # vector
        request.json['regular'],    # regular
        request.json['year']        # year
    )

    return jsonify(content)

@StudentBlueprint.route("/delete_student/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_student(id):
    content = model.delete_student(id)
    return jsonify(content)
