from cgitb import reset
from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma
from flask import jsonify
from werkzeug.utils import secure_filename

from backend.models.Student_model import Student
from backend.models.Group_model import Group

class Participation(db.Model):
    par_id = db.Column(db.Integer, primary_key=True)
    par_date = db.Column(db.Date())
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    par_val = db.Column(db.Integer)

    def __init__(self, par_date, gru_id, std_id, par_val):
        self.par_date = par_date
        self.gru_id = gru_id
        self.std_id = std_id
        self.par_val = par_val
    
class ParticipationSchema(ma.Schema):
    class Meta:
        fields = (
            'par_id',
            'par_date',
            'gru_id',
            'std_id',
            'par_val'
        )
    
participation_schema = ParticipationSchema()
participations_schema = ParticipationSchema(many=True)

db.create_all()

class Participation_Model:
    # Create a participation
    def create_participation(self, par_date, gru_id, std_id, par_val):
        new_participation = Participation(par_date, gru_id, std_id, par_val)
        db.session.add(new_participation)
        db.session.commit()
        result = participation_schema.dump(new_participation)
        return result

    # List participation with ID
    def participation(self, par_id):
        participation = Participation.query.get(par_id)
        result = participation_schema.dump(participation)
        return result

    # List all participations
    def participations(self):
        all_participations = Participation.query.all()
        result = participations_schema.dump(all_participations)
        return result

    # Update participation by ID
    def update_participation(self, par_id, par_date, gru_id, std_id, par_val):
        participation = Participation.query.get(par_id)
        participation.par_date = par_date
        participation.gru_id = gru_id
        participation.std_id = std_id
        participation.par_val = par_val
        db.session.commit()
        result = participation_schema.dump(participation)
        return result

    # Delete participation by ID
    def delete_participation(self, par_id):
        participation = Participation.query.get(par_id)
        db.session.delete(participation)
        db.session.commit()
        return participation_schema.jsonify(participation)   