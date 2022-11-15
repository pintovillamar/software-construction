from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Group_model import GroupModel, Group

from auth.auth_jwt import validate_token

model = GroupModel()

GroupBlueprint = Blueprint("GroupBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@GroupBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@GroupBlueprint.route("/create_group", methods=["POST"])
# @token_required
@cross_origin()
def create_group():
    teacher_id = request.json["teacher_id"]
    name = request.json["name"]
    course_id = request.json["course_id"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_group(teacher_id, name, course_id, created_at, updated_at))

@GroupBlueprint.route("/group/<id>", methods=["GET"])
# @token_required
@cross_origin()
def group(id):
    content = model.group(id)
    return jsonify(content)

@GroupBlueprint.route("/groups", methods=["GET"])
@cross_origin()
def groups():
    content = model.groups()
    return jsonify(content)

@GroupBlueprint.route("/update_group/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_group(id):
    group_created = Group.query.get(id)
    teacher_id = request.json["teacher_id"]
    name = request.json["name"]
    course_id = request.json["course_id"]
    created_at = group_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_group(id, teacher_id, name, course_id, created_at ,updated_at))

@GroupBlueprint.route("/delete_group/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_group(id):
    return jsonify(model.delete_group(id))
