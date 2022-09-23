from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@127.0.0.1:3307/flaskmysql"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning



db = SQLAlchemy(app)
ma = Marshmallow(app)

# tabla task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=False)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description


db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/create_task', methods=['POST'])
def create_task():
    print(request.json)

    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task) # respondemos cpon la tarea creada

@app.route('/tasks', methods=['POST'])
def tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks) # lo vuelve serializable
    return jsonify(result)

@app.route('/task/<id>', methods=['POST'])
def task(id):
    result = Task.query.get(id)
    result = task_schema.dump(result) # lo vuelve serializable
    return jsonify(result)

@app.route('/update_task/<id>', methods=['POST'])
def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    description = request.json['description']

    task.title = title
    task.description = description

    db.session.commit()
    return task_schema.jsonify(task)


@app.route('/delete_task/<id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
