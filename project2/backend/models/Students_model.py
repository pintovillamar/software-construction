from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma

from project2.backend.models.Users_model import User

class Student(db.Model):
    std_id = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean())
    std_year = db.Column(db.Date())
    usr_id = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usr_id, std_regular, std_year):
        self.std_regular = std_regular
        self.std_year = std_year
        self.usr_id = usr_id

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'std_id',
            'usr_id',
            'std_regular',
            'std_year'
        )

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

db.create_all()
