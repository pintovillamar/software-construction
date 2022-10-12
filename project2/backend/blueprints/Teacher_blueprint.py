from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin 

from backend.models.Teacher_model import Teacher_Model
model = Teacher_Model()


teacher_blueprint = Blueprint('/teachers_blueprint', __name__)

# Create a teacher
@teacher_blueprint.route('/create_teacher', methods=['POST'])
@cross_origin()
def create_teacher():
    print(request.json['usr_id'])
    print(request.json['tea_type'])
    print(request.json['tea_cat'])
    content = model.create_teacher(request.json['usr_id'],
                                   request.json['tea_type'],
                                   request.json['tea_cat'])     
    return jsonify(content)

# List teacher with ID
@teacher_blueprint.route('/teacher/<tea_id>', methods=['POST'])
@cross_origin()
def teacher(tea_id):
    content = model.teacher(tea_id)
    return jsonify(content)
    
# List all teachers
@teacher_blueprint.route('/teachers', methods=['POST'])
@cross_origin()
def teachers():
    content = model.teachers()
    return jsonify(content)

# Update teacher by ID
@teacher_blueprint.route('/update_teacher/<tea_id>', methods=['POST'])
@cross_origin()
def update_teacher(tea_id):
    content = model.update_teacher(tea_id, 
                                    request.json['usr_id'],
                                    request.json['tea_type'],
                                    request.json['tea_cat'])
    return jsonify(content)

# Delete teacher by ID
@teacher_blueprint.route('/delete_teacher/<tea_id>', methods=['POST'])
@cross_origin()
def delete_teacher(tea_id):
    model.delete_teacher(tea_id)
    return f"Teacher {tea_id} deleted succsesfully"