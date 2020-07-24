from Controladora import Control
import os

# Esta ruta
# CodigosAMPL
Archivo = "AbelCardenas"

# DataConseguida
listaVariables = ["Hamburguesa", "Pupusas", "Carne", "LibraDeArroz"]
listaPrecios = [2.5, 3, 2.65, 3.25]
listaRestricciones = [
    "0.5*Hamburguesa+0.3*Pupusas+0.4*Carne+0.32*LibraDeArroz>=10",
    "LibraDeArroz=2",
    "0.4*Pupusas+0.5*Carne>=7",
]

Ui = Control()
Ui.createArchive(Archivo, listaVariables, listaPrecios, listaRestricciones)
