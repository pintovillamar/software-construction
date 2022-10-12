import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin 

from backend.models.Student_model import Student_Model
model = Student_Model()

student_blueprint = Blueprint('/student_blueprint', __name__)

# Create a student
@student_blueprint.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    print(request.json['usr_id'])
    print(request.json['std_regular'])
    print(request.json['std_year'])
    print(request.json['std_vector'])
    content = model.create_student(request.json['usr_id'],
                                   request.json['std_regular'],
                                   request.json['std_year'],
                                   request.json['std_vector'])
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
    
    content = model.update_student(std_id, 
                                    request.json['usr_id'],
                                    request.json['std_regular'],
                                    request.json['std_year'],
                                    request.json['std_vector'])
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
    path_photo = model.face_student(std_id)
    f = request.files['file']
    filename = f.filename
    path_v = content
    print(path_photo)
    return path_v

# @student_blueprint.route('/convert_image_vector/<std_id>', methods=['POST'])
# @cross_origin()
# def convert_image_vector(std_id):
#     content = model.convert_image_vector(std_id)
#     return jsonify(content)
