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

# Create a user type
@students_blueprint.route('/create_students', methods=['POST'])
@cross_origin()
def create_students():
    print(request.json['std_regular'])
    content = model.create_students(request.json['std_regular'])    
    return jsonify(content)