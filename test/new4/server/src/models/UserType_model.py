from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class UserType(db.Model):
    __tablename__ = "user_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, description, created_at, updated_at):
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"UserType {self.name}"

class UserTypeSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "name",
            "description",
            "created_at", # EN TODAS LAS TABLAS
            "updated_at"  # EN TODAS LAS TABLAS
        )

user_type_schema = UserTypeSchema()
user_types_schema = UserTypeSchema(many=True)

class UserTypeModel:

    def create_user_type(self, name, description, created_at, updated_at):
        new_user_type = UserType(name, description, created_at, updated_at)
        db.session.add(new_user_type)
        db.session.commit()
        return user_type_schema.dump(new_user_type)

    def user_type(self, id):
        user_type = UserType.query.get(id)
        return user_type_schema.dump(user_type)

    def user_types(self):
        user_types = UserType.query.all()
        return user_types_schema.dump(user_types)

    def update_user_type(self, id, name, description, created_at, updated_at):
        user_type = UserType.query.get(id)
        user_type.name = name
        user_type.description = description
        user_type.created_at = created_at
        user_type.updated_at = updated_at
        db.session.commit()
        return user_type_schema.dump(user_type)

    def delete_user_type(self, id):
        user_type = UserType.query.get(id)
        db.session.delete(user_type)
        db.session.commit()
        return user_type_schema.dump(user_type)
