from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow
from User import User # from User import User ForeingKey use only

cursor = conn.cursor()

class Student(db.Model):
    std_id = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean())
    std_year = db.Column(db.Date())
    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, usr_id, std_regular, std_year):
        self.usr_id = usr_id
        self.std_regular = std_regular
        self.std_year = std_year
        

db.create_all()

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'std_id',
            'usr_id',
            'std_regular',
            'std_year'
        )

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


#Create Teacher
@app.route('/create_student', methods=['POST'])
def create_student():
    print(request.json)

    usr_id = request.json['user_usr_id']
    std_regular = request.json['std_regular']
    std_year = request.json['std_year']

    new_student = Student(usr_id, std_regular, std_year)
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)


# List all teachers
@app.route('/students', methods=['POST'])
def students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students) # lo vuelve serializable
    return jsonify(result)


# Search for a teacher by id
@app.route('/student/<std_id>', methods=['POST'])
def student(std_id):
    result = Student.query.get(std_id)
    result = student_schema.dump(result) # lo vuelve serializable
    return jsonify(result)


# Update a teacher by id
@app.route('/update_student/<std_id>', methods=['POST'])
def update_student(std_id):
    student = Student.query.get(std_id)
    std_regular = request.json['std_regular']
    std_year = request.json['std_year']

    student.std_regular = std_regular 
    student.std_year = std_year

    db.session.commit()
    return student_schema.jsonify(student)


# Delete a teacher by id
@app.route('/delete_student/<std_id>', methods=['POST'])
def delete_student(std_id):
    student = Student.query.get(std_id)
    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)

# ## SELECT * FROM STUDENT

# @app.route('/select_students', methods=['POST'])
# def select_students():
#     cursor.execute("select * from student")
#     #data = cursor.fetchone() # obtiene un registro
#     rv = cursor.fetchall()

#     data = []
#     content = {}
#     for result in rv:
#         content = {'std_regular': result[0], 'std_id': result[1], 'std_year': result[2]}
#         data.append(content)
#         content = {}
#     return jsonify(data)
