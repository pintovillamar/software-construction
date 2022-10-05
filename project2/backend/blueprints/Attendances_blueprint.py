import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Attendaces_Model import Attendaces_Model
model = Attendaces_Model()

attendaces_blueprint = Blueprint('/attendaces_blueprint', __name__)

# Create a attendace
@attendaces_blueprint.route('/create_attendaces', methods=['POST'])
@cross_origin()
def create_attendaces():
    print(request.json['att_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['att_val'])
    content = model.create_attendaces(request.json['att_date'])
    content = model.create_attendaces(request.json['gru_id'])    
    content = model.create_attendaces(request.json['std_id'])
    content = model.create_attendaces(request.json['att_val'])    
    return jsonify(content)

# List attendace with ID
@attendaces_blueprint.route('/attendace/<att_id>', methods=['POST'])
@cross_origin()
def attendace(att_id):
    print(request.json['att_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['att_val'])
    content = model.attendace(request.json[att_id])
    return jsonify(content)
    #return jsonify(model.attendace(int(request.json['att_id'])))

# List all attendaces
@attendaces_blueprint.route('/attendaces', methods=['POST'])
@cross_origin()
def attendaces():
    return jsonify(model.attendaces())

# Update attendace by ID
@attendaces_blueprint.route('/update_attendace/<att_id>', methods=['POST'])
@cross_origin()
def update_attendace(att_id):
    # return jsonify(model.update_attendace(int(request.json['att_id']), request.json['name']))
    content = model.update_attendace(request.json['att_date'])
    content = model.update_attendace(request.json['gru_id'])
    content = model.update_attendace(request.json['std_id'])
    content = model.update_attendace(request.json['att_val'])
    return jsonify(content)

# @attendace_blueprint.route('/delete_attendace', methods=['POST'])
# @cross_origin()
# def delete_attendace():
#     return jsonify(model.delete_attendace(int(request.json['id'])))