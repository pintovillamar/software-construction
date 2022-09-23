from flask import Flask
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL

from model import Model

#libraries: pip3 install flask-mysql
app = Flask(__name__)
model = Model(app)

@app.route('/create_task', methods=['POST'])
def create_task():
    content = model.create_task(request.json['title'], request.json['description'])    
    return jsonify(content)

@app.route('/task/<id>', methods=['POST'])
def tasks(id):
    return jsonify(model.get_task(id))


if __name__ == "__main__":
    app.run(debug=True)