from flask import Blueprint
from flask_cors import cross_origin

from models.Schedule_model import Schedule_Model
model = Schedule_Model()

schedule_blueprint = Blueprint('/schedule_blueprint', __name__)

@schedule_blueprint.route('/create_schedule', methods=['POST'])
@cross_origin()
def create_schedule():
    return model.create_schedule()

@schedule_blueprint.route('/schedule/<id>', methods=['GET'])
@cross_origin()
def schedule(id):
    return model.schedule(id)

@schedule_blueprint.route('/schedules', methods=['GET'])
@cross_origin()
def schedules():
    return model.schedules()

@schedule_blueprint.route('/update_schedule/<id>', methods=['PUT'])
@cross_origin()
def update_schedule(id):
    return model.update_schedule(id)

@schedule_blueprint.route('/delete_schedule/<id>', methods=['DELETE'])
@cross_origin()
def delete_schedule(id):
    return model.delete_schedule(id)

