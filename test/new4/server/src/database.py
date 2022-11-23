from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from conn import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

db.init_app(app)

with app.app_context():
    db.create_all()