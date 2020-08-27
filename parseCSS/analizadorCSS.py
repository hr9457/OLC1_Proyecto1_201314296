class analizadorcss:
    
    #contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.fila = 0
        self.columna = 0
        self.token = ""
        self.listaErrores = []
        self.listaToken = []
        self.palabrasReservadas = []

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
        if(caracter == chr(35) # #
        or caracter == chr(37) # %
        or caracter == chr(40) # (
        or caracter == chr(41) # )
        or caracter == chr(44) # ,
        or caracter == chr(45) # -
        or caracter == chr(46) # .
        or caracter == chr(58) # :
        or caracter == chr(59) # ;
        or caracter == chr(61) # =
        or caracter == chr(123) # {
        or caracter == chr(125)): # }
            return True
        else:
            return False

    # agreacion de token
    def addToken(self,token):
        self.listaToken.append(token)

    # error lexico
    def errorToken(self,numero,fila,columna,token):
        self.listaErrores.append(["No","Fila","Columna","Error"])


    #automata
    def automata(self):
        #puntero para saber parte del texto
        puntero = 0

        #recorrido de la cadena con un while
        #recorrido hasta que no llegue al final de la cadena
        while puntero < len(self.txtEntrada):
            pass



