from flask import Blueprint
from flask_cors import cross_origin

from models.UserType_model import User_Type_Model
model = User_Type_Model()

user_type_blueprint = Blueprint('/user_type_blueprint', __name__)

@user_type_blueprint.route('/create_user_type', methods=['POST'])
@cross_origin()
def create_user_type():
    return model.create_user_type()

@user_type_blueprint.route('/user_type/<id>', methods=['GET'])
@cross_origin()
def user_type(id):
    return model.user_type(id)

@user_type_blueprint.route('/user_types', methods=['GET'])
@cross_origin()
def user_types():
    return model.user_types()

@user_type_blueprint.route('/update_user_type/<id>', methods=['PUT'])
@cross_origin()
def update_user_type(id):
    return model.update_user_type(id)

@user_type_blueprint.route('/delete_user_type/<id>', methods=['DELETE'])
@cross_origin()
def delete_user_type(id):
    return model.delete_user_type(id)
