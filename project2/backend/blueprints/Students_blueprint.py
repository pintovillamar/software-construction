import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Students_Model import Students_Model
model = Students_Model()

students_blueprint = Blueprint('/students_blueprint', __name__)

# Create a student
@students_blueprint.route('/create_students', methods=['POST'])
@cross_origin()
def create_students():
    print(request.json['usr_id'])
    print(request.json['std_regular'])
    print(request.json['std_year'])
    content = model.create_students(request.json['usr_id'])
    content = model.create_students(request.json['std_regular'])    
    content = model.create_students(request.json['std_year'])    
    return jsonify(content)

# List student with ID
@students_blueprint.route('/student/<std_id>', methods=['POST'])
@cross_origin()
def student(std_id):
    print(request.json['usr_id'])
    print(request.json['std_regular'])
    print(request.json['std_year'])
    content = model.student(request.json[std_id])
    return jsonify(content)
    #return jsonify(model.student(int(request.json['std_id'])))

# List all students
@students_blueprint.route('/students', methods=['POST'])
@cross_origin()
def students():
    return jsonify(model.students())

# Update student by ID
@students_blueprint.route('/update_student/<std_id>', methods=['POST'])
@cross_origin()
def update_student(std_id):
    # return jsonify(model.update_student(int(request.json['std_id']), request.json['name']))
    content = model.update_student(request.json['usr_id'])
    content = model.update_student(request.json['std_regular'])
    content = model.update_student(request.json['std_year'])
    return jsonify(content)

# @student_blueprint.route('/delete_student', methods=['POST'])
# @cross_origin()
# def delete_student():
#     return jsonify(model.delete_student(int(request.json['id'])))