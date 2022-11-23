from flask_cors import CORS
from database import app

from blueprints.UserType_blueprint import user_type_blueprint
from blueprints.User_blueprint import user_blueprint

app.register_blueprint(user_type_blueprint)
app.register_blueprint(user_blueprint)

cors = CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True)
