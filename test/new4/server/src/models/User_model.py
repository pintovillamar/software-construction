from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.Text, nullable=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey("user_type.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, last_name, dni, email, password, photo, user_type_id, created_at, updated_at):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email
        self.password = password
        self.photo = photo
        self.user_type_id = user_type_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"User {self.name}"

class UserSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "name",
            "last_name",
            "dni",
            "email",
            "password",
            "photo",
            "user_type_id",
            "created_at",
            "updated_at"
        )
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserModel:

    def create_user(self, name, last_name, dni, email, password, photo, user_type_id, created_at, updated_at):
        new_user = User(name, last_name, dni, email, password, photo, user_type_id, created_at, updated_at)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

    def user(self, id):
        user = User.query.get(id)
        return user_schema.dump(user)
    
    def users(self):
        users = User.query.all()
        return users_schema.dump(users)
    
    def update_user(self, id, name, last_name, dni, email, password, photo, user_type_id, created_at, updated_at):
        user = User.query.get(id)
        user.name = name
        user.last_name = last_name
        user.dni = dni
        user.email = email
        user.password = password
        user.photo = photo
        user.user_type_id = user_type_id
        user.created_at = created_at
        user.updated_at = updated_at
        db.session.commit()
        return user_schema.dump(user)

    def delete_user(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)
    