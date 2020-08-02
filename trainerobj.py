class TrainerObj:
    def __init__(
        self, id, firstname, lastname, username, password, description, email,
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.description = description
        self.email = email

    def getname(self):
        name = self.firstname
        return name

    def getapellido(self):
        apellido = self.lastname
        return apellido
