class CodigoControl:

    CODIGO_DE_CONTROL = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

    def __init__(self, numeroDni=0, letraDni=''):
        self.numeroDni = numeroDni
        self.letraDni = letraDni

    def asignarLetra(self):
        return self.CODIGO_DE_CONTROL[self.numeroDni % 23]
    
    def comprobarLetra(self):
        return True if self.asignarLetra() == self.letraDni else False