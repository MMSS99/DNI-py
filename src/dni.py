from src.codigo_control import CodigoControl

class Dni:

    def __init__(self, dni: str):
        self.dni = dni


    def setDni(self, dni: str):
        self.dni = dni

    def getDni(self):
        return self.dni

    def getNumero(self):
        return int(self.dni[:-1])

    def getLetra(self):
        return self.dni[-1]
    
    def darLetra(self):
        return self.dni + CodigoControl().asignarLetra(int(self.getDni()))

    def comprobarDni(self):
        return True if CodigoControl().comprobarLetra(self.getNumero(), self.getLetra()) else False