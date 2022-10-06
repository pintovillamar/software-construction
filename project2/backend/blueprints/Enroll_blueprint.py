from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from backend.models.Enroll_model import Enroll_Model
model = Enroll_Model()

enroll_blueprint = Blueprint('/enroll_blueprint', __name__)

# Create a enroll
@enroll_blueprint.route('/create_enroll', methods=['POST'])
@cross_origin()
def create_enroll():
    content = model.create_enroll(request.json['stu_id'],
                                    request.json['gru_id'],
                                    request.json['enr_date'])    
    return jsonify(content)

# List enroll with ID
@enroll_blueprint.route('/enroll/<enr_id>', methods=['POST'])
@cross_origin()
def enroll(enr_id):
    content = model.enroll(enr_id)
    return jsonify(content)

# List all enrolls
@enroll_blueprint.route('/enrolls', methods=['POST'])
@cross_origin()
def enrolls():
    content = model.enrolls()
    return jsonify(content)

# Update enroll by ID
@enroll_blueprint.route('/update_enroll/<enr_id>', methods=['POST'])
@cross_origin()
def update_enroll(enr_id):
    content = model.update_enroll(enr_id, 
                                    request.json['stu_id'],
                                    request.json['gru_id'],
                                    request.json['enr_date'])
    return jsonify(content)

# Delete enroll by ID
@enroll_blueprint.route('/delete_enroll/<enr_id>', methods=['POST'])
@cross_origin()
def delete_enroll(enr_id):
    model.delete_enroll(enr_id)
    return f"Enroll {enr_id} deleted succesfully"
    

