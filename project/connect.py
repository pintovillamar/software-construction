from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="prueba",
    user="postgres",
    password="1234")

cursor = conn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@127.0.0.1:5432/prueba"
flag = app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)