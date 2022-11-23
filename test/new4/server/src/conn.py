from flask import Flask

from database import db, ma

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/prueba"
app.config['SECRET_KEY'] = "lasalle"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False