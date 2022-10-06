from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

# Import FKs
from backend.models.User_type_model import User_type

class User(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_dni = db.Column(db.String(8))
    usr_pass = db.Column(db.String(16))
    usr_photo = db.Column(db.String(70))
    usr_name = db.Column(db.String(70))
    usr_last_name = db.Column(db.String(70))
    usr_dob = db.Column(db.Date()) # date of birth
    usr_email = db.Column(db.String(70))
    ust_id = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id): # este se usa para el JSON así que guardarlo
        self.usr_dni = usr_dni
        self.usr_pass = usr_pass
        self.usr_photo = usr_photo
        self.usr_name = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dob = usr_dob
        self.usr_email = usr_email
        self.ust_id = ust_id

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'usr_id',
            'usr_dni',
            'usr_pass',
            'usr_photo',
            'usr_name',
            'usr_last_name',
            'usr_dob',
            'usr_email',
            'ust_id'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()

class User_Model:
    # Create a user
    def create_user(self, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id):
        new_user = User(usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id)
        db.session.add(new_user)
        db.session.commit()
        result = user_schema.dump(new_user)
        return result

    # List user with ID
    def user(self, usr_id):
        user = User.query.get(usr_id)
        result = user_schema.dump(user)
        return result

    # List all users
    def users(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return result

    # Update user by ID
    def update_user(self, usr_id, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id):
        user = User.query.get(usr_id)
        user.usr_dni = usr_dni
        user.usr_pass = usr_pass
        user.usr_photo = usr_photo
        user.usr_name = usr_name
        user.usr_last_name = usr_last_name
        user.usr_dob = usr_dob
        user.usr_email = usr_email
        user.ust_id = ust_id
        db.session.commit()
        result = user_schema.dump(user)
        return result

    # Delete user by ID
    def delete_user(self, usr_id):
        user = User.query.get(usr_id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)


