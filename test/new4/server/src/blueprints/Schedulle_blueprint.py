from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Schedulle_model import SchedulleModel, Schedulle

from auth.auth_jwt import validate_token

model = SchedulleModel()

SchedulleBlueprint = Blueprint("SchedulleBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@SchedulleBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@SchedulleBlueprint.route("/create_schedulle", methods=["POST"])
# @token_required
@cross_origin()
def create_schedulle():
    begin = request.json["begin"]
    end = request.json["end"]
    day = request.json["day"]
    group_id = request.json["group_id"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_schedulle(begin, end, day, group_id, created_at, updated_at))

@SchedulleBlueprint.route("/schedulle/<id>", methods=["GET"])
# @token_required
@cross_origin()
def schedulle(id):
    content = model.schedulle(id)
    return jsonify(content)

@SchedulleBlueprint.route("/schedulles", methods=["GET"])
@cross_origin()
def schedulles():
    content = model.schedulles()
    return jsonify(content)

@SchedulleBlueprint.route("/update_schedulle/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_schedulle(id):
    schedulle_created = Schedulle.query.get(id)
    begin = request.json["begin"]
    end = request.json["end"]
    day = request.json["day"]
    group_id = request.json["group_id"]
    created_at = schedulle_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_schedulle(id, begin, end, day, group_id, created_at ,updated_at))

@SchedulleBlueprint.route("/delete_schedulle/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_schedulle(id):
    return jsonify(model.delete_schedulle(id))
