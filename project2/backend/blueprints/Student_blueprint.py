import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin 

from backend.models.Student_model import Student_Model
model = Student_Model()

student_blueprint = Blueprint('/students_blueprint', __name__)

# Create a student
@student_blueprint.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    print(request.json['usr_id'])
    print(request.json['std_regular'])
    print(request.json['std_year'])
    content = model.create_student(request.json['usr_id'])
    content = model.create_student(request.json['std_regular'])    
    content = model.create_student(request.json['std_year'])    
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
    content = model.student()
    return jsonify(content)

# Update student by ID
@student_blueprint.route('/update_student/<std_id>', methods=['POST'])
@cross_origin()
def update_student(std_id):
    
    content = model.update_student(std_id, 
                                    request.json['usr_id'],
                                    request.json['std_regular'],
                                    request.json['std_year'])
    return jsonify(content)

@student_blueprint.route('/delete_student/<std_id>', methods=['POST'])
@cross_origin()
def delete_student(std_id):
    model.delete_student(std_id)
    return f"Student {std_id} deleted succsesfully"