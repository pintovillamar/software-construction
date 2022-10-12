from flask import Flask
import requests


# CHANGES
from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from backend.models.connection_pool import getcursor
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename
import numpy as np




from backend.models.face_recognition_model import Face_Recognition_Model
model = Face_Recognition_Model() # POR AHORA NO SE USA



face_recognition_blueprint = Blueprint('/face_recognition_blueprint', __name__)

# app = Flask(__name__) #instancia # moved to conn.py 


@face_recognition_blueprint.route('/openface_prueba', methods=['POST']) #wrap (decorator)
@cross_origin()
def openface(): 
    
    f = request.files['file']
    
    # si queremos guardar la foto
    filename = f.filename
    path = "/home/jose/Documents/software-construction/project2/photos/Students/" + filename
    path_uploaded = "/home/jose/Documents/software-construction/project2/photos/Students" + filename
    # path_uploaded_compare = ""
    f.save(path)       
       

    # call openfaceAPI ##################################
    url = 'http://127.0.0.1:81/openfaceAPI'
    files = {'file': open(path, 'rb')}
    #files = {'file': f}
    result = requests.post(url, files=files)
    # print(result.json())
    ######################################################
    
    # queda pendiente: registrar los demas datas del 
    # usuario en la BD junto con el vector de caracteristicas

    

    return result.json()

# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #lunch server on port 5000

# END POINT DEL RECONOCIMIENTO FACIAL
# DNI Y FOTO

# el end point debe hacer:
# 


def face_recognition(image1, image2):
    temp1 = image1.replace("[", "")
    temp1 = temp1.replace("]", "")
    temp1 = temp1.replace("  "," ")
    temp1 = temp1.replace("\n","")
    temp1.strip()

    temp2 = image2.replace("[", "")
    temp2 = temp2.replace("]", "")
    temp2 = temp2.replace("  "," ")
    temp2 = temp2.replace("\n","")
    temp2.strip()

    temp1 = " ".join(temp1.split())
    temp2 = " ".join(temp2.split())

    arr1 = np.fromstring(temp1, dtype=float, sep=' ')
    arr2 = np.fromstring(temp2, dtype=float, sep=' ')
        
    a = np.array(arr1)
    b = np.array(arr2)

    return np.linalg.norm(a-b)