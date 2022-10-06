from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from backend.models.User_model import User_Model
model = User_Model()

user_blueprint = Blueprint('/user_blueprint', __name__)

# Create a user
@user_blueprint.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    print(request.json['usr_dni'])
    content = model.create_user(request.json['usr_dni'],
                                request.json['usr_pass'],
                                request.json['usr_photo'],
                                request.json['usr_name'],
                                request.json['usr_last_name'],
                                request.json['usr_dob'],
                                request.json['usr_email'], 
                                request.json['ust_id'])    
    return jsonify(content)

# List user with ID
@user_blueprint.route('/user/<usr_id>', methods=['POST'])
@cross_origin()
def user(usr_id):
    content = model.user(usr_id)
    return jsonify(content)

# List all users
@user_blueprint.route('/users', methods=['POST'])
@cross_origin()
def users():
    content = model.users()
    return jsonify(content)

# Update user by ID
@user_blueprint.route('/update_user/<usr_id>', methods=['POST'])
@cross_origin()
def update_user(usr_id):
    content = model.update_user(usr_id, 
                                request.json['usr_dni'],
                                request.json['usr_pass'],
                                request.json['usr_photo'],
                                request.json['usr_name'],
                                request.json['usr_last_name'],
                                request.json['usr_dob'],
                                request.json['usr_email'], 
                                request.json['ust_id'])
    return jsonify(content)

# Delete user by ID
@user_blueprint.route('/delete_user/<usr_id>', methods=['POST'])
@cross_origin()
def delete_user(usr_id):
    model.delete_user(usr_id)
    return f"User {usr_id} deleted succesfully"
