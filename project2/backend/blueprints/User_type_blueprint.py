from flask import Blueprint
from flask import request
from flask import jsonify
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
    content = model.user_type(ust_id)
    return jsonify(content)

# List all user types
@user_type_blueprint.route('/user_types', methods=['POST'])
@cross_origin()
def user_types():
    content = model.user_types()
    return jsonify(content)

# Update usertype by ID
@user_type_blueprint.route('/update_user_type/<ust_id>', methods=['POST'])
@cross_origin()
def update_user_type(ust_id):
    content = model.update_user_type(ust_id, request.json['ust_name'])
    return jsonify(content)

# Delete user type by ID
@user_type_blueprint.route('/delete_user_type/<ust_id>', methods=['POST'])
@cross_origin()
def delete_user_type(ust_id):
    model.delete_user_type(ust_id)
    return f"User type {ust_id} deleted succesfully" 