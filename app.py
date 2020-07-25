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

        print(listaVariables)

        for j in range(restriccion):
            restriccion = request.form[f"restriction{j}"]
            listaRestricciones.append(restriccion)
        print(listaRestricciones)

        codigoampl.createArchive(
            session["name"], listaVariables, listaPrecios, listaRestricciones
        )
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
