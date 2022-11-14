from jwt import decode, encode, exceptions
from datetime import datetime, timedelta
from os import getenv
from flask import jsonify


def expiration_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)

    return new_date

def write_token(data: dict):
    token = encode(payload={**data,"exp" : expiration_date(2)}, key=getenv("SECRET_KEY"), algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        return response