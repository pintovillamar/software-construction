from psycopg2.pool import SimpleConnectionPool
from flask import Flask
from flask_sqlalchemy import SQLAlchemy as db
from flask_marshmallow import Marshmallow as ma
from contextlib import contextmanager

dbConnection = "dbname='prueba' user='postgres' host='localhost' password='1234'"

# pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)

if __name__ == "__main__":
    try:
        # with here will take care of put connection when its done
        with getcursor() as cur:
            cur.execute("select * from user_type")
            result_set = cur.fetchall()

        for result in result_set:
            print(result)

    except Exception as e:
        print("error in executing with exception: ", e)