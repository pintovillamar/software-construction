import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.User_type_model import User_Type_Model
model = User_Type_Model()


user_type_blueprint = Blueprint('/user_types_blueprint', __name__)

# Create a user type
@user_type_blueprint.route('/create_user_type', methods=['POST'])
@cross_origin()
def create_user_type():
    print(request.json['ust_name'])
    content = model.create_user_type(request.json['ust_name'])    
    return jsonify(content)

# List user type with ID
@user_type_blueprint.route('/user_type/<ust_id>', methods=['POST'])
@cross_origin()
def user_type(ust_id):
    print(request.json['ust_id'])
    content = model.user_type(request.json['ust_id'])
    return jsonify(content)
    #return jsonify(model.user_type(int(request.json['ust_id'])))

# List all user types
@user_type_blueprint.route('/user_types', methods=['POST'])
@cross_origin()
def user_types():
    # return jsonify(model.user_types())
    content = model.user_types()
    return jsonify(content)

# Update usertype by ID
@user_type_blueprint.route('/update_user_type/<ust_id>', methods=['POST'])
@cross_origin()
def update_user_type(ust_id):
    # return jsonify(model.update_user_type(int(request.json['ust_id']), request.json['name']))
    return jsonify(model.update_user_type(request.json['ust_name']))

# @user_type_blueprint.route('/delete_user_type', methods=['POST'])
# @cross_origin()
# def delete_user_type():
#     return jsonify(model.delete_user_type(int(request.json['id'])))