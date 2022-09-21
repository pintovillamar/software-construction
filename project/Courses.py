from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow

cursor = conn.cursor()

class Course(db.Model):
    cur_id = db.Column(db.Integer, primary_key=True)
    cur_name = db.Column(db.String(70))
    cur_des = db.Column(db.String(150))

    def __init__(self, cur_name, cur_des):
        self.cur_name = cur_name
        self.cur_des = cur_des

db.create_all()

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('cur_id', 'cur_name', 'cur_des')

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

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

@app.route('/course/<cur_id>', methods=['POST'])
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