from flask import Flask
from flask import request

app = Flask(__name__) #instancia

@app.route('/') #wrap (decorator)
def index():
    return 'Hola mundo' #return string

# GET param
@app.route('/method1')
#http://127.0.0.1:8080/method1?param1=mensaje
def method1():
    param = request.args.get('param1', 'without data')
    return 'the param is: ' + str(param)

# params followed by slashes
@app.route('/method2/') # accept 0 params
@app.route('/method2/<name>/') # accept one param
@app.route('/method2/<name>/<int:dni>') # acep two params, forzamos a q el segundo parametro sea int
#http://127.0.0.1:8080/method2/vicente/78787878
def method2(name='No data', dni='no dni'): #debe tener el mismo nombre que en <name>/<dni>
    #param = request.args.get('param1', 'without data')
    return 'the param is: ' + str(name) + ' ' + str(dni)

if __name__ == '__main__':
    app.run(debug=True, port=8080) #lunch server on port 5000