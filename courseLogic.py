from Logic import Logic
from courseObj import CourseObj


class CourseLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "name",
            "description",
            "duration",
            "cost",
            "iduser",
            "idtrainer",
            "estado",
        ]

    def getAllCoursesUrCourses(self, trainerid):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.course where idtrainer='{trainerid}';"
        data = database.executeQuery(sql)
        return data

    def getAllCoursesAvailableCourses(self):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.course where iduser is NULL;"
        data = database.executeQuery(sql)
        return data

    def getAllCoursesUserSuscripted(self, iduser):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.course where iduser='{iduser}';"
        data = database.executeQuery(sql)
        return data

    def insertCourse(self, name, description, duration, cost, idtrainer):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.course (idcourse, name, description, duration, cost, iduser, idtrainer, estado) "
            + f"VALUES ('0', '{name}', '{description}', '{duration}', '{cost}', NULL, '{idtrainer}', 'No finalizado');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def getCourseData(self, course):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.course where idcourse='{course}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            courseObj = CourseObj(
                data_dic["id"],
                data_dic["name"],
                data_dic["description"],
                data_dic["duration"],
                data_dic["cost"],
                data_dic["iduser"],
                data_dic["idtrainer"],
                data_dic["estado"],
            )
            return courseObj
        else:
            return None

    def deleteCourse(self, idd):
        # Debo hacer una seguridad extra porque un trainer por querer estafar a alguien en un curso
        # puede escribir el link "/trainer/session/course/updateStatus/<int:id>" con un id no permitido y borrarlo
        # sin problemas, por eso verificaré un dato y si quiere estafar lo mando a un html para que sepa que la app
        # sabe lo que quiere hacer.
        Traitor = "Traitor"
        database = self.get_databaseXObj()
        sqlControl = (
            f"select iduser from proyectocerberus.course where (idcourse = '{idd}');"
        )
        idUserHopeNull = database.executeQuery(sqlControl)
        if idUserHopeNull[0][0] is None:
            sql = (
                "DELETE FROM proyectocerberus.course " + f"WHERE (idcourse = '{idd}');"
            )
            answer2 = database.executeNonQueryBool(sql)
            return answer2
        else:
            return Traitor

    def updateCourse(self, id, nombre, description, duration, cost):
        Traitor = "Traitor"
        database = self.get_databaseXObj()
        sqlControl = (
            f"select iduser from proyectocerberus.course where (idcourse = '{id}');"
        )
        idUserHopeNull = database.executeQuery(sqlControl)
        if idUserHopeNull[0][0] is None:
            sql = (
                "UPDATE proyectocerberus.course SET "
                + f"name = '{nombre}', "
                + f"description = '{description}', duration = '{duration}', cost = '{cost}' WHERE (idcourse = '{id}');"
            )
            answer = database.executeNonQueryBool(sql)
            return answer
        else:
            return Traitor

    def changeCourseStatus(self, idd):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE proyectocerberus.course SET "
            + f"estado = 'Finalizado' WHERE (idcourse = '{idd}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def buyCourse(self, idcourse, iduser):
        database = self.get_databaseXObj()
        # Consigo el costo del curso
        sqlgetCost = (
            f"select cost from proyectocerberus.course where (idcourse = '{idcourse}');"
        )
        courseCost = database.executeQuery(sqlgetCost)
        courseCostData = float(courseCost[0][0])
        # Consigo el dinero actual del usuario
        sqlgetWallet = (
            f"select wallet from proyectocerberus.user where (iduser = '{iduser}');"
        )
        userWallet = database.executeQuery(sqlgetWallet)
        userWalletData = float(userWallet[0][0])
        # Consigo el nuevo dinero del user
        AdjustedWallet = userWalletData - courseCostData
        # Actualizo la billetera del usuario
        sqlActualizeWallet = (
            "UPDATE proyectocerberus.user SET "
            + f"wallet = {AdjustedWallet} WHERE (iduser = '{iduser}');"
        )
        database.executeNonQueryBool(sqlActualizeWallet)
        # Me suscribo al curso
        sqlCourse = (
            "UPDATE proyectocerberus.course SET "
            + f"iduser = '{iduser}' WHERE (idcourse = '{idcourse}');"
        )
        answer = database.executeNonQueryBool(sqlCourse)
        return answer
