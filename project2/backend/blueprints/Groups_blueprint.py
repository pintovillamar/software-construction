import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Groups_model import Groups_Model
model = Groups_Model()


groups_blueprint = Blueprint('/groups_blueprint', __name__)

# Create a group
@groups_blueprint.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    print(request.json['tea_id'])
    print(request.json['gru_name'])
    print(request.json['cur_id'])
    content = model.create_group(request.json['tea_id'])    
    content = model.create_group(request.json['gru_name']) 
    content = model.create_group(request.json['cur_id']) 
    return jsonify(content)

# List group with ID
@groups_blueprint.route('/group/<gru_id>', methods=['POST'])
@cross_origin()
def group(gru_id):
    print(request.json['tea_id'])
    print(request.json['gru_name'])
    print(request.json['cur_id'])
    content = model.group(request.json[gru_id])
    return jsonify(content)
    #return jsonify(model.group(int(request.json['gru_id'])))

# List all groups
@groups_blueprint.route('/groups', methods=['POST'])
@cross_origin()
def groups():
    return jsonify(model.groups())

# Update group by ID
@groups_blueprint.route('/update_group/<gru_id>', methods=['POST'])
@cross_origin()
def update_group(gru_id):
    # return jsonify(model.update_group(int(request.json['gru_id']), request.json['name']))
    content = model.update_group(request.json['tea_id'])
    content = model.update_group(request.json['gru_name'])
    content = model.update_group(request.json['cur_id'])
    return jsonify(content)

# @group_blueprint.route('/delete_group', methods=['POST'])
# @cross_origin()
# def delete_group():
#     return jsonify(model.delete_group(int(request.json['id'])))