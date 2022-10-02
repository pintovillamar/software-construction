from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow

cursor = conn.cursor()

class User_type(db.Model):
    ust_id = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(70))

    def __init__(self, ust_name):
        self.ust_name = ust_name

class User_typeSchema(ma.Schema):
    class Meta:
        fields = (
            'ust_id',
            'ust_name'
        )

user_type_schema = User_typeSchema()
user_types_schema = User_typeSchema(many=True)

db.create_all() 

# to-dos
# 1 create a new file for the endpoints

# Create user_type
@app.route('/create_user_type', methods=['POST'])
def create_user_type():
    print(request.json)

    ust_name = request.json['ust_name']

    new_user_type = User_type(ust_name)
    db.session.add(new_user_type)
    db.session.commit()

    return user_type_schema.jsonify(new_user_type)


# List all user_types
@app.route('/user_types', methods=['POST'])
def user_types():
    all_user_types = User_type.query.all()
    result = user_types_schema.dump(all_user_types)
    return jsonify(result)


# Search for a user_type by id
@app.route('/user_type/<id>', methods=['POST'])
def user_type(id):
    user_type = User_type.query.get(id)
    result = user_type_schema.dump(user_type)
    return user_type_schema.jsonify(result)


# Update user_type
@app.route('/update_user_type/<id>', methods=['POST'])
def update_user_type(id):
    user_type = User_type.query.get(id)

    ust_name = request.json['ust_name']

    user_type.ust_name = ust_name

    db.session.commit()

    return user_type_schema.jsonify(user_type)


# Delete user_type
@app.route('/delete_user_type/<id>', methods=['POST'])
def delete_user_type(id):
    user_type = User_type.query.get(id)
    db.session.delete(user_type)
    db.session.commit()

    return user_type_schema.jsonify(user_type)

# Get users by user_type (students)
@app.route('/get_students',methods=['POST'])
def get_students():
    sql='select * from "user" where "ust_id"=2'

    cursor.execute(sql)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'name': result[4], 'last_name': result[5], 'user_type': result[8]}
        data.append(content)
        content = {}
    return jsonify(data)

# get users by user_type (teachers)
@app.route('/get_teachers',methods=['POST'])
def get_teachers():
    sql='select * from "user" where "ust_id"=3'

    cursor.execute(sql)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'name': result[4], 'last_name': result[5], 'user_type': result[8]}
        data.append(content)
        content = {}
    return jsonify(data)