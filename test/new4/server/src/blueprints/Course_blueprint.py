from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Course_model import CourseModel, Course

from auth.auth_jwt import validate_token

model = CourseModel()

CourseBlueprint = Blueprint("CourseBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@CourseBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@CourseBlueprint.route("/create_course", methods=["POST"])
# @token_required
@cross_origin()
def create_course():
    name = request.json["name"]
    des = request.json["des"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_course(name, des, created_at, updated_at))

@CourseBlueprint.route("/course/<id>", methods=["GET"])
# @token_required
@cross_origin()
def course(id):
    content = model.course(id)
    return jsonify(content)

@CourseBlueprint.route("/courses", methods=["GET"])
@cross_origin()
def courses():
    content = model.courses()
    return jsonify(content)

@CourseBlueprint.route("/update_course/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_course(id):
    course_created = Course.query.get(id)
    name = request.json["name"]
    des = request.json["des"]
    created_at = course_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_course(id, name, des, created_at ,updated_at))

@CourseBlueprint.route("/delete_course/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_course(id):
    return jsonify(model.delete_course(id))
