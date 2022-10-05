from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma

# Import FKs
from project2.backend.models.User_types_model import User_type

class User(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_dni = db.Column(db.String(8))
    usr_pass = db.Column(db.String(16))
    usr_photo = db.Column(db.String(70))
    usr_name = db.Column(db.String(70))
    usr_last_name = db.Column(db.String(70))
    usr_dob = db.Column(db.Date()) # date of birth
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

