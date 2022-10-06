import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Course_model import Course_Model
model = Course_Model()


courses_blueprint = Blueprint('/courses_blueprint', __name__)

# Create a course
@courses_blueprint.route('/create_course', methods=['POST'])
@cross_origin()
def create_course():
    print(request.json['cur_name'])
    print(request.json['cur_des'])
    content = model.create_course(request.json['cur_name'])    
    content = model.create_course(request.json['cur_des']) 
    return jsonify(content)

# List course with ID
@courses_blueprint.route('/course/<cur_id>', methods=['POST'])
@cross_origin()
def course(cur_id):
    print(request.json['cur_name'])
    print(request.json['cur_des'])
    content = model.course(request.json[cur_id])
    return jsonify(content)
    #return jsonify(model.course(int(request.json['cur_id'])))

# List all courses
@courses_blueprint.route('/courses', methods=['POST'])
@cross_origin()
def courses():
    return jsonify(model.courses())

# Update course.route('/update_course/<cur_id>', methods=['POST'])
@cross_origin()
def update_course(cur_id):
    # return jsonify(model.update_teacher(int(request.json['tea_id']), request.json['name']))
    content = model.update_teacher(request.json['cur_name'])
    content = model.update_teacher(request.json['cur_des'])
    return jsonify(content)

# @course_blueprint.route('/delete_course', methods=['POST'])
# @cross_origin()
# def delete_course():
#     return jsonify(model.delete_course(int(request.json['id'])))