from wtforms import validators,StringField, TelField, IntegerField, EmailField, Form

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=4, max=10, message="ingresa nombre valido")
        ])
    email = EmailField('email', [validators.Email(message="Ingrese un correo Valido")])
    aPaterno = TelField('apaterno')
    aMaterno = TelField('amaterno')
    edad  = IntegerField('edad')