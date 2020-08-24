from Logic import Logic
from walletobj import WalletObj

class WalletLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = ["id", "iduser", "tarjeta", "cvv", "month", "year", "ownercard", "date", "amount"]

    def getWalletData(self, iduser):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.pays where iduser='{iduser}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            wallet = WalletObj(
                data_dic["id"],
                data_dic["iduser"],
                data_dic["tarjeta"],
                data_dic["cvv"],
                data_dic["month"],
                data_dic["year"],
                data_dic["ownercard"],
                data_dic["date"],
                data_dic["amount"],
            )
            return wallet
        else:
            return None
    
    def insertToWallet(self, id, iduser, tarjeta, cvv, month, year, ownercard, date, amount):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.pays (id, iduser, tarjeta, cvv, month, year, ownercard, date, amount) "
            + f"VALUES ('0', '{iduser}', '{tarjeta}', '{cvv}', '{month}', '{year}', '{ownercard}', '{date}', '{amount}');"
        )
        data = database.executeNonQueryBool(sql)
        return data

    def updateWallet(self, iduser):
        database = self.get_databaseXObj()
        #consigo la cantidad ingresada
        sqlPay = (f"select amount from proyectocerberus.pays where (iduser = '{iduser}');")
        paymentData = database.executeQuery(sqlPay)
        payment = float(paymentData[0][0])
        # Consigo el dinero actual del usuario
        sqlgetWallet = (
            f"select wallet from proyectocerberus.user where (iduser = '{iduser}');"
        )
        userWallet = database.executeQuery(sqlgetWallet)
        userWalletData = float(userWallet[0][0])
        # actualizo el wallet del user
        AdjustedWallet = userWalletData + payment
        sql=(f"UPDATE proyectocerberus.user SET wallet = {AdjustedWallet} WHERE (iduser = '{iduser}');")
        data = database.executeNonQueryBool(sql)
        return data