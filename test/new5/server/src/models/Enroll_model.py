from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime
import json

from models.Student_model import Student
from models.Group_model import Group

class Enroll(db.Model):
    __tablename__ = "enroll"
    enr_id = db.Column(db.Integer, primary_key=True)
    enr_date = db.Column(db.Date)
    enr_created = db.Column(db.DateTime)
    enr_updated = db.Column(db.DateTime)
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, std_id, gru_id, enr_date, enr_updated, enr_created):
        self.std_id = std_id
        self.gru_id = gru_id
        self.enr_date = enr_date
        self.enr_created = enr_created
        self.enr_updated = enr_updated

class EnrollSchema(ma.Schema):
    class Meta:
        fields = (
            'enr_id',
            'std_id',
            'gru_id',
            'enr_date',
            'enr_created',
            'enr_updated'
        )
    
enroll_schema = EnrollSchema()
enrolls_schema = EnrollSchema(many=True)

db.create_all()

class Enroll_Model:

    def create_enroll(self):
        new_enroll = Enroll(request.json['std_id'], 
                                request.json['gru_id'],
                                request.json['enr_date'],
                                datetime.datetime.now(),
                                datetime.datetime.now())
        db.session.add(new_enroll)
        db.session.commit()
        return enroll_schema.jsonify(new_enroll)

    def enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id)
        result = enroll_schema.dump(enroll)
        return result
    
    # List all enrollments
    def enrolls(self):
        enrolls = Enroll.query.all()
        result = enrolls_schema.dump(enrolls)
        return result

    # Update an enrollment
    def update_enroll(self, id):
        enroll = Enroll.query.get(id)
        enroll.std_id = request.json['std_id']
        enroll.gru_id = request.json['gru_id']
        enroll.enr_date = request.json['enr_date']
        enroll.enr_updated = datetime.datetime.now()
        db.session.commit()
        return enrolls_schema.jsonify(enroll)

    # Delete an enrollment
    def delete_enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id)
        db.session.delete(enroll)
        db.session.commit()
        return enroll_schema.jsonify(enroll)