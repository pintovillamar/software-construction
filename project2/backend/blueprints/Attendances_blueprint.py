import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin 

from backend.models.Attendance_model import Attendance_Model
model = Attendance_Model()

attendace_blueprint = Blueprint('/attendaces_blueprint', __name__)

# Create a attendace
@attendace_blueprint.route('/create_attendace', methods=['POST'])
@cross_origin()
def create_attendace():
    print(request.json['att_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['att_val'])
    content = model.create_attendace(request.json['att_date'])
    content = model.create_attendace(request.json['gru_id'])    
    content = model.create_attendace(request.json['std_id'])
    content = model.create_attendace(request.json['att_val'])    
    return jsonify(content)

# List attendace with ID
@attendace_blueprint.route('/attendace/<att_id>', methods=['POST'])
@cross_origin()
def attendace(att_id):
    content = model.attendace(att_id)
    return jsonify(content)

# List all attendaces
@attendace_blueprint.route('/attendaces', methods=['POST'])
@cross_origin()
def attendaces():
    content = model.attendaces()
    return jsonify(content)

# Update attendace by ID
@attendace_blueprint.route('/update_attendace/<att_id>', methods=['POST'])
@cross_origin()
def update_attendace(att_id):

    content = model.update_attendace(att_id,
                                            request.json['att_date'],
                                            request.json['gru_id'],
                                            request.json['std_id'],
                                            request.json['att_val'])
    return jsonify(content)

# Delete attendace by ID
@attendace_blueprint.route('/delete_attendace/<att_id>', methods=['POST'])
@cross_origin()
def delete_attendace(att_id):
    model.delete_attendace(att_id)
    return f"Attendace {att_id} deleted succsesfully"