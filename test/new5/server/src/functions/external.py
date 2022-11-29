import numpy as np

def convertToJson(image):
    temp = image.replace('\"',"")
    temp = temp.replace('\'',"")
    temp = temp.replace('result:',"")
    temp = temp.replace("[", "")
    temp = temp.replace("]", "")
    temp = temp.replace("{", "")
    temp = temp.replace("}", "")
    temp = temp.replace("  "," ")
    temp = temp.replace("\n","")
    temp = temp.replace('\\n','')
    temp.strip()

    temp = " ".join(temp.split())

    return temp

def face_recognition(image1, image2):
    print("estoy en face_recognition")
    image1 = np.fromstring(image1, dtype=float, sep=' ')
    image2 = np.fromstring(image2, dtype=float, sep=' ')

    if ( np.linalg.norm(np.array(image1) - np.array(image2)) >= 1 ):
        return False
    else:
        return True