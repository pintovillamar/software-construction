from flask import Flask
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

#libraries: pip3 install flask-mysql

app = Flask(__name__)
#app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'flaskmysql'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

@app.route('/create_task', methods=['POST'])
@cross_origin()
def create_task():   
    params = {
        'title' : request.json['title'],
        'description' : request.json['description']
    }
    
    query = """insert into task (title, description) 
         values (%(title)s, %(description)s)"""
    cursor.execute(query, params)
    conn.commit()

    content = {'id': cursor.lastrowid, 'title': params['title'], 'description': params['description']}
    return jsonify(content)

@app.route('/delete_task', methods=['POST'])
@cross_origin()
def delete_task():  
    params = {
        'id' : int(request.json['id'])
    }
    
    query = """delete from task where id = %(id)s"""         
    cursor.execute(query, params)
    conn.commit()

    content = {'result': 1}
    return jsonify(content)

@app.route('/tasks', methods=['POST'])
@cross_origin()
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