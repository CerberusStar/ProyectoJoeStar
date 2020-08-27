class WalletObj:
    def __init__(self, id, iduser, tarjeta, cvv, month, year, ownercard, date, amount):
        self.id = id
        self.iduser = iduser
        self.tarjeta = tarjeta
        self.cvv = cvv
        self.month = month
        self.year = year
        self.ownercard = ownercard
        self.date = date
        self.amount = amount

    def getiduser(self):
        iduser = self.iduser
        return iduser
