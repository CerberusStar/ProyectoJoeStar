from ClaseAMPL import SolverWithAMPL
import os
import time


class Control:
    def __init__(self):
        self.urlCarpetaCodigo = os.getcwd() + "\\codigosAMPL\\"
        self.urlCarpetaData = os.getcwd() + "\\datosAMPL\\"

    def createArchive(self, filename, listVariables, listPrices, listRestrictions):
        # Creación de ambos ".txt"
        filenameComplete = filename + ".txt"
        rutacompletaCodigo = self.urlCarpetaCodigo + filenameComplete
        rutacompletaData = self.urlCarpetaData + filenameComplete

        # ".txt" donde se va a guardar la data (ARCHIVO VACIO)
        file = open(rutacompletaData, "w")
        file.close()

        # ".txt" donde se va a guardar el código
        file = open(rutacompletaCodigo, "w")

        # Empezar a escribir el código de AMPL
        # Escribir las variables
        for var in listVariables:
            file.write(f"var {var} integer >= 0;" + os.linesep)

        # Escribir la Función a optimizar
        # Unir las dos listas de datos principales en un String
        position = 0
        Funcion = ""
        for var in listVariables:
            variable = str(var)
            precio = str(listPrices[position])
            position += 1
            Funcion += precio + "*" + variable + " + "
        FuncionArreglada = Funcion.rstrip(" + ;")
        # Escribe en el ".txt" la Función a optimizar
        file.write(f"minimize cost: {FuncionArreglada};" + os.linesep)

        # Escribir las restricciones
        numeroRestriccion = 1
        for restriccion in listRestrictions:
            file.write(
                f"subject to Restriccion{numeroRestriccion}: {restriccion};"
                + os.linesep
            )
            numeroRestriccion += 1

        # Escribir los displays para guardar la data en otro archivo
        # Escribir el comando 'solve' para que AMPL trabaje la data
        RutaSolverGurobi = os.getcwd() + "\\AMPL\\gurobi.exe"
        print(RutaSolverGurobi)
        file.write(f'option solver "{RutaSolverGurobi}";' + os.linesep)
        file.write(f"solve;" + os.linesep)
        # Guardar los datos mediante displays (Código AMPL)
        StringVariables = ""
        for var in listVariables:
            StringVariables += str(var) + ","
        StringVariablesFixed = StringVariables.rstrip(",")
        # Escribir el comando y especificarle donde guardar los archivos
        file.write(f"display {StringVariablesFixed} > {rutacompletaData};")

        # Cerrar el archivo
        file.close()

        # Correr el archivo en AMPL
        # Inicializar AMPL dandole la url del programa
        RutaAMPL = os.getcwd() + "\\AMPL\\ampl.exe"
        test = SolverWithAMPL(RutaAMPL)
        # Ejecutar el código que acabo de crear
        test.ejecutarCodigo(rutacompletaCodigo)
        return None

    def controlDeError(self, filename):
        filenameComplete = filename + ".txt"
        rutacompletaData = self.urlCarpetaData + filenameComplete
        time.sleep(5.5)
        archivo = open(f"{rutacompletaData}", "r")
        data = archivo.read()
        if data != "":
            archivo.close()
            return 1
        else:
            archivo.close()
            return 0

    def borrarArchivo(self, filename):
        filenameComplete = filename + ".txt"
        rutacompletaCodigo = self.urlCarpetaCodigo + filenameComplete
        rutacompletaData = self.urlCarpetaData + filenameComplete
        os.remove(rutacompletaCodigo)
        os.remove(rutacompletaData)
        return None
