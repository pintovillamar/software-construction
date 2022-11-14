import os

from dotenv import load_dotenv

def build_database_uri() -> str:
    # host = os.environ("DB_HOST")
    # port = os.environ("DB_PORT")
    # user = os.environ("DB_USER")
    # password = os.environ("DB_PASSWORD")
    # database = os.environ("DB_DATABASE")
    user = "postgres"
    host = "localhost"
    database = "prueba2"
    password = "1234"

    return f'postgresql://{user}@{host}/{database}'

def build_secret_key() -> str:
    return f"lasalle"

def build_sqlalchemy_track_modifications() -> bool:
    track = False
    return track


DATABASE_URI = build_database_uri()
SECRET_KEY = build_secret_key()
TRACK_MODIFICATIONS = build_sqlalchemy_track_modifications() 