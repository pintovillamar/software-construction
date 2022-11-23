from flask import Blueprint
from flask_cors import cross_origin

from models.Course_model import Course_Model
model = Course_Model()

course_blueprint = Blueprint('/course_blueprint', __name__)

@course_blueprint.route('/create_course', methods=['POST'])
@cross_origin()
def create_course():
    return model.create_course()

@course_blueprint.route('/course/<id>', methods=['GET'])
@cross_origin()
def course(id):
    return model.course(id)

@course_blueprint.route('/courses', methods=['GET'])
@cross_origin()
def courses():
    return model.courses()

@course_blueprint.route('/update_course/<id>', methods=['PUT'])
@cross_origin()
def update_course(id):
    return model.update_course(id)

@course_blueprint.route('/delete_course/<id>', methods=['DELETE'])
@cross_origin()
def delete_course(id):
    return model.delete_course(id)

@course_blueprint.route('/get_course_combobox', methods=['GET'])
@cross_origin()
def get_course_combobox():
    return model.get_course_combobox()
