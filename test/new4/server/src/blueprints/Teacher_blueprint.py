from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Teacher_model import TeacherModel, Teacher

from auth.auth_jwt import validate_token

model = TeacherModel()

TeacherBlueprint = Blueprint("TeacherBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@TeacherBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@TeacherBlueprint.route("/create_teacher", methods=["POST"])
# @token_required
@cross_origin()
def create_teacher():
    user_id = request.json["user_id"]
    type = request.json["type"]
    cat = request.json["cat"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_user_type(user_id, type, cat, created_at, updated_at))

@TeacherBlueprint.route("/teacher/<id>", methods=["GET"])
# @token_required
@cross_origin()
def teacher(id):
    content = model.teacher(id)
    return jsonify(content)

@TeacherBlueprint.route("/teachers", methods=["GET"])
@cross_origin()
def teachers():
    content = model.teachers()
    return jsonify(content)

@TeacherBlueprint.route("/update_teacher/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_teacher(id):
    teacher_created = Teacher.query.get(id)
    user_id = request.json["user_id"]
    type = request.json["type"]
    cat = request.json["cat"]
    created_at = teacher_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_user_type(id, user_id, type, cat, created_at ,updated_at))

@TeacherBlueprint.route("/delete_teacher/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_teacher(id):
    return jsonify(model.delete_teacher(id))
