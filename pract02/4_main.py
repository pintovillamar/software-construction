from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__) #instancia

@app.route('/', methods = ['GET', 'POST']) #wrap (decorator)
def index():
    comment_form = forms.CommentForm(request.form) #crea una instancia con los datos que envio el cvleinte
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    return render_template('form.html', title = 'vicente', form = comment_form)

if __name__ == '__main__':
    app.run(debug=True, port=8002) #lunch server on port 500