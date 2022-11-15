from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

class User_type(db.Model):
    ust_id = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(70))

    def __init__(self, ust_name):
        self.ust_name = ust_name

class UserTypeSchema(ma.Schema):
    class Meta:
        fields = ('ust_id', 'ust_name')
        
userType_schema = UserTypeSchema()
userTypes_schema = UserTypeSchema(many=True)


db.create_all()


class User_Type_Model:
    # Create a user type
    def create_user_type(self, ust_name):
        new_user_type = User_type(ust_name)
        db.session.add(new_user_type)
        db.session.commit()
        result = userType_schema.dump(new_user_type)
        return result

    # List user type with ID
    def user_type(self, ust_id):
        user_type = User_type.query.get(ust_id)
        result = userType_schema.dump(user_type)
        return result

    # List all user types
    def user_types(self):
        all_users_types = User_type.query.all()
        result = userTypes_schema.dump(all_users_types)
        return result

    # Update user type by ID
    def update_user_type(self, ust_id, ust_name):
        user_type = User_type.query.get(ust_id)
        user_type.ust_name = ust_name
        db.session.commit()
        result = userType_schema.dump(user_type)
        return result

    # Delete user type by ID
    def delete_user_type(self, ust_id):
        user_type = User_type.query.get(ust_id)
        # user_type.ust_name = ust_name
        db.session.delete(user_type)
        db.session.commit()
        return userType_schema.jsonify(user_type)

        # to do 
        # 1. return json with ust_id AND ust_name

