from Logic import Logic
from userobj import UserObj

import mysql.connector
from mysql.connector import Error
import os
import pymysql.cursors

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

    def getUserDataByID(self, id):
            database = self.get_databaseXObj()
            sql = f"select * from proyectocerberus.user where iduser='{id}';"
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

    def updateUser(self, id, nombre, apellido, password, email, peso, edad, altura):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE proyectocerberus.user SET "
            + f"firstname = '{nombre}', lastname = '{apellido}', password = '{password}', "
            + f"email = '{email}', weigth = '{peso}', age = '{edad}', size = '{altura}'  WHERE (iduser = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, "rb") as file:
            binaryData = file.read()
        return binaryData

    def insertphotoUser(self, username, photo):
        try:
            connection = mysql.connector.connect(
                host="localhost", database="proyectocerberus", user="root", password="12345"
            )
            cursor = connection.cursor()

            sql_insert_blob_query = """UPDATE proyectocerberus.user SET photo = %s WHERE (username = %s)"""
            empPicture = self.convertToBinaryData(photo)

            #Convert data into tuple format
            insert_blob_tuple = (empPicture, username)

            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            
            print(
                f"Image and file inserted successfully as a BLOB into python_employee table {result}"
            )
            return True    
        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))

    def convertToDoc(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
            with open(filename, "wb") as file:
                file.write(data)

    def readBLOB(self, user):
        print("Reading BLOB data from python_employee table")

        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="12345",
                db="proyectocerberus",
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
            )
            with connection.cursor() as cursor:
                sql_fetch_blob_query = (
                    """SELECT photo from proyectocerberus.user where username = %s"""
                )

                cursor.execute(sql_fetch_blob_query, (user,))
                record = cursor.fetchall()
                for row in record:
                   # print("Name = ", row["name"])
                    image = row["photo"]
                    if image is not None:
                        print("Storing employee image and bio-data on disk \n")
                        photo = os.getcwd() + f"\\static\\uploads\\{user}.jpg"
                        self.convertToDoc(image, photo)
                        return f"{user}.jpg"
                    else:
                        return ""

        except mysql.connector.Error as error:
            print("Failed to read BLOB data from MySQL table {}".format(error))
            
        


    
