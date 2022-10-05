from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma

# Import FKs
from project2.backend.models.Teachers_model import Teacher
from project2.backend.models.Courses_model import Course

class Group(db.Model):
    gru_id = db.Column(db.Integer, primary_key=True)    
    tea_id = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))
    gru_name = db.Column(db.String(70))
    cur_id = db.Column(db.Integer, db.ForeignKey(Course.cur_id))

    def __init__(self, tea_id, gru_name, cur_id): # este se usa para el JSON así que guardarlo
        self.tea_id = tea_id
        self.gru_name = gru_name
        self.cur_id = cur_id

class GroupSchema(ma.Schema):
    class Meta:
        fields = (
            'gru_id',
            'tea_id',
            'gru_name',
            'cur_id'
        )

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

db.create_all()

class Groups_Model:
    # Create a group
    def create_group(self, tea_id, gru_name, cur_id):
        new_group = Group(tea_id, gru_name, cur_id)
        db.session.add(new_group)
        db.session.commit()
        return group_schema.dump(new_group)

    # List group with ID
    def group(self, gru_id):
        group = Group.query.get(gru_id)
        return group_schema.dump(group)

    # List all groups
    def groups(self):
        all_groups = Group.query.all()
        result = groups_schema.dump(all_groups)
        db.session.commit()
        return result

    # Update group by ID
    def update_group(self, gru_id):
        group = Group.query.get(gru_id)
        group.tea_id = Group.tea_id
        group.gru_name = Group.gru_name
        group.cur_id = Group.cur_id
        db.session.commit()
        return group_schema.jsonify(group)
        
