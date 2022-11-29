from flask import Blueprint
from flask_cors import cross_origin

from models.Student_model import Student_Model
model = Student_Model()

student_blueprint = Blueprint('/student_blueprint', __name__)

@student_blueprint.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    return model.create_student()

@student_blueprint.route('/student/<id>', methods=['GET'])
@cross_origin()
def student(id):
    return model.student(id)

@student_blueprint.route('/students', methods=['GET'])
@cross_origin()
def students():
    return model.students()

@student_blueprint.route('/update_student/<id>', methods=['PUT'])
@cross_origin()
def update_student(id):
    return model.update_student(id)

@student_blueprint.route('/delete_student/<id>', methods=['DELETE'])
@cross_origin()
def delete_student(id):
    return model.delete_student(id)

