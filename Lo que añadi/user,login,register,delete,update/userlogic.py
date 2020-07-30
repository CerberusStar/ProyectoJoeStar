from Logic import Logic
from userobj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id_usuario",
            "nombre",
            "apellido",
            "usuario",
            "password",
            "email",
            "peso",
            "edad",
            "altura",
            "wallet",
        ]

    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from joestardb.usuarios where usuario='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["id_usuario"],
                data_dic["nombre"],
                data_dic["apellido"],
                data_dic["usuario"],
                data_dic["password"],
                data_dic["email"],
                data_dic["peso"],
                data_dic["edad"],
                data_dic["altura"],
                data_dic["wallet"],
            )
            return userObj
        else:
            return None

    def insertUser(
        self, nombre, apellido, usuario, password, email, peso, edad, altura
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO joestardb.usuarios (id_usuario, nombre, apellido, usuario, password, email, peso, edad, altura, wallet) "
            + f"VALUES ('0', '{nombre}', '{apellido}', '{usuario}', '{password}', '{email}', '{peso}', '{edad}', '{altura}', '');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def deleteUser(self, user):
        database = self.get_databaseXObj()
        sql = "DELETE FROM joestardb.usuarios " + f"WHERE (usuario = '{user}');"
        answer2 = database.executeNonQueryBool(sql)
        return answer2

    def updateUser(
        self, id, nombre, apellido, usuario, password, email, peso, edad, altura
    ):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE joestardb.usuarios SET "
            + f"nombre = '{nombre}', apellido = '{apellido}', usuario = '{usuario}', password = '{password}', "
            + f"email = '{email}', peso = '{peso}', edad = '{edad}', altura = '{altura}', wallet = '' WHERE (id_usuario = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer
