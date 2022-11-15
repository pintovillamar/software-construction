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

from models.Schedulle_model import SchedulleModel, Schedulle

from models.User_model import User

model = SchedulleModel()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


SchedulleBlueprint = Blueprint("SchedulleBlueprint", __name__)

# Login 
@SchedulleBlueprint.route("/login", methods=["GET"])
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

@SchedulleBlueprint.route("/create_schedulle", methods=["POST"])
@token_required
@cross_origin()
def create_schedulle():
    f = request.files['file']
    filename = secure_filename(f.filename)
    # path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + filename
    
    data = json.loads(request.form.get('data'))

    content = model.create_schedulle(
        data["begin"],              # begin
        data["end"],                # end
        data["day"],                # day
        data["group_id"],           # group_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    updated = rename_pic(Schedulle.query.get(content["id"]).id)

    content = model.update_schedulle(
        content["id"],              # id
        data["begin"],              # begin
        data["end"],                # end
        data["day"],                # day
        data["group_id"],           # group_id
        datetime.now(),             # created_at
        datetime.now()              # updated_at
    )

    f.save(updated + filename)

    return jsonify(content)

@SchedulleBlueprint.route("/schedulle/<id>", methods=["GET"])
@token_required
@cross_origin()
def schedulle(id):
    content = model.schedulle(id)
    return jsonify(content)

@SchedulleBlueprint.route("/schedulles", methods=["GET"])
@token_required
@cross_origin()
def schedulles():
    content = model.schedulles()
    return jsonify(content)

@SchedulleBlueprint.route("/update_schedulle/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_schedulle(id):
    schedulle_created = Schedulle.query.get(id)

    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))

    content = model.update_schedulle(
        id,                           # id
        data["begin"],                # begin
        data["end"],                  # end
        data["day"],                  # day
        data["group_id"],             # group_id
        schedulle_created.created_at, # created_at
        datetime.now()                # updated_at
    )

    f.save(updated)

    return jsonify(model.update_schedulle(content))

@SchedulleBlueprint.route("/delete_schedulle/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_schedulle(id):
    return jsonify(model.delete_schedulle(id))

def rename_pic(id):
    schedulle_id = id
    schedulle_id = Schedulle.query.get(schedulle_id).id
    begin = Schedulle.query.get(schedulle_id).begin
    end = Schedulle.query.get(schedulle_id).end
    day = Schedulle.query.get(schedulle_id).day
    group_id = Schedulle.query.get(schedulle_id).group_id

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_inf_schedulle = path +str(schedulle_id)+"_"+begin+"_"+end+"_"+day+"-"+group_id+"-"
    return new_inf_schedulle
