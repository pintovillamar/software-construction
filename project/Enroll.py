from flask import request
from flask import jsonify
from connect import conn, app, db, ma
from Student import Student
from Group import Group

cursor = conn.cursor()

class Enroll(db.Model):
    enr_id = db.Column(db.Integer, primary_key=True)
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    enr_date = db.Column(db.Date())

    def __init__(self, std_id, gru_id, enr_date):
        self.std_id = std_id
        self.gru_id = gru_id
        self.enr_date = enr_date

class EnrollSchema(ma.Schema):
    class Meta:
        fields = (
            'enr_id',
            'std_id',
            'gru_id',
            'enr_date'
        )
    
enroll_schema = EnrollSchema()
enrolls_schema = EnrollSchema(many=True)

db.create_all()

#ENDPOINTS

# Create an enrollment
@app.route('/create_enroll', methods=['POST'])
def create_enroll():
    print(request.json)

    std_id = request.json['std_id']
    gru_id = request.json['gru_id']
    enr_date = request.json['enr_date']

    new_enroll = Enroll(std_id, gru_id, enr_date)
    db.session.add(new_enroll)
    db.session.commit()

    return enroll_schema.jsonify(new_enroll)

# Get all enrollments
@app.route('/enrolls', methods=['POST'])
def enrolls():
    all_enrolls = Enroll.query.all()
    result = enrolls_schema.dump(all_enrolls)
    return jsonify(result)

# Get an enrollment
@app.route('/enroll/<enr_id>', methods=['POST'])
def enroll(id):
    enroll = Enroll.query.get(id)
    return enroll_schema.jsonify(enroll)

# Update an enrollment
@app.route('/update_enroll/<enr_id>', methods=['PUT'])
def update_enroll(id):
    enroll = Enroll.query.get(id)

    std_id = request.json['std_id']
    gru_id = request.json['gru_id']
    enr_date = request.json['enr_date']

    enroll.std_id = std_id
    enroll.gru_id = gru_id
    enroll.enr_date = enr_date

    db.session.commit()
    return enroll_schema.jsonify(enroll)
