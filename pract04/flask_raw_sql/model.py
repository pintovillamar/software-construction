from flask import Flask
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL

#libraries: pip3 install flask-mysql

class Model:
    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'Pass.123$'
        app.config['MYSQL_DATABASE_DB'] = 'flaskmysql'
        app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
        self.mysql.init_app(app)

        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()

    def create_task(self, title, description):  
        params = {
            'title' : title,
            'description' : description
        }
        query = """insert into task (title, description) 
            values (%(title)s, %(description)s)"""
        self.cursor.execute(query, params)
        self.conn.commit()

        data = {'id': self.cursor.lastrowid, 'title': title, 'description': description}
        return data

    def get_task(self, id):  
        self.cursor.execute("SELECT * from task where id="+id)
        rv = self.cursor.fetchall()

        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'title': result[1], 'description': result[2]}
            data.append(content)
            content = {}

        return data
