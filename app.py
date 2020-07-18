from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/beforeAMPL")
def question():

    return render_template("index.html")


@app.route("/ampl", methods=["GET", "POST"])
def ampl():
    listaVariables = []
    listaPrecios = []
    listaRestricciones = []
    numbers = [1, 2, 3, 4]
    restriccion = [1, 2]
    if request.method == "GET":
        # código que toma el id y lo imprime
        # form a la tabla y ponerle el method GET
        # Ocupar un input type hidden para el id
        return render_template("amplForm.html", number=numbers, restriccion=restriccion)
    else:
        for i in numbers:
            variable = request.form[f"variable{i}"]
            precio = request.form[f"precio{i}"]

            listaVariables.append(variable)
            listaPrecios.append(precio)

        print(listaVariables)

        for j in restriccion:
            restriccion = request.form[f"restriction{j}"]
            listaRestricciones.append(restriccion)
        print(listaRestricciones)

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
