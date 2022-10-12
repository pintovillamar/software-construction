from backend.models.connection_pool import getcursor
from flask import jsonify
from backend.models.conn import db
from backend.models.conn import ma
from werkzeug.utils import secure_filename

class Face_Recognition_Model:
    def openface():
        pass        
        # # si queremos guardar la foto
        # filename = file.filename
        # path = "/home/jose/Documents/software-construction/openfaceAPI/photos/" + filename
        # file.save(path)       
           
   
        # # call openfaceAPI ##################################
        # url = 'http://127.0.0.1:81/openfaceAPI'
        # files = {'file': open(path, 'rb')}
        # #files = {'file': f}

        # result = requests.post(url, files=files)
        # print(result.json())
        # ######################################################

        

        # # queda pendiente: registrar los demas datas del 
        # # usuario en la BD junto con el vector de caracteristicas
