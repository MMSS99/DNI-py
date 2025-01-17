class CodigoControl:

    CODIGO_DE_CONTROL = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

    @classmethod
    def asignarLetra(cls, numero: int):
        return cls.CODIGO_DE_CONTROL[numero % len(cls.CODIGO_DE_CONTROL)]
    
    @classmethod
    def comprobarLetra(cls, numero: int, letra: str):
        return True if cls.asignarLetra(numero) == letra else False