from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from datetime import datetime

from models.UserType_model import UserTypeModel, UserType
model = UserTypeModel()

UserTypeBlueprint = Blueprint("UserTypeBlueprint", __name__)

@UserTypeBlueprint.route("/create_user_type", methods=["POST"])
@cross_origin()
def create_user_type():
    name = request.json["name"]
    description = request.json["description"]
    created_at = datetime.now()
    updated_at = datetime.now()
    return jsonify(model.create_user_type(name, description, created_at, updated_at))

@UserTypeBlueprint.route("/user_type/<id>", methods=["GET"])
@cross_origin()
def user_type(id):
    content = model.user_type(id)
    return jsonify(content)

@UserTypeBlueprint.route("/user_types", methods=["GET"])
@cross_origin()
def user_types():
    content = model.user_types()
    return jsonify(content)

@UserTypeBlueprint.route("/update_user_type/<id>", methods=["PUT"])
@cross_origin()
def update_user_type(id):
    # user = User.query.get(std_id.usr_id)
    user_created = UserType.query.get(id)
    name = request.json["name"]
    description = request.json["description"]
    created_at = user_created.created_at
    updated_at = datetime.now()
    return jsonify(model.update_user_type(id, name, description,created_at ,updated_at))

@UserTypeBlueprint.route("/delete_user_type/<id>", methods=["DELETE"])
@cross_origin()
def delete_user_type(id):
    return jsonify(model.delete_user_type(id))
