import mysql.connector


class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="proyectocerberus"
        )
        cursor = con.cursor()
        return con, cursor

    def getIdConv(self, idUser, idtrainer):
        con, cursor = self.__createCursor()
        sql = (
            "select c_id from proyectocerberus.conversation where "
            + f" user = {idUser} AND trainer = {idtrainer} ; "
        )
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def insertMessage(self, message, id_c, iduserFrom, typeU):
        con, cursor = self.__createCursor()
        if typeU == 1:
            statusU = "trainer"
        else:
            statusU = "user"

        sql = (
            "insert into proyectocerberus.conversation_reply"
            + "(cr_id, reply, user_trainer_id_fk, ip, time, status, c_id_fk, typeUser)"
            + f"values(0, '{message}', {iduserFrom},'192.168.0.1', 15556, 'read', {iduserFrom}, '{statusU}'); "
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount


datab = Database()
mss = "Hola mundo"
idconver = datab.getIdConv(1, 1)
datab.insertMessage(mss, idconver, 1, 1)
