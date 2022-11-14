from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import requests
import json

from external import convertToJson

from datetime import datetime

from models.test_model import testModel
from models.User_model import User

model = testModel()

TestBlueprint = Blueprint("testBlueprint", __name__)

@TestBlueprint.route("/test/<id>", methods=["POST"])
@cross_origin()
def test(id):
    

    user_id = id    
    user_id = User.query.get(user_id).id
    user_name = User.query.get(user_id).name
    user_last_name = User.query.get(user_id).last_name
    new_name = str(user_id)+"_"+user_name+"_"+user_last_name+"-"

    f = request.files['file']
    filename = secure_filename(f.filename)
    path = "/home/jose/Documents/software-construction/test/new4/server/static/images/" + str(new_name) + filename
    f.save(path)
    # data = json.loads(request.form.get('data'))

    content = path
    print(content)

    return jsonify(content)