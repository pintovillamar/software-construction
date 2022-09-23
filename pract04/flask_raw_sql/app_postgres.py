from flask import Flask
from flask import request
from flask import jsonify
import psycopg2

#libraries: sudo pip3 install psycopg2-binary

app = Flask(__name__)

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="flask",
    user="postgres",
    password="Pass.123$")

cursor = conn.cursor()

@app.route('/create_task', methods=['POST'])
def create_task():
    print(request.json)

    params = {
        'title' : request.json['title'],
        'description' : request.json['description']
    }
    query = """insert into task (title, description) 
         values (%(title)s, %(description)s) RETURNING id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {'id': id_of_new_row, 'title': params['title'], 'description': params['description']}
    return jsonify(content)

@app.route('/tasks', methods=['POST'])
def tasks():
    cursor.execute("SELECT * from task")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'title': result[1], 'description': result[2]}
        data.append(content)
        content = {}
    return jsonify(data)


@app.route('/task/<id>', methods=['POST'])
def task(id):
    cursor.execute("SELECT * from task where id="+id)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'title': result[1], 'description': result[2]}
        data.append(content)
        content = {}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)