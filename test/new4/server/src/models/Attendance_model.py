from database import db, ma
from flask import Flask

from models.Group_model import Group
from models.Student_model import Student

class Attendance(db.Model):
    __tablename__="attendace"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey(Group.id), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.id), nullable=False)
    valor = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, group_id, student_id, date, valor, created_at, updated_at):
        self.group_id = group_id
        self.student_id = student_id
        self.date = date
        self.valor = valor
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Attendance('{self.date}', '{self.group_id}', '{self.student_id}', '{self.valor}')"

class AttendanceSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "date",
            "group_id",
            "student_id",
            "valor",
            "created_at",
            "updated_at"
        )

attendace_schema = AttendanceSchema()
attendaces_schema = AttendanceSchema(many=True)

class AttendanceModel:
    def create_attendace(self, date, group_id, student_id, valor, created_at, updated_at):
        new_attendace = Attendance(date, group_id, student_id, valor, created_at, updated_at)
        db.session.add(new_attendace)
        db.session.commit()
        return attendace_schema.dump(new_attendace)
    
    def attendace(self, id):
        attendace = Attendance.query.get(id)
        return attendace_schema.dump(attendace)

    def attendaces(self):
        attendaces = Attendance.query.all()
        return attendace_schema.dump(attendaces)

    def update_attendace(self, date, group_id, student_id, valor):
        attendace = Attendance.query.get(id)
        attendace.regular = date
        attendace.year = group_id
        attendace.user_id = student_id
        attendace.vector = valor
        db.session.commit()
        return attendace_schema.dump(attendace)

    def delete_attendace(self, id):
        attendace = Attendance.query.get(id)
        db.session.delete(attendace)
        db.session.commit()
        return attendace_schema.dump(attendace)