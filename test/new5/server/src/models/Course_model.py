from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime

class Course(db.Model):
    __tablename__ = "course"
    cur_id = db.Column(db.Integer, primary_key=True)
    cur_name = db.Column(db.String(255), nullable=False)
    cur_desc = db.Column(db.String(255), nullable=False)
    cur_created = db.Column(db.DateTime, nullable=False)
    cur_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, cur_name, cur_desc, cur_created, cur_updated):
        self.cur_name = cur_name
        self.cur_desc = cur_desc
        self.cur_created = cur_created
        self.cur_updated = cur_updated

class CourseSchema(ma.Schema):
    class Meta:
        fields = ( 
            "cur_id",
            "cur_name",
            "cur_desc",
            "cur_created",
            "cur_updated"
        )
    
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

db.create_all()

class Course_Model:

    def create_course(self):
        new_course = Course(request.json['cur_name'], request.json['cur_desc'], datetime.datetime.now(), datetime.datetime.now())
        db.session.add(new_course)
        db.session.commit()
        return course_schema.jsonify(new_course)

    def course(self, id):
        course = Course.query.get(id)
        return course_schema.jsonify(course)
    
    def courses(self):
        courses = Course.query.all()
        return jsonify(courses_schema.dump(courses))
    
    def update_course(self, id):
        course = Course.query.get(id)
        course.cur_name = request.json['cur_name']
        course.cur_desc = request.json['cur_desc']
        course.cur_updated = datetime.datetime.now()
        db.session.commit()
        return course_schema.jsonify(course)

    def delete_course(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return course_schema.jsonify(course)