# clase para la creacion del token 
class Token:
    # caracteristicas del token  
    # metodo constructor  
    def __init__(self):
        self.__fila = 0
        self.__columna = 0
        self.__lexema = ''
        self.__idToken = ""

    # metodo get y set para lexema y idToken
    def getFila(self):
        return self.__fila

    def setFila(self,fila):
        self.__fila = fila

    def getColumna(self):
        return self.__columna

    def setColumna(self,columna):
        self.__columna = columna

    def getLexema(self):
        return self.__lexema

    def setLexema(self,lexema):
        self.__lexema = lexema

    def getIdToken(self):
        return self.__idToken

    def setIdToken(self,idToken):
        self.__idToken = idToken
