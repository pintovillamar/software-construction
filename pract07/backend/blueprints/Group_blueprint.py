from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin 

from backend.models.Group_model import Group_Model
model = Group_Model()


group_blueprint = Blueprint('/groups_blueprint', __name__)

# Create a group
@group_blueprint.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    print(request.json['tea_id'])
    print(request.json['gru_name'])
    print(request.json['cur_id'])
    content = model.create_group(request.json['tea_id'],
                                 request.json['gru_name'],
                                 request.json['cur_id'])    
 
    return jsonify(content)

# List group with ID
@group_blueprint.route('/group/<gru_id>', methods=['POST'])
@cross_origin()
def group(gru_id):
    content = model.group(gru_id)
    return jsonify(content)
    
# List all groups
@group_blueprint.route('/groups', methods=['POST'])
@cross_origin()
def groups():
    content = model.groups()
    return jsonify(content)

# Update group by ID
@group_blueprint.route('/update_group/<gru_id>', methods=['POST'])
@cross_origin()
def update_group(gru_id):
    content = model.update_group(gru_id, 
                                    request.json['tea_id'],
                                    request.json['gru_name'],
                                    request.json['cur_id'])
    return jsonify(content)

# Delete group by ID
@group_blueprint.route('/delete_group/<gru_id>', methods=['POST'])
@cross_origin()
def delete_group(gru_id):
    model.delete_group(gru_id)
    return f"Group {gru_id} deleted succsesfully"