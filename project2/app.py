from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.user_type_blueprint import user_type_blueprint

#app = Flask(__name__)
# para que utilice vue compilado ( npm run build ). En la carpeta dist, esta lo compilado de vue
app = Flask(__name__,
            static_folder = "./frontend/dist/static",
            template_folder = "./frontend/dist")

app.register_blueprint(user_type_blueprint)

cors = CORS(app, support_credentials=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def dender_vue(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)