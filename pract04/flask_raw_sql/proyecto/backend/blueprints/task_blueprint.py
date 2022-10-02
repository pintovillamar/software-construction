from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel
model = TaskModel()
#from backend.models.task_model_pg import TaskModelPG
#model = TaskModelPG()

task_blueprint = Blueprint('task_blueprint', __name__)



@task_blueprint.route('/task/create_task', methods=['POST'])
@cross_origin()
def create_task():
    content = model.create_task(request.json['title'], request.json['description'])    
    return jsonify(content)

@task_blueprint.route('/task/delete_task', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_task(int(request.json['id'])))

@task_blueprint.route('/task/get_task', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_task(int(request.json['id'])))

@task_blueprint.route('/task/get_tasks', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_tasks())


@task_blueprint.route('/task/upload_photo', methods = ['GET', 'POST'])
@cross_origin()
def upload_file():
    

    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save("/home/vicente/Downloads/" + filename)

        # luego guardar en la base de datos. Solo se guarda el directorio

        return "OK"
