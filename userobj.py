class UserObj:
    def __init__(
        self,
        id,
        nombre,
        apellido,
        usuario,
        password,
        email,
        peso,
        edad,
        altura,
        sexo,
        wallet,
    ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.email = email
        self.peso = peso
        self.edad = edad
        self.altura = altura
        self.sexo = sexo
        self.wallet = wallet

    def getname(self):
        name = self.nombre
        return name

    def getapellido(self):
        apellido = self.apellido
        return apellido
