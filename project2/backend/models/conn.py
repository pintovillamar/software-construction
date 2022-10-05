from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import psycopg2

app = Flask(__name__)
#            static_folder = "./frontend/dist/static",
#            template_folder = "./frontend/dist")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
