from database import db, ma
from flask import Flask

from models.User_model import User

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regular = db.Column(db.Boolean, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    vector = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, regular, year, vector, created_at, updated_at):
        self.user_id = user_id
        self.regular = regular
        self.year = year
        self.vector = vector
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Student('{self.regular}', '{self.year}', '{self.user_id}', '{self.vector}')"
    
class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "user_id",
            "regular",
            "year",
            "vector",
            "created_at",
            "updated_at"
        )
    
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

class StudentModel:
    def create_student(self, regular, year, user_id, vector, created_at, updated_at):
        new_student = Student(regular, year, user_id, vector, created_at, updated_at)
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student)
    
    def student(self, id):
        student = Student.query.get(id)
        return student_schema.dump(student)

    def students(self):
        students = Student.query.all()
        return students_schema.dump(students)

    def update_student(self, id, regular, year, user_id, vector):
        student = Student.query.get(id)
        student.regular = regular
        student.year = year
        student.user_id = user_id
        student.vector = vector
        db.session.commit()
        return student_schema.dump(student)

    def delete_student(self, id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return student_schema.dump(student)

    

    