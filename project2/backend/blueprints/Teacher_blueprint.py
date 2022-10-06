import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Teacher_model import Teacher_Model
model = Teacher_Model()


teachers_blueprint = Blueprint('/teachers_blueprint', __name__)

# Create a teacher
@teachers_blueprint.route('/create_teacher', methods=['POST'])
@cross_origin()
def create_teacher():
    print(request.json['usr_id'])
    print(request.json['tea_type'])
    print(request.json['tea_cat'])
    content = model.create_teacher(request.json['usr_id'])    
    content = model.create_teacher(request.json['tea_type']) 
    content = model.create_teacher(request.json['tea_cat']) 
    return jsonify(content)

# List teacher with ID
@teachers_blueprint.route('/teacher/<tea_id>', methods=['POST'])
@cross_origin()
def teacher(tea_id):
    print(request.json['usr_id'])
    print(request.json['tea_type'])
    print(request.json['tea_cat'])
    content = model.teacher(request.json[tea_id])
    return jsonify(content)
    #return jsonify(model.teacher(int(request.json['tea_id'])))

# List all teachers
@teachers_blueprint.route('/teachers', methods=['POST'])
@cross_origin()
def teachers():
    return jsonify(model.teachers())

# Update teacher by ID
@teachers_blueprint.route('/update_teacher/<tea_id>', methods=['POST'])
@cross_origin()
def update_teacher(tea_id):
    # return jsonify(model.update_teacher(int(request.json['tea_id']), request.json['name']))
    content = model.update_teacher(request.json['usr_id'])
    content = model.update_teacher(request.json['tea_type'])
    content = model.update_teacher(request.json['tea_cat'])
    return jsonify(content)

# @teacher_blueprint.route('/delete_teacher', methods=['POST'])
# @cross_origin()
# def delete_teacher():
#     return jsonify(model.delete_teacher(int(request.json['id'])))