from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from conn import app

import json

import jwt
from functools import wraps

from datetime import datetime, timedelta

from models.Participation_model import ParticipationModel, Participation

from models.User_model import User

model = ParticipationModel()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["id"]).first()
            print(current_user)
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated

ParticipationBlueprint = Blueprint("ParticipationBlueprint", __name__)

@ParticipationBlueprint.route("/login", methods=["GET"])
@cross_origin()
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})
    
    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})

    if user.password == auth.password:
        token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(minutes = 30)}, app.config["SECRET_KEY"])
        
        return jsonify({'token': token})
    
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm: "login required!"'})

@ParticipationBlueprint.route("/create_participation", methods=["POST"])
@token_required
@cross_origin()
def create_participation():
    f = request.files['file']
    filename = secure_filename(f.filename)
    data = json.loads(request.form.get('data'))

    content = model.create_participation(
        data["date"],
        data["group_id"],
        data["student_id"],
        data,["valor"],
        datetime.now(),
        datetime.now()
    )

    updated = rename_pic(Participation.query.get(content["id"]).id)

    content = model.update_participation(
        content["id"],
        data["date"],
        data["group_id"],
        data["student_id"],
        data,["valor"],
        datetime.now(),
        datetime.now()
    )
    f.save(updated + filename)

    return jsonify(content)

@ParticipationBlueprint.route("/participation/<id>", methods=["GET"])
@token_required
@cross_origin()
def participation(id):
    content = model.participation(id)
    return jsonify(content)

@ParticipationBlueprint.route("/participations", methods=["GET"])
@token_required
@cross_origin()
def participations():
    content = model.participations()
    return jsonify(content)
    
@ParticipationBlueprint.route("/update_participation/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_participation(id):

    participation_created = Participation.query.get(id)
    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))
    content = model.update_participation(
        id,
        data["date"],
        data["group_id"],
        data["student_id"],
        data,["valor"],
        participation_created.created_at,
        datetime.now()
    )

@ParticipationBlueprint.route("/delete_participation/<id>", methods=["DELETE"])
# @token_required
@cross_origin()
def delete_participation(id):
    return jsonify(model.delete_participation(id))

def rename_pic(id):
    participation_id = id
    participation_id = Participation.query.get(participation_id).id
    date = Participation.query.get(participation_id).date
    group_id = Participation.query.get(participation_id).group_id
    student_id = Participation.query.get(participation_id).student_id
    valor = Participation.query.get(participation_id).valor

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_type_participation = path +str(participation_id)+"_"+date+"_"+group_id+"_"+student_id+"-"+group_id+"-"
    return new_type_participation