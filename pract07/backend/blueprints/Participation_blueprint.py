import json
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin 

from backend.models.Participation_model import Participation_Model
model = Participation_Model()

participation_blueprint = Blueprint('/participations_blueprint', __name__)

# Create a participation
@participation_blueprint.route('/create_participation', methods=['POST'])
@cross_origin()
def create_participation():
    print(request.json['par_date'])
    print(request.json['gru_id'])
    print(request.json['std_id'])
    print(request.json['par_val'])
    content = model.create_participation(request.json['par_date']
                                        ,request.json['gru_id']
                                        ,request.json['std_id']
                                        ,request.json['par_val'])
    return jsonify(content)

# List participation with ID
@participation_blueprint.route('/participation/<par_id>', methods=['POST'])
@cross_origin()
def participation(par_id):
    content = model.participation(par_id)
    return jsonify(content)

# List all participations
@participation_blueprint.route('/participations', methods=['POST'])
@cross_origin()
def participations():
    content = model.participations()
    return jsonify(content)

# Update participation by ID
@participation_blueprint.route('/update_participation/<par_id>', methods=['POST'])
@cross_origin()
def update_participation(par_id):
    
    content = model.update_participation(par_id,
                                            request.json['par_date'],
                                            request.json['gru_id'],
                                            request.json['std_id'],
                                            request.json['par_val'])
    return jsonify(content)

# Delete participation by ID
@participation_blueprint.route('/delete_participation/<par_id>', methods=['POST'])
@cross_origin()
def delete_participation(par_id):
    model.delete_participation(par_id)
    return f"Participation {par_id} deleted succsesfully"