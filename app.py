from flask import Flask, render_template, request, redirect, session, url_for
from Controladora import Control
from MethodUtil import MethodUtil
from userlogic import UserLogic
from userobj import UserObj
from trainerlogic import TrainerLogic
from trainerobj import TrainerObj
from courseObj import CourseObj
from courseLogic import CourseLogic
from walletlogic import WalletLogic
from walletobj import WalletObj
from rutineLogic import rutineLogic
from rutineObj import RutineObj
from werkzeug.security import generate_password_hash, check_password_hash
from ClaseDatabaseMessage import Database
import datetime
import os
from changephoto import changephoto as changephoto
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from os import remove
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

database = Database()
codigoampl = Control()
app = Flask(__name__)
app.secret_key = "prueba"


@app.route("/")
def index():
    return render_template("index.html")


# PARA EL USUARIO NORMAL
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

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
            session["user_id"] = userdata.id
            session["wallet"] = userdata.wallet
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
        gender = request.form["gender"]
        if gender == "male":
            sexo = 1
        elif gender == "female":
            sexo = 0

        altura = request.form["altura"]
        logic = UserLogic()
        controlDeErrorUsernameUser = logic.getUserData(usuario)
        if controlDeErrorUsernameUser is None:
            confirmation = logic.insertUser(
                nombre, apellido, usuario, password, email, peso, edad, altura, sexo
            )
            if confirmation is True:
                session["username"] = usuario
                return redirect(url_for("loginform"))
            else:
                return "hay un problema"
        else:
            return render_template(
                "registerform.html",
                messageUserExisted="Ya existe ese usuario, por favor escoja otro",
                nombre=nombre,
                apellido=apellido,
                usuario=usuario,
                email=email,
                peso=peso,
                edad=edad,
                sexo=sexo,
                altura=altura,
            )


@app.route("/inicio/sesion", methods=MethodUtil.list_ALL())
def iniciarsesion():
    if "username" in session:
        rutine = rutineLogic()
        data = rutine.getAllRutinesFromUser(session["user_id"])
        
        usuario = session["username"]
        login = UserLogic()
        nombreCompletoImagen = os.getcwd() + f"\\static\\uploads\\{usuario}.jpg"
        comprobacion = os.path.exists(nombreCompletoImagen)
        if comprobacion is True:
            filename = f"{usuario}.jpg"
        else:
            filename = login.readBLOB(session["username"])

        return render_template(
            "dashboard_user.html",
            userdata=session["username"],
            wallet=session["wallet"],
            rutinas = data,
            filename = filename,
        )
    else:
        return redirect(url_for("inicio"))


@app.route("/inicio/session/salir", methods=MethodUtil.list_ALL())
def salir():
    if "username" in session:
        session.pop("wallet", None)
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
                nombre = data.nombre
                apellido = data.apellido
                usuario = data.usuario
                password = data.password
                email = data.email
                peso = data.peso
                edad = data.edad
                altura = data.altura
                session["id_user"] = data.id

            return render_template(
                "update_user.html",
                nombre1=nombre,
                apellido1=apellido,
                username1=usuario,
                email1=email,
                peso1=peso,
                edad1=edad,
                altura1=altura,
            )
        else:
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            password = request.form["password"]
            email = request.form["email"]
            peso = request.form["peso"]
            edad = request.form["edad"]
            altura = request.form["altura"]
            logic = UserLogic()
            confirmation = logic.updateUser(
                session["id_user"],
                nombre,
                apellido,
                password,
                email,
                peso,
                edad,
                altura,
            )

            if confirmation is True:
                return redirect(url_for("iniciarsesion"))
    else:
        return redirect(url_for("inicio"))


@app.route("/inicio/session/course", methods=MethodUtil.list_GETOnly())
def courseUser():
    course = CourseLogic()
    data = course.getAllCoursesAvailableCourses()
    data2 = course.getAllCoursesUserSuscripted(session["user_id"])
    return render_template(
        "courseAvailableFromUser.html",
        courses=data,
        suscriptions=data2,
        wallet=session["wallet"],
    )

@app.route("/inicio/session/course/trainer/<int:idtrainer>", methods=["GET"])
def seeTrainerAcount(idtrainer):
    if request.method == "GET":
        session["TrainerIDGetByUser"] = idtrainer
        print(idtrainer)
        logictrainer = TrainerLogic()
        data = logictrainer.getTrainerDataById(idtrainer)
        print(data)
        return render_template("trainerprofilefromuser.html", data=data)
        

@app.route(
    "/inicio/session/course/suscription/<string:name>/<string:cost>/<int:idd>",
    methods=MethodUtil.list_GETOnly(),
)
def courseSuscriptionUser(name, cost, idd):
    costDouble = float(cost)
    ActualMoney = session["wallet"]
    NewMoney = ActualMoney - costDouble
    session["adjustedWallet"] = NewMoney
    if NewMoney < 0:
        return render_template(
            "error.html",
            message="No tienes suficientes fondos, agrega más a tu wallet antes de comprar",
        )
    else:
        return render_template(
            "courseSuscriptionConfirmation.html",
            Name=name,
            Actual=ActualMoney,
            Cost=cost,
            Nuevo=NewMoney,
            id=idd,
        )

@app.route("/inicio/session/photo", methods=MethodUtil.list_ALL())
def photo():
    if "username" in session:
        if request.method == "GET":
            return render_template("changephoto.html")
        if request.method == "POST":
            print(f"request.files -> {request.files}")
            usuario = session["username"]
            if "file" not in request.files:
                flash("No file part")
                print(request.url)
                return redirect(request.url)
            file = request.files["file"]
            print(f"file.filename -> {file.filename}")
            if file.filename == "":
                flash("No image selected for uploading")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                comprobacion = os.path.exists("static/uploads/"+f"{usuario}.jpg")
                if comprobacion is True:
                    remove("static/uploads/"+f"{usuario}.jpg")
                file.save(os.path.join(changephoto.config["UPLOAD_FOLDER"], filename))
                flash("Image successfully uploaded and displayed")
                print(filename)
                
                logic = UserLogic()
                nombreimagen = os.getcwd() + f"\\static\\uploads\\{filename}"
                confirmation = logic.insertphotoUser(session["username"],nombreimagen)

                archivo = f"static/uploads/{filename}"
                nombre_nuevo = "static/uploads/"+f"{usuario}.jpg"
                os.rename(archivo, nombre_nuevo)
                
                #nombre = f"{usuario}.jpg"

                #print(nombre)
                if confirmation is True:
                    return render_template("changephoto.html", filename=filename)
            else:
                flash("Allowed image types are -> png, jpg, jpeg, gif")
                return redirect(request.url)

@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for("static", filename="uploads/" + filename), code=301)



@app.route(
    "/inicio/session/course/buy/<int:idcourse>", methods=MethodUtil.list_POSTOnly()
)
def buyCourse(idcourse):
    iduser = session["user_id"]
    actualCourse = CourseLogic()
    actualCourse.buyCourse(idcourse, iduser)
    session["wallet"] = session["adjustedWallet"]
    return redirect(url_for("courseUser"))

@app.route("/inicio/session/saldo/pay", methods=MethodUtil.list_ALL())
def pay():
    if request.method == "GET":
        return render_template("saldo.html")
    if request.method == "POST":
        tarjeta = request.form["tarjeta"]
        cvv = request.form["cvv"]
        month = request.form["mes"]
        year = request.form["año"]
        ownercard = request.form["nombre"]
        x = datetime.datetime.now()
        date = x.strftime("%x")
        amount = request.form["cantidad"]
        logic = WalletLogic()
        iduser= session["user_id"]
        data = logic.insertToWallet(id, iduser, tarjeta, cvv, month, year, ownercard, date, amount)
        if data is True:
            session["user_id"] =iduser
            pay = float(amount)
            if pay < 0:
                return render_template("error.html", message="La cantidad ingresada no es valida, intentalo de nuevo")
            else:
                actualMoney = session["wallet"]
                payment = pay + actualMoney
                session["adjustedWallet"] = payment
                return render_template("payconfirmation.html", amount = amount, payment = payment)
        else:
            return render_template("error.html", message="hubo un error intentelo de nuevo")

@app.route(
    "/inicio/session/saldo/payment", methods=MethodUtil.list_POSTOnly()
)
def payment():
    if request.method == "POST":
        actualWallet = WalletLogic()
        actualWallet.updateWallet(session["user_id"], session["adjustedWallet"])
        session["wallet"] = session["adjustedWallet"]
        return redirect(url_for("iniciarsesion"))


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
# PARA EL TRAINER
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------


@app.route("/trainer", methods=MethodUtil.list_ALL())
def inicioTrainer():
    if request.method == "GET":
        return render_template("inicioTrainer.html")


@app.route("/trainer/loginform", methods=MethodUtil.list_ALL())
def loginformTrainer():
    if request.method == "GET":
        return render_template("loginformTrainer.html", message="")
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        logic = TrainerLogic()
        userdata = logic.getTrainerData(usuario)
        if userdata is not None:
            session["idtrainer"] = userdata.id
            session["usernameTrainer"] = userdata.username
            if userdata.password == password:
                return redirect(url_for("iniciarsesionTrainer"))
            else:
                return render_template(
                    "loginformTrainer.html",
                    message="el usuario o la contraseña está incorrecto, intentelo de nuevo",
                )
        else:
            return render_template(
                "loginformTrainer.html",
                message="el usuario o la contraseña está incorrecto, intentelo de nuevo",
            )


@app.route("/trainer/registerform", methods=MethodUtil.list_ALL())
def registerformTrainer():
    if request.method == "GET":
        return render_template("registerformTrainer.html",)
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        usuario = request.form["usuario"]
        password = request.form["password"]
        email = request.form["email"]
        descripcion = request.form["descripcion"]
        logic = TrainerLogic()
        controlDeErrorUsername = logic.getTrainerData(usuario)
        if controlDeErrorUsername is None:
            confirmation = logic.insertTrainer(
                nombre, apellido, usuario, password, descripcion, email
            )
            if confirmation is True:
                session["usernameTrainer"] = usuario
                return redirect(url_for("loginformTrainer"))
            else:
                return "hay un problema"
        else:
            return render_template(
                "registerformTrainer.html",
                message2="Ya existe ese username, escoja otro",
                nombre=nombre,
                apellido=apellido,
                usuario=usuario,
                email=email,
                descripcion=descripcion,
            )


@app.route("/trainer/sesion", methods=MethodUtil.list_ALL())
def iniciarsesionTrainer():
    if "usernameTrainer" in session:
        return render_template(
            "dashboard_trainer.html", userdata=session["usernameTrainer"]
        )
    else:
        return redirect(url_for("inicioTrainer"))


@app.route("/trainer/session/salir", methods=MethodUtil.list_ALL())
def salirTrainer():
    if "usernameTrainer" in session:
        session.pop("usernameTrainer", None)
        return redirect(url_for("inicioTrainer"))
    else:
        return redirect(url_for("inicioTrainer"))


@app.route("/trainer/session/update", methods=MethodUtil.list_ALL())
def updateUserTrainer():
    if "usernameTrainer" in session:
        if request.method == "GET":
            logic = TrainerLogic()
            data = logic.getTrainerData(session["usernameTrainer"])
            if data is not None:
                id = data.id
                nombre = data.firstname
                apellido = data.lastname
                password = data.password
                description = data.description
                email = data.email
                session["id_trainer"] = id

            return render_template(
                "update_Trainer.html",
                nombre1=nombre,
                apellido1=apellido,
                password1=password,
                descripcion1=description,
                email1=email,
            )
        else:
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            password = request.form["password"]
            description = request.form["descripcion"]
            email = request.form["email"]
            logic = TrainerLogic()
            confirmation = logic.updateTrainer(
                session["id_trainer"], nombre, apellido, password, description, email,
            )

            if confirmation is True:
                return redirect(url_for("iniciarsesionTrainer"))
    else:
        return redirect(url_for("inicioTrainer"))


@app.route("/trainer/session/course", methods=MethodUtil.list_ALL())
def courseTrainer():
    if request.method == "GET":
        course = CourseLogic()
        data = course.getAllCoursesUrCourses(session["idtrainer"])
        return render_template("courseFromTrainer.html", courses=data)
    if request.method == "POST":
        curso = request.form["name"]
        desc = request.form["desc"]
        duration = request.form["duration"]
        cost = request.form["cost"]
        logic = CourseLogic()
        Confirmation = logic.insertCourse(
            curso, desc, duration, cost, session["idtrainer"]
        )
        if Confirmation is True:
            return redirect(url_for("courseTrainer"))
        else:
            return "Hubo problema"


@app.route("/trainer/session/course/delete/<int:id>", methods=["GET"])
def deleteCourseByTrainer(id):
    if request.method == "GET":
        logic = CourseLogic()
        HopeAnswer = logic.deleteCourse(id)
        if HopeAnswer != "Traitor":
            return redirect("/trainer/session/course")
        else:
            return redirect("/traitor")


@app.route("/trainer/session/course/update/<int:idd>", methods=MethodUtil.list_ALL())
def updateCourse(idd):
    if request.method == "GET":
        logic = CourseLogic()
        data = logic.getCourseData(idd)
        if data is not None:
            nombre = data.name
            desc = data.description
            duration = data.duration
            return render_template(
                "updateCourse.html",
                idd=idd,
                name1=nombre,
                desc1=desc,
                duration1=duration,
            )
        else:
            return redirect("/traitor")

    else:
        nombre = request.form["name"]
        desc = request.form["desc"]
        duration = request.form["duration"]
        cost = request.form["cost"]
        logic = CourseLogic()
        confirmation = logic.updateCourse(idd, nombre, desc, duration, cost)
        if confirmation is True:
            return redirect(url_for("courseTrainer"))
        else:
            return redirect("/traitor")


@app.route("/traitor")
def traitor():
    return render_template("traitor.html", user=session["usernameTrainer"])


@app.route("/trainer/session/userAcount/<int:id>/<string:status>", methods=["GET"])
def seeUserAcount(id, status):
    if request.method == "GET":
        if status == "No finalizado":
            session["usernameUserFromTrainer"] = id
            logicuser = UserLogic()
            data = logicuser.getUserDataByID(id)
            imc = "{0:.2f}".format(data.peso / (data.altura * data.altura))
            imc = float(imc)
            return render_template("UserForTrainer.html", data=data, imc=imc)
        return render_template(
            "error.html",
            message="Este curso ya ha finalizado, no se puede acceder al perfil",
        )


@app.route("/trainer/session/userAcount/rutine", methods=["GET", "POST"])
def userRutine():
    if request.method == "GET":
        rutine = rutineLogic()
        data = rutine.getAllRutinesFromUser(session["usernameUserFromTrainer"])
        return render_template("rutinasDelUsuario.html", rutinas=data)
    if request.method == "POST":
        Etapa = request.form["etapa"]
        Ejercicio = request.form["ejercicio"]
        Time = request.form["time"]
        Set = request.form["set"]
        logic = rutineLogic()
        logic.insertRutina(
            session["idtrainer"],
            session["usernameUserFromTrainer"],
            Ejercicio,
            Etapa,
            Time,
            Set,
        )
        return redirect(url_for("userRutine"))


@app.route("/trainer/session/rutine/delete/<int:id>", methods=["GET"])
def deleteRutineByTrainer(id):
    if request.method == "GET":
        logic = rutineLogic()
        logic.deleteRutina(id)
        return redirect("/trainer/session/userAcount/rutine")


@app.route("/trainer/session/course/updateStatus/<int:id>", methods=["GET"])
def changeCourseStatusByTrainer(id):
    if request.method == "GET":
        logic = CourseLogic()
        logic.changeCourseStatus(id)
        return redirect("/trainer/session/course")


@app.route("/trainer/session/rutine/update/<int:idd>", methods=MethodUtil.list_ALL())
def updateRutine(idd):
    if request.method == "GET":
        logic2 = rutineLogic()
        data = logic2.getRutineData(idd)
        if data is not None:
            ejercicio1 = data.exercise
            repeticiones1 = data.repetition
            return render_template(
                "updateRutine.html",
                idd=idd,
                ejercicio=ejercicio1,
                repetition=repeticiones1,
            )
    else:
        Etapa = request.form["etapa"]
        Ejercicio = request.form["ejercicio"]
        Time = request.form["time"]
        Set = request.form["set"]
        logic = rutineLogic()
        confirmation = logic.updateRutina(idd, Ejercicio, Etapa, Time, Set)
        return redirect(url_for("userRutine"))


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


@app.route("/trainer/session/course/chat", methods=MethodUtil.list_ALL())
def chat():
    if request.method == "GET":
        mss = Database()
        idm = session["idtrainer"]
        idConv = mss.getIdConv(session["usernameUserFromTrainer"], session["idtrainer"])
        if len(idConv) == 0:
            data = 0
            return render_template("TrainerChat.html", conver=data)
        else:
            data = mss.getConvByIdConv(idConv[0][0])
            return render_template("TrainerChat.html", conver=data)


if __name__ == "__main__":
    app.run(debug=True)
