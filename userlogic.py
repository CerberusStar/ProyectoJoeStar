from Logic import Logic
from userobj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "iduser",
            "firstname",
            "lastname",
            "username",
            "password",
            "email",
            "age",
            "weigth",
            "size",
            "gender",
            "wallet",
        ]

    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.user where username='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["iduser"],
                data_dic["firstname"],
                data_dic["lastname"],
                data_dic["username"],
                data_dic["password"],
                data_dic["email"],
                data_dic["weigth"],
                data_dic["age"],
                data_dic["size"],
                data_dic["gender"],
                data_dic["wallet"],
            )
            return userObj
        else:
            return None

    def insertUser(
        self, nombre, apellido, usuario, password, email, peso, edad, altura, sexo
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.user (iduser, firstname, lastname, username, password, email, age, weigth, size, gender, wallet) "
            + f"VALUES ('0', '{nombre}', '{apellido}', '{usuario}', '{password}', '{email}', '{edad}', '{peso}', '{altura}', '{sexo}' ,'0.00');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def deleteUser(self, user):
        database = self.get_databaseXObj()
        sql = "DELETE FROM proyectocerberus.user " + f"WHERE (username = '{user}');"
        answer2 = database.executeNonQueryBool(sql)
        return answer2

    def updateUser(self, id, nombre, apellido, password, email, peso, edad, altura):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE proyectocerberus.user SET "
            + f"firstname = '{nombre}', lastname = '{apellido}', password = '{password}', "
            + f"email = '{email}', weigth = '{peso}', age = '{edad}', size = '{altura}'  WHERE (iduser = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer
