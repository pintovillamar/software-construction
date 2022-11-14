from flask import Flask

from database import db, ma

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/app1"
app.config['SECRET_KEY'] = "lasalle"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

with app.app_context():
    db.create_all()