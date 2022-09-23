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

    def __init__(self, usr_id, tea_type, tea_cat):
        self.usr_id = usr_id
        self.tea_type = tea_type
        self.tea_cat = tea_cat

db.create_all()

class TeacherSchema(ma.Schema):
    class Meta:
        fields = (
                'tea_id',
                'usr_id', # aqui se pone el usr_id?!??! sí se pone.
                'tea_type',
                'tea_cat'
                )

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)


#Create Teacher
@app.route('/create_teacher', methods=['POST'])
def create_teacher():
    print(request.json)

    usr_id = request.json['usr_id']
    tea_type = request.json['tea_type']
    tea_cat = request.json['tea_cat']
    

    new_teacher = Teacher(usr_id, tea_type, tea_cat)
    db.session.add(new_teacher)
    db.session.commit()

    return teacher_schema.jsonify(new_teacher)


# List all teachers
@app.route('/teachers', methods=['POST'])
def teachers():
    all_teachers = Teacher.query.all()
    result = teachers_schema.dump(all_teachers) # lo vuelve serializable
    return jsonify(result)

# Search for a teacher by id
@app.route('/teacher/<id>', methods=['POST'])
def teacher(id):
    teacher = Teacher.query.get(id)
    result = teacher_schema.dump(teacher)
    return teacher_schema.jsonify(result)


# Update a teacher by id
@app.route('/update_teacher/<id>', methods=['POST'])
def update_teacher(id):
    teacher = Teacher.query.get(id)

    usr_id = request.json['usr_id']
    tea_type = request.json['tea_type']
    tea_cat = request.json['tea_cat']

    teacher.usr_id = usr_id
    teacher.tea_type = tea_type
    teacher.tea_cat = tea_cat

    db.session.commit()
    return teacher_schema.jsonify(teacher)