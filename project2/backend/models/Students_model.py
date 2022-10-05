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

class Students_Model:
    # Create a student
    def create_student(self, usr_id, std_regular, std_year):
        new_student = Student(usr_id, std_regular, std_year)
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student)

    # List student with ID
    def student(self, std_id):
        student = Student.query.get(std_id)
        return student_schema.dump(student)

    # List all user types
    def students(self):
        all_students = Student.query.all()
        result = student_schema.dump(all_students)
        db.session.commit()
        return result

    # Update student by ID
    def update_student(self, std_id):
        student = Student.query.get(std_id)
        student.usr_id = Student.usr_id
        student.std_regular = Student.std_regular
        student.std_year = Student.std_year
        db.session.commit()
        return student_schema.jsonify(student)