from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from models.User_model import User_Model
model = User_Model()

user_blueprint = Blueprint('/user_blueprint', __name__)

@user_blueprint.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    return model.create_user()

@user_blueprint.route('/user/<id>', methods=['GET'])
@cross_origin()
def user(id):
    return model.user(id)

@user_blueprint.route('/users', methods=['GET'])
@cross_origin()
def users():
    return model.users()

@user_blueprint.route('/update_user/<id>', methods=['PUT'])
@cross_origin()
def update_user(id):
    return model.update_user(id)

@user_blueprint.route('/delete_user/<id>', methods=['DELETE'])
@cross_origin()
def delete_user(id):
    return model.delete_user(id)
