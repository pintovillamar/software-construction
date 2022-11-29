from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from models.Enroll_model import Enroll_Model

model = Enroll_Model()

enroll_blueprint = Blueprint('/enroll_blueprint', __name__)

@enroll_blueprint.route('/create_enroll', methods=['POST'])
@cross_origin()
def create_enroll():
    return model.create_enroll()

@enroll_blueprint.route('/enroll/<id>', methods=['GET'])
@cross_origin()
def enroll(id):
    return model.enroll(id)

@enroll_blueprint.route('/enrolls', methods=['GET'])
@cross_origin()
def enrolls():
    return model.enrolls()

@enroll_blueprint.route('/update_enroll/<id>', methods=['PUT'])
@cross_origin()
def update_enroll(id):
    return model.update_enroll(id)

@enroll_blueprint.route('/delete_enroll/<id>', methods=['DELETE'])
@cross_origin()
def delete_enroll(id):
    return model.delete_enroll(id)
