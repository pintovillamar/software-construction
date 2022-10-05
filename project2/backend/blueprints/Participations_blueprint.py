import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 

from backend.models.Participations_Model import Participations_Model
model = Participations_Model()

participations_blueprint = Blueprint('/participations_blueprint', __name__)

# Create a participation
@participations_blueprint.route('/create_participations', methods=['POST'])
@cross_origin()
def create_participations():
    print(request.json['par_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['par_val'])
    content = model.create_participations(request.json['par_date'])
    content = model.create_participations(request.json['gru_id'])    
    content = model.create_participations(request.json['std_id'])
    content = model.create_participations(request.json['par_val'])    
    return jsonify(content)

# List participation with ID
@participations_blueprint.route('/participation/<par_id>', methods=['POST'])
@cross_origin()
def participation(par_id):
    print(request.json['par_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['par_val'])
    content = model.participation(request.json[par_id])
    return jsonify(content)
    #return jsonify(model.participation(int(request.json['par_id'])))

# List all participations
@participations_blueprint.route('/participations', methods=['POST'])
@cross_origin()
def participations():
    return jsonify(model.participations())

# Update participation by ID
@participations_blueprint.route('/update_participation/<par_id>', methods=['POST'])
@cross_origin()
def update_participation(par_id):
    # return jsonify(model.update_participation(int(request.json['par_id']), request.json['name']))
    content = model.update_participation(request.json['par_date'])
    content = model.update_participation(request.json['gru_id'])
    content = model.update_participation(request.json['std_id'])
    content = model.update_participation(request.json['par_val'])
    return jsonify(content)

# @participation_blueprint.route('/delete_participation', methods=['POST'])
# @cross_origin()
# def delete_participation():
#     return jsonify(model.delete_participation(int(request.json['id'])))