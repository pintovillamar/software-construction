from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from models.Group_model import Group_Model
model = Group_Model()

group_blueprint = Blueprint('/group_blueprint', __name__)

@group_blueprint.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    return model.create_group()

@group_blueprint.route('/group/<id>', methods=['GET'])
@cross_origin()
def group(id):
    return model.group(id)

@group_blueprint.route('/groups', methods=['GET'])
@cross_origin()
def groups():
    return model.groups()

@group_blueprint.route('/update_group/<id>', methods=['PUT'])
@cross_origin()
def update_group(id):
    return model.update_group(id)

@group_blueprint.route('/delete_group/<id>', methods=['DELETE'])
@cross_origin()
def delete_group(id):
    return model.delete_group(id)
