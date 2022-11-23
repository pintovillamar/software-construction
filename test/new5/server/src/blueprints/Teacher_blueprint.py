from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from models.Teacher_model import Teacher_Model
model = Teacher_Model()

teacher_blueprint = Blueprint('/teacher_blueprint', __name__)

@teacher_blueprint.route('/create_teacher', methods=['POST'])
@cross_origin()
def create_teacher():
    return model.create_teacher()

@teacher_blueprint.route('/teacher/<id>', methods=['GET'])
@cross_origin()
def teacher(id):
    return model.teacher(id)

@teacher_blueprint.route('/teachers', methods=['GET'])
@cross_origin()
def teachers():
    return model.teachers()

@teacher_blueprint.route('/update_teacher/<id>', methods=['PUT'])
@cross_origin()
def update_teacher(id):
    return model.update_teacher(id)

@teacher_blueprint.route('/delete_teacher/<id>', methods=['DELETE'])
@cross_origin()
def delete_teacher(id):
    return model.delete_teacher(id)

@teacher_blueprint.route('/get_teacher_combobox/<id>', methods=['GET'])
@cross_origin()
def get_teacher_combobox(id):
    return model.get_teacher_combobox(id)
