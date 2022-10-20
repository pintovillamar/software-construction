from unittest import result
from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

# Import FKs
from backend.models.Student_model import Student
from backend.models.Group_model import Group

class Enroll(db.Model):
    enr_id = db.Column(db.Integer, primary_key=True)
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    enr_date = db.Column(db.Date())

    def __init__(self, std_id, gru_id, enr_date):
        self.std_id = std_id
        self.gru_id = gru_id
        self.enr_date = enr_date

class EnrollSchema(ma.Schema):
    class Meta:
        fields = (
            'enr_id',
            'std_id',
            'gru_id',
            'enr_date'
        )
    
enroll_schema = EnrollSchema()
enrolls_schema = EnrollSchema(many=True)

db.create_all()

class Enroll_Model:
    # Create an enrollment
    def create_enroll(self, std_id, gru_id, enr_date):
        new_enroll = Enroll(std_id, gru_id, enr_date)
        db.session.add(new_enroll)
        db.session.commit()
        result = enroll_schema.dump(new_enroll)
        return result
    
    # List an enrollment with ID
    def enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id)
        result = enroll_schema.dump(enroll)
        return result
    
    # List all enrollments
    def enrolls(self):
        all_enrolls = Enroll.query.all()
        result = enrolls_schema.dump(all_enrolls)
        return result

    # Update an enrollment
    def update_enroll(self, enr_id, std_id, gru_id, enr_date):
        enroll = Enroll.query.get(enr_id)
        enroll.std_id = std_id
        enroll.gru_id = gru_id
        enroll.enr_date = enr_date
        db.session.commit()
        result = enroll_schema.dump(enroll)
        return result

    # Delete an enrollment
    def delete_enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id)
        db.session.delete(enroll)
        db.session.commit()
        return enroll_schema.jsonify(enroll)
    