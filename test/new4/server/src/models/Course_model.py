from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    des = db.Column(db.String(255), nullable=False)

    def __init__(self, name, des):
        self.name = name
        self.des = des

    def __repr__(self):
        return f"Course {self.name}"

class CourseSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "name",
            "des"
        )
    
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class CourseModel:

    def create_course(self, name, des):
        new_course = Course(name, des)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

    def course(self, id):
        course = Course.query.get(id)
        return course_schema.dump(course)
    
    def courses(self):
        courses = Course.query.all()
        return courses_schema.dump(courses)
    
    def update_course(self, id, name, des):
        course = Course.query.get(id)
        course.name = name
        course.des = des
        db.session.commit()
        return course_schema.dump(course)

    def delete_course(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return course_schema.dump(course)
    