from flask import request
from flask import jsonify
from connect import conn, app, db, ma
from Group import Group
from Student import Student

cursor = conn.cursor()

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

#ENDPOINTS

# Create a participation
@app.route('/create_participation', methods=['POST'])
def create_participation():
    print(request.json)

    par_date = request.json['par_date']
    gru_id = request.json['gru_id']
    std_id = request.json['std_id']
    par_val = request.json['par_val']

    new_participation = Participation(par_date, gru_id, std_id, par_val)
    db.session.add(new_participation)
    db.session.commit()

    return participation_schema.jsonify(new_participation)

# Get all participations
@app.route('/participations', methods=['POST'])
def participations():
    all_participations = Participation.query.all()
    result = participations_schema.dump(all_participations)
    return jsonify(result)

# Get a participation
@app.route('/participation/<par_id>', methods=['POST'])
def participation(id):
    participation = Participation.query.get(id)
    return participation_schema.jsonify(participation)

# Update a participation
@app.route('/update_participation/<par_id>', methods=['PUT'])
def update_participation(id):
    participation = Participation.query.get(id)

    par_date = request.json['par_date']
    gru_id = request.json['gru_id']
    std_id = request.json['std_id']
    par_val = request.json['par_val']

    participation.par_date = par_date
    participation.gru_id = gru_id
    participation.std_id = std_id
    participation.par_val = par_val

    db.session.commit()

    return participation_schema.jsonify(participation)

# Delete a participation
@app.route('/delete_participation/<par_id>', methods=['DELETE'])
def delete_participation(id):
    participation = Participation.query.get(id)
    db.session.delete(participation)
    db.session.commit()

    return participation_schema.jsonify(participation)
