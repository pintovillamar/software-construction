from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename
import json, requests


# Import FKs
from backend.models.User_type_model import User_type

class UserTest(db.Model):
    usrT_id = db.Column(db.Integer, primary_key=True)
    usrT_photo = db.Column(db.String(200))
    usrT_dni = db.Column(db.String(8))
    usrT_pass = db.Column(db.String(16))
    usrT_name = db.Column(db.String(70))
    usrT_last_name = db.Column(db.String(70))
    usrT_dob = db.Column(db.Date()) # date of birth
    usrT_email = db.Column(db.String(70))
    ust_id = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usrT_photo, usrT_pass, usrT_dni, usrT_name, usrT_last_name, usrT_dob, usrT_email, ust_id): # este se usa para el JSON así que guardarlo
        self.usrT_photo = usrT_photo
        self.usrT_pass = usrT_pass
        self.usrT_dni = usrT_dni
        self.usrT_name = usrT_name
        self.usrT_last_name = usrT_last_name
        self.usrT_dob = usrT_dob
        self.usrT_email = usrT_email
        self.ust_id = ust_id
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'usrT_photo',
            'usrT_id',
            'usrT_dni',
            'usrT_pass',
            'usrT_name',
            'usrT_last_name',
            'usrT_dob',
            'usrT_email',
            'ust_id'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()

class UserTest_Model:
    # Create a user
    def create_user_test(self, usrT_photo, usrT_pass, usrT_dni, usrT_name, usrT_last_name, usrT_dob, usrT_email, ust_id):
        new_user = UserTest(usrT_photo,
                            usrT_pass,
                            usrT_dni,
                            usrT_name,
                            usrT_last_name,
                            usrT_dob,
                            usrT_email,
                            ust_id)
        db.session.add(new_user)
        db.session.commit()
        result = user_schema.dump(new_user)
        return result

    # List user with ID
    def user_test(self, usrT_id):
        user = UserTest.query.get(usrT_id)
        result = user_schema.dump(user)
        return result

    # List all users
    def users_test(self):
        users = UserTest.query.all()
        result = users_schema.dump(users)
        return result


