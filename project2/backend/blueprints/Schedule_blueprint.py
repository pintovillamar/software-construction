from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from backend.models.Schedule_model import Schedule_Model
model = Schedule_Model()

schedule_blueprint = Blueprint('/schedule_blueprint', __name__)

# Create a schedule
@schedule_blueprint.route('/create_schedule', methods=['POST'])
@cross_origin()
def create_schedule():
    content = model.create_schedule(request.json['sch_begin'],
                                    request.json['sch_end'],
                                    request.json['sch_day'],
                                    request.json['gru_id'])    
    return jsonify(content)

# List schedule with ID
@schedule_blueprint.route('/schedule/<sch_id>', methods=['POST'])
@cross_origin()
def schedule(sch_id):
    content = model.schedule(sch_id)
    return jsonify(content)

# List all schedules
@schedule_blueprint.route('/schedules', methods=['POST'])
@cross_origin()
def schedules():
    content = model.schedules()
    return jsonify(content)

# Update schedule by ID
@schedule_blueprint.route('/update_schedule/<sch_id>', methods=['POST'])
@cross_origin()
def update_schedule(sch_id):
    content = model.update_schedule(sch_id, 
                                    request.json['sch_begin'],
                                    request.json['sch_end'],
                                    request.json['sch_day'],
                                    request.json['gru_id'])
    return jsonify(content)

# Delete schedule by ID
@schedule_blueprint.route('/delete_schedule/<sch_id>', methods=['POST'])
@cross_origin()
def delete_schedule(sch_id):
    model.delete_schedule(sch_id)
    return f"Schedule {sch_id} deleted succesfully"