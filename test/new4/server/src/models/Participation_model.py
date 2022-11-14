from database import db, ma
from flask import Flask

from models.Group_model import Group
from models.Student_model import Student

class Participation(db.Model):
    __tablename__="participation"
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
        return f"Participation('{self.date}', '{self.group_id}', '{self.student_id}', '{self.valor}')"

class ParticipationSchema(ma.Schema):
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

participation_schema = ParticipationSchema()
participations_schema = ParticipationSchema(many=True)

class ParticipationModel:
    def create_participation(self, date, group_id, student_id, valor, created_at, updated_at):
        new_participation = Participation(date, group_id, student_id, valor, created_at, updated_at)
        db.session.add(new_participation)
        db.session.commit()
        return participation_schema.dump(new_participation)
    
    def participation(self, id):
        participation = Participation.query.get(id)
        return participation_schema.dump(participation)

    def participations(self):
        participations = Participation.query.all()
        return participation_schema.dump(participations)

    def update_participation(self, date, group_id, student_id, valor):
        participation = Participation.query.get(id)
        participation.regular = date
        participation.year = group_id
        participation.user_id = student_id
        participation.vector = valor
        db.session.commit()
        return participation_schema.dump(participation)

    def delete_participation(self, id):
        participation = Participation.query.get(id)
        db.session.delete(participation)
        db.session.commit()
        return participation_schema.dump(participation)