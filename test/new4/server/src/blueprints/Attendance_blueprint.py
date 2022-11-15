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

from models.Attendance_model import AttendanceModel, Attendance

from models.User_model import User

model = AttendanceModel()

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

AttendanceBlueprint = Blueprint("AttendanceBlueprint", __name__)

@AttendanceBlueprint.route("/login", methods=["GET"])
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


@AttendanceBlueprint.route("/create_attendance", methods=["POST"])
@token_required
@cross_origin()
def create_attendance():
    f = request.files['file']
    filename = secure_filename(f.filename)
    data = json.loads(request.form.get('data'))

    content = model.create_attendace(
        data["date"],
        data["group_id"],
        data["student_id"],
        data,["valor"],
        datetime.now(),
        datetime.now()
    )

    updated = rename_pic(Attendance.query.get(content["id"]).id)

    content = model.update_attendace(
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
    
@AttendanceBlueprint.route("/attendance/<id>", methods=["GET"])
@token_required
@cross_origin()
def attendance(id):
    content = model.attendance(id)
    return jsonify(content)

@AttendanceBlueprint.route("/attendances", methods=["GET"])
@token_required
@cross_origin()
def attendances():
    content = model.attendances()
    return jsonify(content)
    
@AttendanceBlueprint.route("/update_attendance/<id>", methods=["PUT"])
@token_required
@cross_origin()
def update_attendance(id):
    attendance_created = Attendance.query.get(id)
    updated = rename_pic(id)

    f = request.files['file']
    # filename = secure_filename(f.filename)

    data = json.loads(request.form.get('data'))
    content = model.update_attendace(
        id,
        data["date"],
        data["group_id"],
        data["student_id"],
        data,["valor"],
        attendance_created.created_at,
        datetime.now()
    )

@AttendanceBlueprint.route("/delete_attendance/<id>", methods=["DELETE"])
@token_required
@cross_origin()
def delete_attendance(id):
    return jsonify(model.delete_attendance(id))

def rename_pic(id):
    attendance_id = id
    attendance_id = Attendance.query.get(attendance_id).id
    date = Attendance.query.get(attendance_id).date
    group_id = Attendance.query.get(attendance_id).group_id
    student_id = Attendance.query.get(attendance_id).student_id
    valor = Attendance.query.get(attendance_id).valor

    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

    new_type_attendance = path +str(attendance_id)+"_"+date+"_"+group_id+"_"+student_id+"-"+group_id+"-"
    return new_type_attendance