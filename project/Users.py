class User_type(db.Model):
    ust_id = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(70))

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

class User(ma.Schema):
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