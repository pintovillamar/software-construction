from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime
import json
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

from models.UserType_model import User_Type

class User(db.Model):
    __tablename__ = "user"
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_name = db.Column(db.String(255))
    usr_last_name = db.Column(db.String(255))
    usr_dni = db.Column(db.Integer)
    usr_dob = db.Column(db.Date)
    usr_email = db.Column(db.String(255))
    usr_password = db.Column(db.String(255))
    usr_photo = db.Column(db.Text)
    usr_created = db.Column(db.DateTime)
    usr_updated = db.Column(db.DateTime)
    ust_id = db.Column(db.Integer, db.ForeignKey(User_Type.ust_id))

    def __init__(self, usr_name, usr_last_name, usr_dni, usr_dob, usr_email, usr_password, usr_photo, usr_created, usr_updated, ust_id):
        self.usr_name = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dni = usr_dni
        self.usr_dob = usr_dob
        self.usr_email = usr_email
        self.usr_password = generate_password_hash(usr_password)
        self.usr_photo = usr_photo
        self.usr_created = usr_created
        self.usr_updated = usr_updated
        self.ust_id = ust_id

    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('usr_id', 'usr_name', 'usr_last_name', 'usr_dni', 'usr_dob', 'usr_email', 'usr_password', 'usr_photo', 'usr_created', 'usr_updated', 'ust_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()

class User_Model:
    def create_user(self):
        f = request.files['file']
        filename = secure_filename(f.filename)
        path = '/home/jose/Documents/software-construction/test/new5/server/images/uploaded/' + filename
        f.save(path)
        data = json.loads(request.form['data'])
        new_user = User(
            data['usr_name'],
            data['usr_last_name'],
            data['usr_dni'],
            data['usr_dob'],
            data['usr_email'],
            data['usr_password'],
            path,
            datetime.datetime.now(),
            datetime.datetime.now(),
            data['ust_id']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    def user(self, id):
        user = User.query.get(id)
        return user_schema.jsonify(user)

    def users(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)
    
    def update_user(self, id):
        user = User.query.get(id)
        f = request.files['photo']
        path = '/home/jose/Documents/software-construction/test/new5/server/images/uploaded/' + f.filename
        f.save(path)
        data = json.loads(request.form['data'])
        user.usr_name = data['usr_name']
        user.usr_last_name = data['usr_last_name']
        user.usr_dni = data['usr_dni']
        user.usr_dob = data['usr_dob']
        user.usr_email = data['usr_email']
        user.usr_password = data['usr_password'].generate_password_hash()
        user.usr_photo = path
        user.usr_updated = datetime.datetime.now()
        user.ust_id = data['ust_id']
        db.session.commit()
        return user_schema.jsonify(user)

    def delete_user(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)

# def rename_pic(id):
#     user_name = User.query.get(user_id.usr_id)
#     user_last_name = User.query.get(user_id).usr_last_name

#     path = "/home/jose/Documents/software-construction/test/new4/server/static/images/"

#     new_name = path +str(user_id)+"_"+user_name+"_"+user_last_name+"-"
#     return new_name
