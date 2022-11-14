from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Attendance_model import AttendanceModel, Attendance

from auth.auth_jwt import validate_token

model = AttendanceModel()

AttendanceBlueprint = Blueprint("AttendanceBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@AttendanceBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@AttendanceBlueprint.route("/create_attendance", methods=["POST"])
# # @token_required
@cross_origin()
def create_attendance():

    date = request.json["date"]
    group_id = request.json["group_id"]
    student_id = request.json["student_id"]
    valor = request.json["valor"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_attendance(date, group_id, student_id, valor, created_at, updated_at))

@AttendanceBlueprint.route("/attendance/<id>", methods=["GET"])
# @token_required
@cross_origin()
def attendance(id):
    content = model.attendance(id)
    return jsonify(content)

@AttendanceBlueprint.route("/attendances", methods=["GET"])
@cross_origin()
def attendances():
    content = model.attendances()
    return jsonify(content)
    
@AttendanceBlueprint.route("/update_attendance/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_attendance(id):

    attendance_created = Attendance.query.get(id)
    date = request.json["date"]
    group_id = request.json["group_id"]
    student_id = request.json["student_id"]
    valor = request.json["valor"]
    created_at = attendance_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_attendance(id, date, group_id, student_id, valor,created_at ,updated_at))


@AttendanceBlueprint.route("/delete_attendance/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_attendance(id):
    return jsonify(model.delete_attendance(id))