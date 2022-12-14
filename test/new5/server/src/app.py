from flask_cors import CORS
from database import app

from blueprints.UserType_blueprint import user_type_blueprint
from blueprints.User_blueprint import user_blueprint
from blueprints.Teacher_blueprint import teacher_blueprint
from blueprints.Course_blueprint import course_blueprint
from blueprints.Group_blueprint import group_blueprint
from blueprints.Student_blueprint import student_blueprint
from blueprints.Enroll_blueprint import enroll_blueprint
from blueprints.Schedule_blueprint import schedule_blueprint

app.register_blueprint(user_type_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(teacher_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(group_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(enroll_blueprint)
app.register_blueprint(schedule_blueprint)

cors = CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True)
