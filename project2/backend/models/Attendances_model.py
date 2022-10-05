from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma

from project2.backend.models.Students_model import Student
from project2.backend.models.Groups_model import Group

class Attendance(db.Model):
    att_id = db.Column(db.Integer, primary_key=True)
    att_date = db.Column(db.Date())
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    att_val = db.Column(db.Boolean)

    def __init__(self, att_date, gru_id, std_id, att_val):
        self.att_date = att_date
        self.gru_id = gru_id
        self.std_id = std_id
        self.att_val = att_val

class AttendanceSchema(ma.Schema):
    class Meta:
        fields = (
            'att_id',
            'att_date',
            'gru_id',
            'std_id',
            'att_val'
        )

attendance_schema = AttendanceSchema()
attendances_schema = AttendanceSchema(many=True)

db.create_all()