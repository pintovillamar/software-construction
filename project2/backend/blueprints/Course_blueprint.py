from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin 

from backend.models.Course_model import Course_Model
model = Course_Model()

course_blueprint = Blueprint('/courses_blueprint', __name__)

# Create a course
@course_blueprint.route('/create_course', methods=['POST'])
@cross_origin()
def create_course():
    print(request.json['cur_name'])
    print(request.json['cur_des'])
    content = model.create_course(request.json['cur_name'])    
    content = model.create_course(request.json['cur_des']) 
    return jsonify(content)

# List course with ID
@course_blueprint.route('/course/<cur_id>', methods=['POST'])
@cross_origin()
def course(cur_id):
    content = model.course(cur_id)
    return jsonify(content)

# List all courses
@course_blueprint.route('/courses', methods=['POST'])
@cross_origin()
def courses():
    content = model.courses()
    return jsonify(content)

# Update course by ID
@course_blueprint.route('/update_course/<cur_id>', methods=['POST'])
@cross_origin()
def update_course(cur_id):
    # return jsonify(model.update_teacher(int(request.json['tea_id']), request.json['name']))
    content = model.update_course(cur_id, 
                                    request.json['cur_name'], 
                                    request.json['cur_des'])
    return jsonify(content)

# Delete course by ID
@course_blueprint.route('/delete_course/<cur_id>', methods=['POST'])
@cross_origin()
def delete_course(cur_id):
    model.delete_course(cur_id)
    return f"Course {cur_id} deleted succsesfully"
