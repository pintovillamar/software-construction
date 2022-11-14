from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import requests

from external import convertToJson

from datetime import datetime

from models.Student_model import StudentModel
from models.User_model import User

model = StudentModel()

StudentBlueprint = Blueprint("StudentBlueprint", __name__)

@StudentBlueprint.route("/create_student", methods=["POST"])
@cross_origin()
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
@cross_origin()
def student(id):
    content = model.student(id)
    return jsonify(content)

@StudentBlueprint.route("/students", methods=["GET"])
@cross_origin()
def students():
    content = model.students()
    return jsonify(content)

@StudentBlueprint.route("/update_student/<id>", methods=["PUT"])
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
@cross_origin()
def delete_student(id):
    content = model.delete_student(id)
    return jsonify(content)
