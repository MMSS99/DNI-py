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
        return self.dni + CodigoControl(int(self.getDni())).asignarLetra()

    def comprobarDni(self):
        return True if CodigoControl(self.getNumero(), self.getLetra()).comprobarLetra() else False