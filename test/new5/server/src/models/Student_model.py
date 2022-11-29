from flask import jsonify
from database import db
from database import ma
from flask import request
from dotenv import load_dotenv
import datetime
import json
import os
import requests

from functions.external import convertToJson

from models.User_model import User

class Student(db.Model):
    __tablename__ = "student"
    std_id = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean, nullable=False)
    std_year = db.Column(db.Integer, nullable=False)
    std_vector = db.Column(db.Text, nullable=False)
    std_user_id = db.Column(db.Integer, db.ForeignKey(User.usr_id), nullable=False)
    std_created = db.Column(db.DateTime, nullable=False)
    std_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, std_regular, std_year, std_vector, std_user_id, std_created, std_updated):
        self.std_regular = std_regular
        self.std_year = std_year
        self.std_vector = std_vector
        self.std_user_id = std_user_id
        self.std_created = datetime.datetime.now()
        self.std_updated = datetime.datetime.now()

    def __repr__(self):
        return '<Student %r>' % self.std_id
    
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('std_id', 'std_regular', 'std_year', 'std_vector', 'std_user_id', 'std_created', 'std_updated')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

db.create_all()

class Student_Model:
    def create_student(self):
        user_id = request.json['std_user_id']
        user = User.query.get(user_id)

        url = "http://localhost:81/openfaceAPI"
        files = {'file': open(user.usr_photo, 'rb')}
        vector = requests.post(url, files=files)
        
        vector = convertToJson(vector.text)
        
        std_regular = request.json['std_regular']
        std_year = request.json['std_year']
        std_user_id = user_id
        std_vector = vector
        std_created = datetime.datetime.now()
        std_updated = datetime.datetime.now()

        new_student = Student(std_regular, std_year, std_vector, std_user_id, std_created, std_updated)

        db.session.add(new_student)
        db.session.commit()

        

        return student_schema.jsonify(new_student)

    def student(self, id):
        student = Student.query.get(id)
        return student_schema.jsonify(student)
    
    def students(self):
        all_students = Student.query.all()
        result = students_schema.dump(all_students)
        return jsonify(result)

    def update_student(self, id):
        student = Student.query.get(id)

        std_regular = request.json['std_regular']
        std_year = request.json['std_year']
        std_vector = request.json['std_vector']
        std_user_id = request.json['std_user_id']

        student.std_regular = std_regular
        student.std_year = std_year
        student.std_vector = std_vector
        student.std_user_id = std_user_id
        student.std_updated = datetime.datetime.now()

        db.session.commit()

        return student_schema.jsonify(student)

    def delete_student(self, id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()

        return student_schema.jsonify(student)


    