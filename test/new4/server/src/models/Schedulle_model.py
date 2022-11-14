from flask import jsonify
from database import db
from database import ma

from werkzeug.utils import secure_filename

class Schedulle(db.Model):
    __tablename__ = "schedulle"
    id = db.Column(db.Integer, primary_key=True)
    begin = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    day = db.Column(db.String(255), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)

    def __init__(self, begin, end, day, group_id):
        self.begin = begin
        self.end = end
        self.day = day
        self.group_id = group_id

    def __repr__(self):
        return f"Schedulle {self.id}"

class SchedulleSchema(ma.Schema):
    class Meta:
        fields = ( 
            "id",
            "begin",
            "end",
            "day",
            "group_id"
        )
    
schedulle_schema = SchedulleSchema()
schedulles_schema = SchedulleSchema(many=True)

class TeacherModel:

    def create_schedulle(self, begin, end, day, group_id):
        new_schedulle = Schedulle(begin, end, day, group_id)
        db.session.add(new_schedulle)
        db.session.commit()
        return schedulle_schema.dump(new_schedulle)

    def schedulle(self, id):
        schedulle = Schedulle.query.get(id)
        return schedulle_schema.dump(schedulle)
    
    def schedulles(self):
        teachers = Schedulle.query.all()
        return schedulles_schema.dump(teachers)
    
    def update_schedulle(self, id, begin, end, day, group_id):
        schedulle = Schedulle.query.get(id)
        schedulle.begin = begin
        schedulle.end = end
        schedulle.day = day
        schedulle.group_id = group_id
        db.session.commit()
        return schedulle_schema.dump(schedulle)

    def delete_schedulle(self, id):
        schedulle = Schedulle.query.get(id)
        db.session.delete(schedulle)
        db.session.commit()
        return schedulle_schema.dump(schedulle)
    