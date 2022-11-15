import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import requests
from backend.blueprints.external import *

from backend.models.Student_model import Student_Model
from backend.models.User_model import User
model = Student_Model()

student_blueprint = Blueprint('/student_blueprint', __name__)

# Create a student
@student_blueprint.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    usr_id = request.json['usr_id']
    std_regular = request.json['std_regular']
    std_year = request.json['std_year']
    print(usr_id)
    print(request.json['std_regular'])
    print(request.json['std_year'])
    user = User.query.get(usr_id)
    # convert to vector at creation
    url = 'http://localhost:81/openfaceAPI'
    files = {'file': open(user.usr_photo, 'rb')}
    content1 = requests.post(url, files=files)
    vector = convertToJson(content1.text)
    print(vector)
    # print(convertToJson(vector))

    # print(user.usr_id)
    # print(request.json['std_vector'])
    content = model.create_student(usr_id,
                                   std_regular,
                                   std_year,
                                   str(vector))


    return jsonify(content)

# List student with ID
@student_blueprint.route('/student/<std_id>', methods=['POST'])
@cross_origin()
def student(std_id):
    content = model.student(std_id)
    return jsonify(content)

# List all students
@student_blueprint.route('/students', methods=['POST'])
@cross_origin()
def students():
    content = model.students()
    return jsonify(content)

# Update student by ID
@student_blueprint.route('/update_student/<std_id>', methods=['POST'])
@cross_origin()
def update_student(std_id):
    usr_id = request.json['usr_id']
    user = User.query.get(usr_id)
    url = 'http://localhost:81/openfaceAPI'
    files = {'file': open(user.usr_photo, 'rb')}
    content1 = requests.post(url, files=files)
    vector = content1.text
    print(vector)

    content = model.update_student(std_id, 
                                    usr_id,
                                    request.json['std_regular'],
                                    request.json['std_year'],
                                    vector)
    return jsonify(content)

# Delete student by ID
@student_blueprint.route('/delete_student/<std_id>', methods=['POST'])
@cross_origin()
def delete_student(std_id):
    model.delete_student(std_id)
    return f"Student {std_id} deleted succsesfully"

# test func
@student_blueprint.route('/face_student/<std_id>', methods=['POST'])
@cross_origin()
def face_student(std_id):
    content = model.face_student(std_id)
    # path_photo = model.face_student(std_id)
    # f = request.files['file']
    # filename = f.filename
    # path_v = content
    # print(path_photo)
    return content.json()

# @student_blueprint.route('/convert_image_vector/<std_id>', methods=['POST'])
# @cross_origin()
# def convert_image_vector(std_id):
#     content = model.convert_image_vector(std_id)
#     return jsonify(content)

@student_blueprint.route('/get_student_path/<std_id>', methods=['POST'])
@cross_origin()
def get_student_path(std_id):
    content = model.get_student_path(std_id)
    return jsonify(content)
