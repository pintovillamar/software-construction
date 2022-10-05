from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma

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
        return userType_schema.dump(new_user_type)

    # List user type with ID
    def user_type(self, ust_id):
        # user_type = User_types.query.get(ust_id)
        # return userType_schema.dump(user_type)
        user_type = User_type.query.get(ust_id)
        result = userType_schema.dump(user_type)
        # db.session.commit()
        print(result)
        return jsonify(result)

    # List all user types
    def user_types(self):
        # all_user_types = User_types.query.all()
        # result = userTypes_schema.dump(all_user_types)
        # db.session.commit()
        # return result
        all_users_types = User_type.query.all()
        result = userTypes_schema.dump(all_users_types)
        print(result)
        return result

    # Update user type by ID
    def update_user_type(self, ust_id):
        user_type = User_type.query.get(ust_id)
        user_type.ust_name = User_type.ust_name
        db.session.commit()
        return userType_schema.jsonify(user_type)

    # Delete user type by ID
    def delete_user_type(self, ust_id):
        user_type = User_type.query.get(ust_id)
        db.session.delete(user_type)
        db.session.commit()
        return userType_schema.jsonify(user_type)

