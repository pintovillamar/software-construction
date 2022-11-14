from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Participation_model import ParticipationModel, Participation

from auth.auth_jwt import validate_token

model = ParticipationModel()

ParticipationBlueprint = Blueprint("ParticipationBlueprint", __name__)

# BEFORE REQUEST PARA AUTH
@ParticipationBlueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@ParticipationBlueprint.route("/create_participation", methods=["POST"])
# # @token_required
@cross_origin()
def create_participation():

    date = request.json["date"]
    group_id = request.json["group_id"]
    student_id = request.json["student_id"]
    valor = request.json["valor"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_participation(date, group_id, student_id, valor, created_at, updated_at))

@ParticipationBlueprint.route("/participation/<id>", methods=["GET"])
# @token_required
@cross_origin()
def participation(id):
    content = model.participation(id)
    return jsonify(content)

@ParticipationBlueprint.route("/participations", methods=["GET"])
@cross_origin()
def participations():
    content = model.participations()
    return jsonify(content)
    
@ParticipationBlueprint.route("/update_participation/<id>", methods=["PUT"])
# @token_required
@cross_origin()
def update_participation(id):

    participation_created = Participation.query.get(id)
    date = request.json["date"]
    group_id = request.json["group_id"]
    student_id = request.json["student_id"]
    valor = request.json["valor"]
    created_at = participation_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_participation(id, date, group_id, student_id, valor,created_at ,updated_at))


@ParticipationBlueprint.route("/delete_participation/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_participation(id):
    return jsonify(model.delete_participation(id))