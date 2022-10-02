from flask import request
from flask import jsonify
from connect import conn, app, db, ma
from Group import Group
from Student import Student

cursor = conn.cursor()

class Attendance(db.Model):
    att_id = db.Column(db.Integer, primary_key=True)
    att_date = db.Column(db.Date())
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    att_val = db.Column(db.Boolean)

    def __init__(self, att_date, gru_id, std_id, att_val):
        self.att_date = att_date
        self.gru_id = gru_id
        self.std_id = std_id
        self.att_val = att_val
    
class AttendanceSchema(ma.Schema):
    class Meta:
        fields = (
            'att_id',
            'att_date',
            'gru_id',
            'std_id',
            'att_val'
        )

attendance_schema = AttendanceSchema()
attendances_schema = AttendanceSchema(many=True)

db.create_all()

#ENDPOINTS

# Create an attendance
@app.route('/create_attendance', methods=['POST'])
def create_attendance():
    print(request.json)

    att_date = request.json['att_date']
    gru_id = request.json['gru_id']
    std_id = request.json['std_id']
    att_val = request.json['att_val']

    new_attendance = Attendance(att_date, gru_id, std_id, att_val)
    db.session.add(new_attendance)
    db.session.commit()

    return attendance_schema.jsonify(new_attendance)

# Get all attendances
@app.route('/attendances', methods=['POST'])
def attendances():
    all_attendances = Attendance.query.all()
    result = attendances_schema.dump(all_attendances)
    return jsonify(result)

# Get an attendance by id
@app.route('/attendance/<att_id>', methods=['POST'])
def attendance(att_id):
    attendance = Attendance.query.get(att_id)
    return attendance_schema.jsonify(attendance)

# Update an attendance
@app.route('/attendance/<att_id>', methods=['PUT'])
def update_attendance(att_id):
    attendance = Attendance.query.get(att_id)

    att_date = request.json['att_date']
    gru_id = request.json['gru_id']
    std_id = request.json['std_id']
    att_val = request.json['att_val']

    attendance.att_date = att_date
    attendance.gru_id = gru_id
    attendance.std_id = std_id
    attendance.att_val = att_val

    db.session.commit()
    return attendance_schema.jsonify(attendance)

# Delete an attendance
@app.route('/delete_attendance/<att_id>', methods=['DELETE'])
def delete_attendance(att_id):
    attendance = Attendance.query.get(att_id)
    db.session.delete(attendance)
    db.session.commit()

    return attendance_schema.jsonify(attendance)


