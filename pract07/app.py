from flask import render_template
from flask_cors import CORS # para que no genere errores de CORS al hacer peticiones
from backend.models.conn import app


from backend.blueprints.User_type_blueprint import user_type_blueprint
from backend.blueprints.User_blueprint import user_blueprint
# from backend.blueprints.Schedule_blueprint import schedule_blueprint
# from backend.blueprints.Enroll_blueprint import enroll_blueprint
from backend.blueprints.Student_blueprint import student_blueprint
# from backend.blueprints.Attendances_blueprint import attendance_blueprint
from backend.blueprints.Group_blueprint import group_blueprint
from backend.blueprints.Course_blueprint import course_blueprint
from backend.blueprints.Teacher_blueprint import teacher_blueprint
# from backend.blueprints.Participation_blueprint import participation_blueprint
# from backend.blueprints.face_recognition_blueprint import face_recognition_blueprint
# test purposes
# from backend.blueprints.test_blueprint import test_blueprint

#app = Flask(__name__)
# para que utilice vue compilado ( npm run build ). En la carpeta dist, esta lo compilado de vue
# app = Flask(__name__,
#             static_folder = "./frontend/dist/static",
#             template_folder = "./frontend/dist")

app.register_blueprint(user_type_blueprint)
app.register_blueprint(user_blueprint)
# app.register_blueprint(schedule_blueprint)
# app.register_blueprint(enroll_blueprint)
app.register_blueprint(student_blueprint)
# app.register_blueprint(attendance_blueprint)
app.register_blueprint(group_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(teacher_blueprint)
# app.register_blueprint(participation_blueprint)
# app.register_blueprint(face_recognition_blueprint)
# app.register_blueprint(test_blueprint)

cors = CORS(app, support_credentials=True)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)