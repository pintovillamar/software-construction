from flask import jsonify
from database import db
from database import ma
from flask import request
import datetime
import json

from models.Group_model import Group

class Schedule(db.Model):
    sch_id = db.Column(db.Integer, primary_key=True)
    sch_begin = db.Column(db.Time())
    sch_end = db.Column(db.Time())
    sch_day = db.Column(db.String(255))
    sch_created = db.Column(db.DateTime)
    sch_updated = db.Column(db.DateTime)
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, sch_begin, sch_end, sch_day, gru_id, sch_created, sch_updated):
        self.sch_begin = sch_begin
        self.sch_end = sch_end
        self.sch_day = sch_day
        self.gru_id = gru_id
        self.sch_created = sch_created
        self.sch_updated = sch_updated
    
class ScheduleSchema(ma.Schema):
    class Meta:
        fields = (
            'sch_id',
            'sch_begin',
            'sch_end',
            'sch_day',
            'gru_id',
            'sch_created',
            'sch_updated'
        )

schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)

db.create_all()

class Schedule_Model:
    
    # Create a schedule
    def create_schedule(self):
        new_schedule = Schedule(request.json['sch_begin'], 
                                request.json['sch_end'],
                                request.json['sch_day'],
                                request.json['gru_id'],
                                datetime.datetime.now(),
                                datetime.datetime.now())
        db.session.add(new_schedule)
        db.session.commit()
        return schedule_schema.jsonify(new_schedule)
    # List a schedule with ID
    def schedule(self, id):
        schedule = Schedule.query.get(id)
        result = schedule_schema.dump(schedule)
        return result
    
    # List all schedules
    def schedules(self):
        schedules = Schedule.query.all()
        result = schedules_schema.dump(schedules)
        return result

    # Update a schedule
    def update_schedule(self, id):
        schedule = Schedule.query.get(id)
        schedule.sch_begin = request.json['sch_begin']
        schedule.sch_end = request.json['sch_end']
        schedule.sch_day = request.json['sch_day']
        schedule.gru_id = request.json['gru_id']
        schedule.sch_updated = datetime.datetime.now()
        db.session.commit()
        return schedule_schema.jsonify(schedule)

    # Delete a schedule
    def delete_schedule(self, id):
        schedule = Schedule.query.get(id)
        db.session.delete(schedule)
        db.session.commit()
        return schedule_schema.jsonify(schedule)
        
