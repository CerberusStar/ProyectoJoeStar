from flask import Flask, render_template, request, redirect, session
from Controladora import Control

codigoampl = Control()
app = Flask(__name__)
app.secret_key = "prueba"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user():
    return render_template("user.html")


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
