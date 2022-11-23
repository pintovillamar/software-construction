from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime
import json

from models.User_model import User

class Teacher(db.Model):
    __tablename__ = "teacher"
    tea_id = db.Column(db.Integer, primary_key=True)  
    tea_type = db.Column(db.String(255))
    tea_cat = db.Column(db.String(255))
    tea_created = db.Column(db.DateTime)
    tea_updated = db.Column(db.DateTime)
    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, usr_id, tea_type, tea_cat, tea_created, tea_updated):
        self.usr_id = usr_id
        self.tea_type = tea_type
        self.tea_cat = tea_cat
        self.tea_created = tea_created
        self.tea_updated = tea_updated

class TeacherSchema(ma.Schema):
    class Meta:
        fields = ( 
            "tea_id",
            "usr_id",
            "tea_type",
            "tea_cat",
            "tea_created",
            "tea_updated"
        )
    
teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)

db.create_all()

class Teacher_Model:

    def create_teacher(self):
        new_teacher = Teacher(request.json['usr_id'], 
                                request.json['tea_type'],
                                request.json['tea_cat'],
                                datetime.datetime.now(),
                                datetime.datetime.now())
        db.session.add(new_teacher)
        db.session.commit()
        return teacher_schema.jsonify(new_teacher)

    def teacher(self, id):
        teacher = Teacher.query.get(id)
        return teacher_schema.jsonify(teacher)
    
    def teachers(self):
        teachers = Teacher.query.all()
        result = teachers_schema.dump(teachers)
        return jsonify(result)
    
    def update_teacher(self, id):
        teacher = Teacher.query.get(id)
        teacher.tea_type = request.json['tea_type']
        teacher.tea_cat = request.json['tea_cat']
        teacher.usr_id = request.json['usr_id']
        teacher.tea_updated = datetime.datetime.now()
        db.session.commit()
        return teacher_schema.jsonify(teacher)

    def delete_teacher(self, id):
        teacher = Teacher.query.get(id)
        db.session.delete(teacher)
        db.session.commit()
        return teacher_schema.jsonify(teacher)

    def get_teacher_combobox(self, id):        
        query_user = User.query.filter_by(usr_id=id).first()
        query_teacher = Teacher.query.filter_by(usr_id=query_user.usr_id).first()
        print(query_user.usr_name)
        new_id = query_teacher.tea_id
        name = query_user.usr_name
        last_name = query_user.usr_last_name
        
        
        return jsonify({'id': new_id, 'title': name})
