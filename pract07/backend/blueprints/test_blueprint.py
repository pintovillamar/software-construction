from pickle import GLOBAL
from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import json
from werkzeug.utils import secure_filename

from backend.models.test_model import UserTest_Model
model = UserTest_Model()

test_blueprint = Blueprint('/test_blueprint', __name__)

# Create a userTEST
@test_blueprint.route('/create_user_test', methods=['POST'])
@cross_origin()
def create_user_test():
    # # print(request.json['usrT_dni'])

    # # f = request.files['usrT_photo']

    # # p = request.form.post("data")
    # f = request.form['data']
    # # text json to object 
    

    # content = model.create_user_test(f,
    #                                 request.json['usrT_pass'],
    #                                 request.json['usrT_dni'],    
    #                                 request.json['usrT_name'],
    #                                 request.json['usrT_last_name'],
    #                                 request.json['usrT_dob'],
    #                                 request.json['usrT_email'],
    #                                 request.json['ust_id'])
    # # content = model.create_user_test(f,)

    # # filename = f.filename
    # # path = "/home/jose/Documents/software-construction/project2/backend/photos/uploads" + filename
    # # f.save(path)

    # return jsonify(content)

    
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = "/home/jose/Documents/software-construction/project2/photos/uploads/" + filename 
    f.save(path)
    data = json.loads(request.form.get('data'))
    content = model.create_user_test(path,
                                            data['usrT_pass'],
                                            data['usrT_dni'],
                                            data['usrT_name'],
                                            data['usrT_last_name'],
                                            data['usrT_dob'],
                                            data['usrT_email'],
                                            data['ust_id'])
    return jsonify(content)

# List userTEST with ID
@test_blueprint.route('/user_test/<usrT_id>', methods=['POST'])
@cross_origin()
def user_test(usrT_id):
    content = model.user_test(usrT_id)
    return jsonify(content)

# List all usersTEST
@test_blueprint.route('/users_test', methods=['POST'])
@cross_origin()
def users_test():
    content = model.users_test()
    return jsonify(content)