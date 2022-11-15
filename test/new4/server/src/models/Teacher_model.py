from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    cat = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, type, cat, created_at, updated_at):
        self.user_id = user_id
        self.type = type
        self.cat = cat
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Teacher {self.id}"

class TeacherSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "user_id",
            "type",
            "cat",
            "created_at",
            "updated_at"
        )
    
teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)

class TeacherModel:

    def create_teacher(self, user_id, type, cat, created_at, updated_at):
        new_teacher = Teacher(user_id, type, cat, created_at, updated_at)
        db.session.add(new_teacher)
        db.session.commit()
        return teacher_schema.dump(new_teacher)

    def teacher(self, id):
        teacher = Teacher.query.get(id)
        return teacher_schema.dump(teacher)
    
    def teachers(self):
        teachers = Teacher.query.all()
        return teachers_schema.dump(teachers)
    
    def update_teacher(self, id, user_id, type, cat, created_at, updated_at):
        teacher = Teacher.query.get(id)
        teacher.user_id = user_id
        teacher.type = type
        teacher.cat = cat
        teacher.created_at = created_at
        teacher.updated_at = updated_at
        db.session.commit()
        return teacher_schema.dump(teacher)

    def delete_teacher(self, id):
        teacher = Teacher.query.get(id)
        db.session.delete(teacher)
        db.session.commit()
        return teacher_schema.dump(teacher)
    