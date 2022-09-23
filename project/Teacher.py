from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow

cursor = conn.cursor()

class Teacher(db.Model):
    tea_id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.String(70))
    tea_type = db.Column(db.String(70))
    tea_cat = db.Column(db.String(70))

    def __init__(self, tea_type, tea_cat):
        # se pone el usr_id y el tea_id??!?
        self.tea_type = tea_type
        self.tea_cat = tea_cat

db.create_all()

class TeacherSchema(ma.Schema):
    class Meta:
        fields = (
                'tea_id',
                'usr_id', # aqui se pone el usr_id?!??!
                'tea_type',
                'tea_cat'
                )

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)

@app.route('/create_teacher', methods=['POST'])
def create_course():
    print(request.json)

    tea_id = request.json['tea_id']
    usr_id = request.json['usr_id']
    tea_type = request.json['tea_type']
    tea_cat = request.json['tea_cat']
    

    new_teacher = Teacher(tea_id, usr_id, tea_type, tea_cat)
    db.session.add(new_teacher)
    db.session.commit()

    return teacher_schema.jsonify(new_teacher)

@app.route('/teachers', methods=['POST'])
def teachers():
    all_teachers = Teacher.query.all()
    result = teachers_schema.dump(all_teachers) # lo vuelve serializable
    return jsonify(result)