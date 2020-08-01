from flask import Flask, render_template, request, redirect, session, url_for
from Controladora import Control
from MethodUtil import MethodUtil
from userlogic import UserLogic
from userobj import UserObj
from werkzeug.security import generate_password_hash, check_password_hash


codigoampl = Control()
app = Flask(__name__)
app.secret_key = "prueba"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inicio", methods=MethodUtil.list_ALL())
def inicio():
    if request.method == "GET":
        return render_template("inicio.html")


@app.route("/inicio/loginform", methods=MethodUtil.list_ALL())
def loginform():
    if request.method == "GET":
        return render_template("loginform.html", message="")
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        logic = UserLogic()
        userdata = logic.getUserData(usuario)
        if userdata is not None:
            session["username"] = userdata.usuario
            if userdata.password == password:
                return redirect(url_for("iniciarsesion"))
            else:
                return render_template(
                    "loginform.html",
                    message="el usuario o la contraseña está incorrecto, intentelo de nuevo",
                )
        else:
            return render_template(
                "loginform.html",
                message="el usuario o la contraseña está incorrecto, intentelo de nuevo",
            )


@app.route("/inicio/registerform", methods=MethodUtil.list_ALL())
def registerform():
    if request.method == "GET":
        return render_template("registerform.html",)
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        usuario = request.form["usuario"]
        password = request.form["password"]
        email = request.form["email"]
        peso = request.form["peso"]
        edad = request.form["edad"]
        sexo = request.form["sexo"]
        altura = request.form["altura"]
        logic = UserLogic()
        confirmation = logic.insertUser(
            nombre, apellido, usuario, password, email, peso, edad, altura, sexo
        )
        if confirmation is True:
            session["username"] = usuario
            return redirect(url_for("iniciarsesion"))
        else:
            return "hay un problema"


@app.route("/inicio/sesion", methods=MethodUtil.list_ALL())
def iniciarsesion():
    if "username" in session:
        return render_template("dashboard_user.html", userdata=session["username"])
    else:
        return redirect(url_for("inicio"))


@app.route("/inicio/session/borrar", methods=MethodUtil.list_ALL())
def borrar():
    if "username" in session:
        logic = UserLogic()
        confirmation = logic.deleteUser(session["username"])
        if confirmation is True:
            return redirect(url_for("salir"))
    else:
        return redirect(url_for("inicio"))


@app.route("/inicio/session/salir", methods=MethodUtil.list_ALL())
def salir():
    if "username" in session:
        session.pop("username", None)
        return redirect(url_for("inicio"))
    else:
        return redirect(url_for("inicio"))


@app.route("/inicio/session/update", methods=MethodUtil.list_ALL())
def updateUser():
    if "username" in session:
        if request.method == "GET":
            logic = UserLogic()
            data = logic.getUserData(session["username"])
            if data is not None:
                id = data.id
                nombre = data.nombre
                apellido = data.apellido
                usuario = data.usuario
                password = data.password
                email = data.email
                peso = data.peso
                edad = data.edad
                altura = data.altura
                sexo = data.sexo

                session["id_user"] = id

            return render_template(
                "update_user.html",
                nombre1=nombre,
                apellido1=apellido,
                usuario1=usuario,
                password1=password,
                email1=email,
                peso1=peso,
                edad1=edad,
                altura1=altura,
                sexo1=sexo,
            )
        else:
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            usuario = request.form["usuario"]
            password = request.form["password"]
            email = request.form["email"]
            peso = request.form["peso"]
            edad = request.form["edad"]
            altura = request.form["altura"]
            sexo = request.form["sexo"]
            logic = UserLogic()
            confirmation = logic.updateUser(
                session["id_user"],
                nombre,
                apellido,
                usuario,
                password,
                email,
                peso,
                edad,
                altura,
                sexo,
            )

            if confirmation is True:
                session.pop("username", None)
                session["username"] = usuario
                return redirect(url_for("iniciarsesion"))
    else:
        return redirect(url_for("inicio"))


@app.route("/trainer")
def trainer():
    return render_template("trainer.html")


@app.route("/trainer/beforeAmpl", methods=["POST"])
def update():
    name = request.form.get("name")
    var = int(request.form.get("var"))
    restriction = int(request.form.get("restriction"))
    session["name"] = name
    session["var"] = var
    session["restriction"] = restriction
    return redirect("/trainer/ampl")


@app.route("/trainer/ampl", methods=["GET", "POST"])
def ampl():
    listaVariables = []
    listaPrecios = []
    listaRestricciones = []
    var = session["var"]
    restriccion = session["restriction"]
    if request.method == "GET":
        # código que toma el id y lo imprime
        # form a la tabla y ponerle el method GET
        # Ocupar un input type hidden para el id
        return render_template("amplForm.html", var=var, restriccion=restriccion)
    else:
        for i in range(var):
            variable = request.form[f"variable{i}"]
            precio = request.form[f"precio{i}"]

            listaVariables.append(variable)
            listaPrecios.append(precio)

        for j in range(restriccion):
            restriccion = request.form[f"restriction{j}"]
            listaRestricciones.append(restriccion)

        codigoampl.createArchive(
            session["name"], listaVariables, listaPrecios, listaRestricciones
        )
        # Control de errores, ya que si hay algún error siempre se crean los archivos, pero se escriben sobre ellos
        # Un control de errores puede leer el archivo y sí está vacío algo salió mal
        nombre = session["name"]
        booleano = codigoampl.controlDeError(nombre)
        if booleano == 1:
            return render_template("exito.html")
        else:
            codigoampl.borrarArchivo(session["name"])
            return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
