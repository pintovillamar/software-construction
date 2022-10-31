from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import json
import os

from backend.models.User_model import User_Model
model = User_Model()

user_blueprint = Blueprint('/user_blueprint', __name__)

# self.usr_name = usr_name
# self.usr_last_name = usr_last_name
# self.usr_dni = usr_dni
# self.usr_email = usr_email
# self.usr_passwd = usr_passwd
# self.usr_photo = usr_photo
# self.usr_dob = usr_dob
# self.ust_id = ust_id

# Create a user
@user_blueprint.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    f = request.files['file']
    filename = secure_filename(f.filename)

    path = "/home/jose/Documents/software-construction/project2/photos/uploads/" + filename 
    f.save(path)

    data = json.loads(request.form.get('data'))

    content = model.create_user(data['usr_name'],
                                data['usr_last_name'],
                                data['usr_dni'],
                                data['usr_email'], 
                                data['usr_passwd'],
                                path,
                                data['usr_dob'],
                                data['ust_id'])
    return jsonify(content)

# List user with ID
@user_blueprint.route('/user/<usr_id>', methods=['POST'])
@cross_origin()
def user(usr_id):
    content = model.user(usr_id)
    return jsonify(content)

# List all users
@user_blueprint.route('/users', methods=['POST'])
@cross_origin()
def users():
    content = model.users()
    return jsonify(content)

# Update user by ID
@user_blueprint.route('/update_user/<usr_id>', methods=['POST'])
@cross_origin()
def update_user(usr_id):

    # deletePic(usr_id)

    f = request.files['file']
    filename = secure_filename(f.filename)
    path = "/home/jose/Documents/software-construction/project2/photos/uploads/" + filename
    f.save(path)
    data = json.loads(request.form.get('data'))

    content = model.update_user(usr_id, 
                                data['usr_name'],
                                data['usr_last_name'],
                                data['usr_dni'],
                                data['usr_email'], 
                                data['usr_passwd'],
                                path,
                                data['usr_dob'],
                                data['ust_id']) 
    return jsonify(content)

# Delete user by ID
@user_blueprint.route('/delete_user/<usr_id>', methods=['POST'])
@cross_origin()
def delete_user(usr_id):
    deletePic(usr_id)
    model.delete_user(usr_id)
    return f"User {usr_id} deleted succesfully"

# Delete user pic by ID
def deletePic(usr_id):
    user = model.user(usr_id)
    os.remove(user['usr_photo'])
    return f"User {usr_id} photo deleted succesfully"
