class CourseObj:
    def __init__(
        self, id, name, description, duration, cost, iduser, idtrainer, estado,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration
        self.cost = cost
        self.iduser = iduser
        self.idtrainer = idtrainer
        self.estado = estado

    def iduser(self):
        name = self.iduser
        return name
