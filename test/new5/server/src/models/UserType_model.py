from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime

class User_Type(db.Model):
    __tablename__ = "user_type"
    ust_id = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(255))
    ust_desc = db.Column(db.Text)
    ust_created = db.Column(db.DateTime)
    ust_updated = db.Column(db.DateTime)

    def __init__(self, ust_name, ust_desc, ust_created, ust_updated):
        self.ust_name = ust_name
        self.ust_desc = ust_desc
        self.ust_created = ust_created
        self.ust_updated = ust_updated

class User_TypeSchema(ma.Schema):
    class Meta:
        fields = ('ust_id', 'ust_name', 'ust_desc', 'ust_created', 'ust_updated')

user_type_schema = User_TypeSchema()
user_types_schema = User_TypeSchema(many=True)

db.create_all()

class User_Type_Model:
    def create_user_type(self):
        new_user_type = User_Type(request.json['ust_name'], request.json['ust_desc'], datetime.datetime.now(), datetime.datetime.now())
        db.session.add(new_user_type)
        db.session.commit()
        return user_type_schema.jsonify(new_user_type)

    def user_type(self, id):
        user_type = User_Type.query.get(id)
        return user_type_schema.jsonify(user_type)

    def user_types(self):
        all_user_types = User_Type.query.all()
        result = user_types_schema.dump(all_user_types)
        return jsonify(result)

    def update_user_type(self, id):
        user_type = User_Type.query.get(id)
        user_type.ust_name = request.json['ust_name']
        user_type.ust_desc = request.json['ust_desc']
        user_type.ust_updated = datetime.datetime.now()
        db.session.commit()
        return user_type_schema.jsonify(user_type)

    def delete_user_type(self, id):
        user_type = User_Type.query.get(id)
        db.session.delete(user_type)
        db.session.commit()
        return user_type_schema.jsonify(user_type)