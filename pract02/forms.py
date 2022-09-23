from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField 
from wtforms import validators

class CommentForm(Form):
    #con validaciones
    username = StringField('usename', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=25, message='Ingrese un campo valido')
        ])
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')