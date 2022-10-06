from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

# Import FKs
from backend.models.User_model import User

class Teacher(db.Model):
    tea_id = db.Column(db.Integer, primary_key=True)    
    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))
    tea_type = db.Column(db.String(70))
    tea_cat = db.Column(db.String(70))

    def __init__(self, usr_id, tea_type, tea_cat): # este se usa para el JSON así que guardarlo
        self.usr_id = usr_id
        self.tea_type = tea_type
        self.tea_cat = tea_cat

class TeacherSchema(ma.Schema):
    class Meta:
        fields = (
            'tea_id',
            'usr_id',
            'tea_type',
            'tea_cat'
        )

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)

db.create_all()

class Teacher_Model:
    # Create a teacher
    def create_teacher(self, usr_id, tea_type, tea_cat):
        new_teacher = Teacher(usr_id, tea_type, tea_cat)
        db.session.add(new_teacher)
        db.session.commit()
        result = teacher_schema.dump(new_teacher)
        return result

    # List teacher with ID
    def teacher(self, tea_id):
        teacher = Teacher.query.get(tea_id)
        result = teacher_schema.dump(teacher)
        return result

    # List all teachers
    def teachers(self):
        all_teachers = Teacher.query.all()
        result = teachers_schema.dump(all_teachers)
        return result

    # Update teacher by ID
    def update_teacher(self, tea_id, usr_id, tea_type, tea_cat):
        teacher = Teacher.query.get(tea_id)
        teacher.usr_id = usr_id
        teacher.tea_type = tea_type
        teacher.tea_cat = tea_cat
        db.session.commit()
        result = teacher_schema.dump(teacher)
        return result

    # Delete teacher by ID
    def delete_teacher(self, tea_id):
        teacher = Teacher.query.get(tea_id)
        # teacher.usr_id = usr_id
        # teacher.tea_type = tea_type
        # teacher.tea_cat = tea_cat
        db.session.delete(teacher)
        db.session.commit()
        return teacher_schema.jsonify(teacher)
        
