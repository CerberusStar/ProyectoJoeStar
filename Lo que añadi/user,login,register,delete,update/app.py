from flask import Flask, render_template, request, redirect, session, url_for
from MethodUtil import MethodUtil
from userlogic import UserLogic
from userobj import UserObj
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "python es bien chivo"


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
        altura = request.form["altura"]
        logic = UserLogic()
        confirmation = logic.insertUser(
            nombre, apellido, usuario, password, email, peso, edad, altura
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
def update():
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

                session.pop("username", None)
                session["username"] = id

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
            logic = UserLogic()
            confirmation = logic.updateUser(
                session["username"],
                nombre,
                apellido,
                usuario,
                password,
                email,
                peso,
                edad,
                altura,
            )

            if confirmation is True:
                session.pop("username", None)
                session["username"] = usuario
                return redirect(url_for("iniciarsesion"))
    else:
        return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True)
