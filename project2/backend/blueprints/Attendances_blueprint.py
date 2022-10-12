import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin 

from backend.models.Attendance_model import Attendance_Model
model = Attendance_Model()

attendance_blueprint = Blueprint('/attendances_blueprint', __name__)

# Create a attendace
@attendance_blueprint.route('/create_attendance', methods=['POST'])
@cross_origin()
def create_attendance():
    print(request.json['att_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['att_val'])
    content = model.create_attendance(request.json['att_date'],
                                    request.json['gru_id'],
                                    request.json['std_id'],
                                    request.json['att_val'])
    return jsonify(content)

# List attendace with ID
@attendance_blueprint.route('/attendance/<att_id>', methods=['POST'])
@cross_origin()
def attendance(att_id):
    content = model.attendance(att_id)
    return jsonify(content)

# List all attendances
@attendance_blueprint.route('/attendances', methods=['POST'])
@cross_origin()
def attendances():
    content = model.attendances()
    return jsonify(content)

# Update attendace by ID
@attendance_blueprint.route('/update_attendance/<att_id>', methods=['POST'])
@cross_origin()
def update_attendance(att_id):

    content = model.update_attendance(att_id,
                                            request.json['att_date'],
                                            request.json['gru_id'],
                                            request.json['std_id'],
                                            request.json['att_val'])
    return jsonify(content)

# Delete attendance by ID
@attendance_blueprint.route('/delete_attendance/<att_id>', methods=['POST'])
@cross_origin()
def delete_attendance(att_id):
    model.delete_attendance(att_id)
    return f"Attendace {att_id} deleted succsesfully"