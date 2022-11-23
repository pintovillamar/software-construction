from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime
import json

from models.Teacher_model import Teacher
from models.Course_model import Course

class Group(db.Model):
    __tablename__ = "group"
    gru_id = db.Column(db.Integer, primary_key=True)
    gru_name = db.Column(db.String(255))
    gru_created = db.Column(db.DateTime)
    gru_updated = db.Column(db.DateTime)
    cur_id = db.Column(db.Integer, db.ForeignKey(Course.cur_id))
    tea_id = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))

    # def create_group(self):
    #     new_group = Group(request.json['gru_name'], 
    #                             request.json['cur_id'],
    #                             request.json['tea_id'],
    #                             datetime.datetime.now(),
    #                             datetime.datetime.now())
    #     db.session.add(new_group)
    #     db.session.commit()
    #     return group_schema.jsonify(new_group)


    def __init__(self, gru_name, cur_id, tea_id,  gru_created, gru_updated):
        self.gru_name = gru_name
        self.cur_id = cur_id
        self.tea_id = tea_id
        self.gru_created = gru_created
        self.gru_updated = gru_updated

class GroupSchema(ma.Schema):
    class Meta:
        fields = ( 
            "gru_id",
            "gru_name",
            "tea_id",
            "cur_id",
            "gru_created",
            "gru_updated"
        )
    
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

db.create_all()

class Group_Model:

    def create_group(self):
        new_group = Group(request.json['gru_name'], 
                                request.json['cur_id'],
                                request.json['tea_id'],
                                datetime.datetime.now(),
                                datetime.datetime.now())
        db.session.add(new_group)
        db.session.commit()
        return group_schema.jsonify(new_group)

    def group(self, id):
        group = Group.query.get(id)
        return group_schema.jsonify(group)
    
    def groups(self):
        groups = Group.query.all()
        result = groups_schema.dump(groups)
        return jsonify(result)
    
    def update_group(self, id):
        group = Group.query.get(id)
        group.gru_name = request.json['gru_name']
        group.tea_id = request.json['tea_id']
        group.cur_id = request.json['cur_id']
        group.gru_updated = datetime.datetime.now()
        db.session.commit()
        return group_schema.jsonify(group)


    def delete_group(self, id):
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
        return group_schema.jsonify(group)