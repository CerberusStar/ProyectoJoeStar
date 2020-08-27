from Logic import Logic
from trainerobj import TrainerObj


class TrainerLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "idtrainer",
            "firstname",
            "lastname",
            "username",
            "password",
            "description",
            "email",
        ]

    def getTrainerData(self, trainer):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.trainer where username='{trainer}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            trainer = TrainerObj(
                data_dic["idtrainer"],
                data_dic["firstname"],
                data_dic["lastname"],
                data_dic["username"],
                data_dic["password"],
                data_dic["description"],
                data_dic["email"],
            )
            return trainer
        else:
            return None

    def getTrainerDataById(self, trainer):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.trainer where id='{trainer}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            trainer = TrainerObj(
                data_dic["idtrainer"],
                data_dic["firstname"],
                data_dic["lastname"],
                data_dic["username"],
                data_dic["password"],
                data_dic["description"],
                data_dic["email"],
            )
            return trainer
        else:
            return None

    def insertTrainer(self, nombre, apellido, usuario, password, descripcion, email):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.trainer (id, firstname, lastname, username, password, description, email) "
            + f"VALUES ('0', '{nombre}', '{apellido}', '{usuario}', '{password}', '{descripcion}', '{email}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def updateTrainer(self, id, nombre, apellido, password, descripcion, email):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE proyectocerberus.trainer SET "
            + f"firstname = '{nombre}', lastname = '{apellido}', password = '{password}', "
            + f"description = '{descripcion}', email = '{email}' WHERE (id = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer
