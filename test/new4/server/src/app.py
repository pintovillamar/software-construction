from flask_cors import CORS

from conn import app

from config import load_dotenv, SECRET_KEY

from blueprints.UserType_blueprint import UserTypeBlueprint

app.register_blueprint(UserTypeBlueprint)

cors = CORS(app, supports_credentials=True)

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)