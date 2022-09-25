from flask import request
from flask import jsonify
from connect import conn # import conn de connect
from connect import app
from connect import db, ma # SQLAlchemy Marshmelow
from UserType import User_type # from UserType.py import User_type ForeignKey use only

cursor = conn.cursor()

class User(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_dni = db.Column(db.String(8))
    usr_pass = db.Column(db.String(16))
    usr_photo = db.Column(db.String(70))
    usr_name = db.Column(db.String(70))
    usr_last_name = db.Column(db.String(70))
    usr_dob = db.Column(db.Date())# dia de nacimiento
    usr_email = db.Column(db.String(70))
    ust_id = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id): # este se usa para el JSON así que guardarlo
        self.usr_dni = usr_dni
        self.usr_pass = usr_pass
        self.usr_photo = usr_photo
        self.usr_name = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dob = usr_dob
        self.usr_email = usr_email
        self.ust_id = ust_id

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
            'ust_id'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()

# to-dos
# 1 create a new file for the endpoints


# Create user
@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.json)

    usr_dni = request.json['usr_dni']
    usr_pass = request.json['usr_pass']
    usr_photo = request.json['usr_photo']
    usr_name = request.json['usr_name']
    usr_last_name = request.json['usr_last_name']
    usr_dob = request.json['usr_dob']
    usr_email = request.json['usr_email']
    ust_id = request.json['ust_id']

    new_user = User(usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, ust_id)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# List all users
@app.route('/users', methods=['POST'])
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Search for a user by id
@app.route('/user/<id>', methods=['POST'])
def user(id):
    user = User.query.get(id)
    result = user_schema.dump(user)
    return user_schema.jsonify(result)

# Update a user by id
@app.route('/update_user/<id>', methods=['POST'])
def update_user(usr_id):
    user = User.query.get(usr_id)

    usr_dni = request.json['usr_dni']
    usr_pass = request.json['usr_pass']
    usr_photo = request.json['usr_photo']
    usr_name = request.json['usr_name']
    usr_last_name = request.json['usr_last_name']
    usr_dob = request.json['usr_dob']
    usr_email = request.json['usr_email']
    user_type_ust_id = request.json['user_type_ust_id']

    user.usr_dni = usr_dni
    user.usr_pass = usr_pass
    user.usr_photo = usr_photo
    user.usr_name = usr_name
    user.usr_last_name = usr_last_name
    user.usr_dob = usr_dob
    user.usr_email = usr_email
    user.usr_type_ust_id = user_type_ust_id

    db.session.commit()

    return user_schema.jsonify(user)

# Delete user
@app.route('/delete_user/<id>', methods=['POST'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)





