from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma
from flask import jsonify
from werkzeug.utils import secure_filename

from backend.models.User_model import User
from backend.blueprints.face_recognition_blueprint import Face_Recognition_Model

class Student(db.Model):
    std_id = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean())
    std_year = db.Column(db.Date())
    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))
    std_vector = db.Column(db.String(200))

    def __init__(self, usr_id, std_regular, std_year, std_vector):
        self.std_regular = std_regular
        self.std_year = std_year
        self.usr_id = usr_id
        self.std_vector = std_vector

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'std_id',
            'usr_id',
            'std_regular',
            'std_year',
            'std_vector'
            # guardar el vector
        )

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

db.create_all()

class Student_Model:
    # Create a student
    def create_student(self, usr_id, std_regular, std_year, std_vector):
        new_student = Student(usr_id, std_regular, std_year, std_vector)
        db.session.add(new_student)
        db.session.commit()
        result = student_schema.dump(new_student)
        return result

    # List student with ID
    def student(self, std_id):
        student = Student.query.get(std_id)
        result = student_schema.dump(student)
        return result

    # List all students
    def students(self):
        all_students = Student.query.all()
        result = students_schema.dump(all_students)
        return result

    # Update student by ID
    def update_student(self, std_id, usr_id, std_regular, std_year, std_vector):
        student = Student.query.get(std_id)
        student.usr_id = usr_id
        student.std_regular = std_regular
        student.std_year = std_year
        student.std_vector = std_vector
        db.session.commit()
        result = student_schema.dump(student)
        return result
    
     # Delete student by ID
    def delete_student(self, std_id):
        student = Student.query.get(std_id)
        db.session.delete(student)
        db.session.commit()
        return student_schema.jsonify(student)   

    # def convert_image_vector(self, std_id):
    #     student = Student.query.get(std_id)
    #     student.std_vector = std_vector
    #     result = student_schema.dump(student)
    #     return jsonify(result)

    def face_student(self, std_id):
        student = Student.query.get(std_id)
        path = student.std_vector

        

        return jsonify(path)