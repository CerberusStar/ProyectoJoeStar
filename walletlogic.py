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

    def getAllByID(self, iduser):
        database = self.get_databaseXObj()
        sql = f"select * from proyectocerberus.pays where iduser='{iduser}';"
        data = database.executeQuery(sql)
        return data
    
    def insertToWallet(self, id, iduser, tarjeta, cvv, month, year, ownercard, date, amount):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO proyectocerberus.pays (id, iduser, tarjeta, cvv, month, year, ownercard, date, amount) "
            + f"VALUES ('0', '{iduser}', '{tarjeta}', '{cvv}', '{month}', '{year}', '{ownercard}', '{date}', '{amount}');"
        )
        data = database.executeNonQueryBool(sql)
        return data

    def updateWallet(self, iduser, wallet):
        database = self.get_databaseXObj()
        sql=(f"UPDATE proyectocerberus.user SET wallet = {wallet} WHERE (iduser = '{iduser}');")
        data = database.executeNonQueryBool(sql)
        return data