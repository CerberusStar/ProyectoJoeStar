import mysql.connector
from datetime import datetime


class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="proyectocerberus"
        )
        cursor = con.cursor()
        return con, cursor

    def createConv(self, idUser, idtrainer):
        con, cursor = self.__createCursor()
        sql = (
            "insert into proyectocerberus.conversation "
            + "(c_id, user, trainer, ip, time, status)"
            + f"values(0, '{idUser}', '{idtrainer}', 1, 1, 1);"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def getIdConv(self, idUser, idtrainer):
        con, cursor = self.__createCursor()
        sql = (
            "select c_id from proyectocerberus.conversation where "
            + f" user = {idUser} AND trainer = {idtrainer} ; "
        )
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def insertMessage(self, message, id_c, typeU):
        con, cursor = self.__createCursor()
        valueC = int(id_c[0][0])

        if typeU == 1:
            statusU = "trainer"
        else:
            statusU = "user"
        hour = self.getHour()
        sql = (
            "insert into proyectocerberus.conversation_reply"
            + "(cr_id, reply, ip, time, status, c_id_fk, typeUser)"
            + f"values(0, '{message}','192.168.0.1', '{hour}', 1, {valueC}, '{statusU}'); "
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def getConvByIdConv(self, id_conv):
        con, cursor = self.__createCursor()
        id_conVe = id_conv
        sql = (
            "select * from proyectocerberus.conversation_reply where"
            + f" c_id_fk = {id_conVe} ; "
        )
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def getHour(self):
        now = datetime.now()
        hour = now.time()
        hourStr = str(hour)
        hour_str = hourStr[0 : len(hourStr) - 7]
        print(hour_str)
        return hour_str

    def getDay(self):
        now = datetime.now()
        day = now.date()
        return day

