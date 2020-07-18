import subprocess


class SolverWithAMPL:
    def __init__(self, urlAMPL):
        self.urlAMPL = urlAMPL

    def ejecutarCodigo(self, urlArchivo):
        self.urlArchivo = urlArchivo
        subprocess.Popen("%s %s" % (self.urlAMPL, self.urlArchivo))
        return "Exito ejecutando en AMPL"
