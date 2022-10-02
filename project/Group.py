from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow
from Teacher import Teacher # from Teacher.py import Teacher ForeignKey use only
from Courses import Course # from Course.py import Course ForeignKey use only

cursor = conn.cursor()

class Group(db.Model):
    gru_id = db.Column(db.Integer, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))
    gru_name = db.Column(db.String(70))
    cur_id = db.Column(db.Integer, db.ForeignKey(Course.cur_id))

    def __init__(self, tea_id, gru_name, cur_id):
        self.tea_id = tea_id
        self.gru_name = gru_name
        self.cur_id = cur_id

class GroupSchema(ma.Schema):
    class Meta:
        fields = (
            'gru_id',
            'tea_id',
            'gru_name',
            'cur_id'
        )

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

db.create_all()


#ENDPOINTS
@app.route('/create_group', methods=['POST'])
def create_group():
    print(request.json)

    tea_id = request.json['tea_id']
    gru_name = request.json['gru_name']
    cur_id = request.json['cur_id']

    new_group = Group(tea_id, gru_name, cur_id)
    db.session.add(new_group)
    db.session.commit()

    return group_schema.jsonify(new_group)

@app.route('/groups', methods=['POST'])
def groups():
    all_groups = Group.query.all()
    result = groups_schema.dump(all_groups) # lo vuelve serializable
    return jsonify(result)

@app.route('/group/<gru_id>', methods=['POST'])
def group(gru_id):
    result = Group.query.get(gru_id)
    result = group_schema.dump(result) # lo vuelve serializable
    return jsonify(result)

@app.route('/update_group/<gru_id>', methods=['POST'])
def update_group(gru_id):
    group = Group.query.get(gru_id)
    tea_id = request.json['tea_id']
    gru_name = request.json['gru_name']
    cur_id = request.json['cur_id']

    group.tea_id = tea_id 
    group.gru_name = gru_name
    group.cur_id = cur_id

    db.session.commit()
    return group_schema.jsonify(group)

@app.route('/delete_group/<id>', methods=['POST'])
def delete_group(gru_id):
    group = Group.query.get(gru_id)
    db.session.delete(group)
    db.session.commit()
    return group_schema.jsonify(group)

