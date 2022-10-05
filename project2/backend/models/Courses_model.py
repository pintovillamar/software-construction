from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma


class Course(db.Model):
    cur_id = db.Column(db.Integer, primary_key=True)    
    cur_name = db.Column(db.String(70))
    cur_des = db.Column(db.String(70))

    def __init__(self, cur_name, cur_des): # este se usa para el JSON así que guardarlo
        self.cur_name = cur_name
        self.cur_des = cur_des

class CourseSchema(ma.Schema):
    class Meta:
        fields = (
            'cur_id',
            'cur_name',
            'cur_des'
        )

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

db.create_all()

class Courses_Model:
    # Create a course
    def create_course(self, cur_name, cur_des):
        new_course = Course(cur_name, cur_des)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

    # List course with ID
    def course(self, cur_id):
        course = Course.query.get(cur_id)
        return course_schema.dump(course)

    # List all courses
    def courses(self):
        all_courses = Course.query.all()
        result = courses_schema.dump(all_courses)
        db.session.commit()
        return result

    # Update course by ID
    def update_course(self, cur_id):
        course = Course.query.get(cur_id)
        course.cur_name = Course.cur_name
        course.cur_des = Course.cur_des
        db.session.commit()
        return course_schema.jsonify(course)
        
