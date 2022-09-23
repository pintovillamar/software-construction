from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="prueba",
    user="postgres",
    password="1234")

cursor = conn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@127.0.0.1:5432/prueba"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Group(db.Model):
    gru_id = db.Column(db.Integer, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))
    gru_name = db.Column(db.String(70))
    cur_id = db.Column(db.Integer, db.ForeignKey(Course.cur_id))

class Group(ma.Schema):
    class Meta:
        fields = (
            'gru_id',
            'tea_id',
            'gru_name',
            'cur_id'
        )


#COURSE
class Course(db.Model):
    cur_id = db.Column(db.Integer, primary_key=True)
    cur_name = db.Column(db.String(70))
    cur_des = db.Column(db.String(150))

    def __init__(self, cur_name, cur_des):
        self.cur_name = cur_name
        self.cur_des = cur_des

#db.create_all()

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('cur_id', 'cur_name', 'cur_des')

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


#TEACHER
class Teacher(db.Model):
    tea_id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))
    tea_type = db.Column(db.String(150))
    tea_cat = db.Column(db.String(150))

    def __init__(self, tea_type, tea_cat):
        self.tea_type = tea_type
        self.tea_cat = tea_cat

#db.create_all()

class TeacherSchema(ma.Schema):
    class Meta:
        fields = ('tea_id', 'usr_id', 'tea_type', 'tea_cat')

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)


#USER
class User(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_dni = db.Column(db.String(8))
    usr_pass = db.Column(db.String(16))
    usr_photo = db.Column(db.String(70))
    usr_name = db.Column(db.String(70))
    usr_last_name = db.Column(db.String(70))
    usr_dob = db.Column(db.Date())# dia de nacimiento
    usr_email = db.Column(db.String(70))
    user_type_ust_id = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email):
        self.usr_dni = usr_dni
        self.usr_pass = usr_pass
        self.usr_photo = usr_photo
        self.usr_name = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dob = usr_dob
        self.usr_email = usr_email

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'usr_id',
            'usr_dni',
            'usr_pass',
            'usr_photo',
            'usr_name',
            'usr_last_name',
            'usr_dob',
            'usr_email',
            'user_type_ust_id'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)


#ENDPOINTS
@app.route('/create_course', methods=['POST'])
def create_course():
    print(request.json)

    cur_name = request.json['cur_name']
    cur_des = request.json['cur_des']

    new_course = Course(cur_name, cur_des)
    db.session.add(new_course)
    db.session.commit()

    return course_schema.jsonify(new_course)

@app.route('/courses', methods=['POST'])
def courses():
    all_courses = Course.query.all()
    result = courses_schema.dump(all_courses) # lo vuelve serializable
    return jsonify(result)

@app.route('/course/<id>', methods=['POST'])
def course(cur_id):
    result = Course.query.get(cur_id)
    result = course_schema.dump(result) # lo vuelve serializable
    return jsonify(result)

@app.route('/update_course/<id>', methods=['POST'])
def update_course(cur_id):
    course = Course.query.get(cur_id)
    cur_name = request.json['cur_name']
    cur_des = request.json['cur_des']

    course.cur_name = cur_name 
    course.cur_des = cur_des

    db.session.commit()
    return course_schema.jsonify(course)

@app.route('/delete_course/<id>', methods=['POST'])
def delete_course(cur_id):
    course = Course.query.get(cur_id)
    db.session.delete(course)
    db.session.commit()
    return course_schema.jsonify(course)

## SELECT * FROM COURSE

@app.route('/select_courses', methods=['POST'])
def select_courses():
    cursor.execute("select * from course")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'cur_name': result[0], 'cur_id': result[1], 'cur_des': result[2]}
        data.append(content)
        content = {}
    return jsonify(data)

@app.route('/create_user_type', methods=['POST'])
def create_user_type():
    print(request.json)

    cur_name = request.json['ust_id']
    cur_des = request.json['ust_name']

    new_course = Course(cur_name, cur_des)
    db.session.add(new_course)
    db.session.commit()

    return course_schema.jsonify(new_course)



if __name__ == "__main__":
    app.run(debug=True)