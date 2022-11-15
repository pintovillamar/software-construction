from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    des = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, des, created_at, updated_at):
        self.name = name
        self.des = des
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Course {self.name}"

class CourseSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "name",
            "des",
            "created_at",
            "updated_at"
        )
    
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class CourseModel:

    def create_course(self, name, des, created_at, updated_at):
        new_course = Course(name, des, created_at, updated_at)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

    def course(self, id):
        course = Course.query.get(id)
        return course_schema.dump(course)
    
    def courses(self):
        courses = Course.query.all()
        return courses_schema.dump(courses)
    
    def update_course(self, id, name, des, created_at, updated_at):
        course = Course.query.get(id)
        course.name = name
        course.des = des
        course.created_at = created_at
        course.updated_at = updated_at
        db.session.commit()
        return course_schema.dump(course)

    def delete_course(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return course_schema.dump(course)
    