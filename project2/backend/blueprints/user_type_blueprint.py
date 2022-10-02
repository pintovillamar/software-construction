from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.user_type_model import UserTypeModel
model = UserTypeModel()


user_type_blueprint = Blueprint('/user_type_blueprint', __name__)

@user_type_blueprint.route('/create_user_type', methods=['POST'])
@cross_origin()
def create_user_type():
    content = model.create_user_type(request.json['ust_name'])    
    return jsonify(content)

# @user_type_blueprint.route('/delete_user_type', methods=['POST'])
# @cross_origin()
# def delete_user_type():
#     return jsonify(model.delete_user_type(int(request.json['id'])))

# Get user_type by id
@user_type_blueprint.route('/user_type/', methods=['POST'])
@cross_origin()
def user_type():
    return jsonify(model.user_type(int(request.json['ust_id'])))

# Gets all user_types
@user_type_blueprint.route('/user_types', methods=['POST'])
@cross_origin()
def user_types():
    return jsonify(model.user_types())

# @user_type_blueprint.route('/update_user_type', methods=['POST'])
# @cross_origin()
# def update_user_type():
#     return jsonify(model.update_user_type(int(request.json['id']), request.json['name']))
