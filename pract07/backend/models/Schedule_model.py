from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

# Import FKs
from backend.models.Group_model import Group

class Schedule(db.Model):
    sch_id = db.Column(db.Integer, primary_key=True)
    sch_begin = db.Column(db.Time())
    sch_end = db.Column(db.Time())
    sch_day = db.Column(db.String(70))
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, sch_begin, sch_end, sch_day, gru_id):
        self.sch_begin = sch_begin
        self.sch_end = sch_end
        self.sch_day = sch_day
        self.gru_id = gru_id
    
class ScheduleSchema(ma.Schema):
    class Meta:
        fields = (
            'sch_id',
            'sch_begin',
            'sch_end',
            'sch_day',
            'gru_id'
        )

schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)

db.create_all()

class Schedule_Model:
    
    # Create a schedule
    def create_schedule(self, sch_begin, sch_end, sch_day, gru_id):
        new_schedule = Schedule(sch_begin, sch_end, sch_day, gru_id)
        db.session.add(new_schedule)
        db.session.commit()
        result = schedule_schema.dump(new_schedule)
        return result

    # List a schedule with ID
    def schedule(self, sch_id):
        schedule = Schedule.query.get(sch_id)
        result = schedule_schema.dump(schedule)
        return result
    
    # List all schedules
    def schedules(self):
        all_schedules = Schedule.query.all()
        result = schedules_schema.dump(all_schedules)
        return result

    # Update a schedule
    def update_schedule(self, sch_id, sch_begin, sch_end, sch_day, gru_id):
        schedule = Schedule.query.get(sch_id)
        schedule.sch_begin = sch_begin
        schedule.sch_end = sch_end
        schedule.sch_day = sch_day
        schedule.gru_id = gru_id
        db.session.commit()
        result = schedule_schema.dump(schedule)
        return result

    # Delete a schedule
    def delete_schedule(self, sch_id):
        schedule = Schedule.query.get(sch_id)
        db.session.delete(schedule)
        db.session.commit()
        return schedule_schema.jsonify(schedule)
        

    