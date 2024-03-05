from flask import Flask, render_template, request, redirect, url_for
import forms
from flask import flash
from flask_wtf.csrf import CSRFProtect
from wtforms import validators
from flask import g
from config import DevelopmentConfig

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




@app.route("/")
def nose():
    return render_template("layout2.html")



@app.route("/index", methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data, 
                       ape_paterno = create_form.ape_paterno.data, 
                       email = create_form.email.data)
        #insert alumnos() values()
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form = create_form)


@app.route("/ABC_Completo", methods = ["GET", "POST"])
def ABCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    print(alumnos)

    return render_template("ABC_Completo.html", alumnos = alumno)



@app.route("/alumnos", methods = ['GET', 'POST'])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    nom = ''
    apa = ''
    ama = ''
    edad = '' 
    email = ''
    if request.method == 'POST' and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.aPaterno.data
        ama = alumno_clase.aMaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data
        print("Nombre: {}".format(nom))
        print("A Paterno: {}".format(apa))
        print("A Materno: {}".format(ama))
        print("Edad: {}".format(edad))
        print("Email: {}".format(email))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("Alumnos.html", form = alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

@app.route("/Eliminar", methods = ['GET', 'POST'])
def Eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.ape_paterno.data = alum1.ape_paterno
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        #delete from alumnos where id= id
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template("Eliminar.html", form = create_form)


@app.route("/Modificar", methods = ['GET', 'POST'])
def Modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.ape_paterno.data = alum1.ape_paterno
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.nombre = create_form.nombre.data
        alum1.ape_paterno = create_form.ape_paterno.data 
        alum1.email = create_form.email.data 
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template("Modificar.html", form = create_form)



if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()