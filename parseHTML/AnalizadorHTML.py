# anlizar para la parte del archivo en html
class AnalizadorHTML:
    
    # metodo contructor
    def __init__(self,txtEntrada,nombreArchivo):
        self.txtEntrada = txtEntrada
        self.nombreArchivo = nombreArchivo
        self.estado = 0
        self.numeroError = 1
        self.fila = 0
        self.columna = 0
        self.token = ""
        self.listaErrores = []
        self.listaToken = []


    # metodo para saber si es una letra
    def isLetter(self,caracter):
        if ( (caracter >= chr(65) and caracter <= chr(90))
        or (caracter >= chr(97) and caracter <= chr(122)) ):
            return True
        else:
            return False

    # verificion si es un numero
    def isNumber(self,caracter):
        if (caracter >= chr(48) and caracter <= chr(57)):
            return True
        else:
            return False

    # verificacion si un es un simbolo permitido por el lenguaje CSS
    # 12 simbolos identificados
    def isSymbol(self,caracter):
        if caracter == chr(61): # =
            return True
        else:
            return False

    # agreacion de token
    def addToken(self,token,lexema):
        self.listaToken.append([token,lexema])

    # error lexico
    def errorLexico(self,numero,fila,columna,token):
        self.listaErrores.append([""+str(numero),""+str(fila),
        ""+str(columna),token])


    #*************************************************************
    #automata
    def automata(self):
        puntero = 0
