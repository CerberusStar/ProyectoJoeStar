from Logic import Logic
from rutineObj import RutineObj

class rutineLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "idtrainer",
            "iduser",
            "exercise",
            "step",
            "time",
            "repetition",
        ]

    def getAllRutinesFromUser(self, userid):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.routine where iduser='{userid}' order by step asc;"
        data = database.executeQuery(sql)
        return data

    def deleteRutina(self, idd):
        database = self.get_databaseXObj()
        sql = "DELETE FROM proyectocerberus.routine " + f"WHERE (id = '{idd}');"
        answer2 = database.executeNonQueryBool(sql)
        return answer2
        
    def insertRutina(self, idtrainer, iduser, exercise, step, time, repetition):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.routine (id, idtrainer, iduser, exercise, step, time, repetition) "
            + f"VALUES ('0', '{idtrainer}', '{iduser}', '{exercise}', '{step}', '{time}', '{repetition}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def updateRutina(self, id, exercise, step, time, repetition):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE proyectocerberus.routine SET "
            + f"exercise = '{exercise}', step = '{step}', "
            + f"time = '{time}', repetition = '{repetition}' WHERE (id = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def getRutineData(self, rutina):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.routine where id='{rutina}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            rutineObj = RutineObj(
                data_dic["id"],
                data_dic["idtrainer"],
                data_dic["iduser"],
                data_dic["exercise"],
                data_dic["step"],
                data_dic["time"],
                data_dic["repetition"],
            )
            return rutineObj
        else:
            return None