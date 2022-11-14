from flask_cors import CORS

from conn import app

from config import load_dotenv, SECRET_KEY

#### Tests ####
# from blueprints.test_blueprint import TestBlueprint
#### Tests ####

from blueprints.UserType_blueprint import UserTypeBlueprint
from blueprints.User_blueprint import UserBlueprint
from blueprints.Student_blueprint import StudentBlueprint
from routes.auth import routes_auth
# from blueprints.test_blueprint import TestBlueprint

app.register_blueprint(UserTypeBlueprint)
app.register_blueprint(UserBlueprint)
app.register_blueprint(routes_auth)
# app.register_blueprint(StudentBlueprint)
# app.register_blueprint(TestBlueprint)

cors = CORS(app, supports_credentials=True)

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)