from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def __init__(self, teacher_id, name, course_id):
        self.teacher_id = teacher_id
        self.name = name
        self.course_id = course_id

    def __repr__(self):
        return f"Group {self.name}"

class GroupSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "teacher_id",
            "name",
            "course_id"
        )
    
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

class GroupModel:

    def create_group(self, teacher_id, name, course_id):
        new_group = Group(teacher_id, name, course_id)
        db.session.add(new_group)
        db.session.commit()
        return group_schema.dump(new_group)

    def group(self, id):
        group = Group.query.get(id)
        return group_schema.dump(group)
    
    def groups(self):
        groups = Group.query.all()
        return groups_schema.dump(groups)
    
    def update_group(self, id, teacher_id, name, course_id):
        group = Group.query.get(id)
        group.teacher_id = teacher_id
        group.name = name
        group.course_id = course_id
        db.session.commit()
        return group_schema.dump(group)

    def delete_group(self, id):
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
        return group_schema.dump(group)
    