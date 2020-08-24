class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0 # estado actual del automa
        # element token error
        self.numError = 0 
        self.filaError = 0 # fila
        self.columnaError = 0 # columna
        self.token = "" # token
        self.listaErrores = [] # listado para los erroes
        self.listaReservadas = ["var","true","false","if","else","for","while","do",
        "break","return","this","console","Math","pow"]

    #----------------------------------------------
    # metodo para verificacion de tipo de caracter
    # verificacion si es un una letra
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

    # verificacion si un es un simbolo permitido por el lenguaje JS
    def isSymbol(self,caracter):
        if ( caracter == chr(33) # !
        or caracter == chr(38) # &
        or caracter == chr(39) # '
        or caracter == chr(40) # (
        or caracter == chr(41) # )
        or caracter == chr(42) # *
        or caracter == chr(43) # +
        or caracter == chr(45) # -
        or caracter == chr(46) # .
        or caracter == chr(58) # :
        or caracter == chr(59) # ;
        or caracter == chr(60) # <
        or caracter == chr(61) # =
        or caracter == chr(62) # >
        or caracter == chr(123) # {
        or caracter == chr(124) # |
        or caracter == chr(125)): # }
            return True
        else:
            return False

    #-----------------------------------------------
    # metodo para analizar token por token
    # verificacion de la cadena
    def automata(self):
        # puntero indica que parte de la cadena vamos
        puntero = 0

        # while mientras no hemos llegado al final de la cadena
        while puntero < len(self.txtEntrada):
            
            # estado inicial
            if self.estado == 0:
                # revision de de entrada en la cadena
                # es una letra
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.estado = 1

                # es un digito
                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.estado = 2

                # es un simbolo permitido por el lenguaje
                elif self.isSymbol(self.txtEntrada[puntero]) == True:
                    self.estado = 3

                # posible comentarios
                elif self.txtEntrada[puntero] == chr(47):
                    self.estado = 4

                # movientos en el cursos
                elif (self.txtEntrada[puntero] == ' '
                or self.txtEntrada[puntero] == '\n'
                or self.txtEntrada[puntero] == '\t'
                or self.txtEntrada[puntero] == '\r'):
                    #ignoro paso al siguiente caracter
                    puntero += 1
                    self.estado = 0

                # error lexico
                else:
                    pass

            # estado de letras, palabras reservadas o id
            if self.estado == 1:
                
                # aceptacion del estado L|D|_
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 1

                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 1

                elif self.txtEntrada[puntero] == chr(95): # _
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 1

                # prueba de existensia de palabra reservada o id
                else:
                    pass

            # estado para numeros
            if self.estado == 2:
                # acpetacion para numero
                if self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 2


                else:
                    pass


            # estado para simbolos
            if self.estado == 3:
                # aceptacion para algun simbolo del lenguaje JS
                if self.isSymbol(self.txtEntrada[puntero]) == True:
                    self.token = self.txtEntrada[puntero]
                    self.estado = 0 # regreso al estado 0
                    puntero +=1

                # erro lexico
                else:
                    pass

            # estado para posibles comentarios
            if self.estado == 4:
                # acpetacion del simbolo /
                if self.txtEntrada[puntero] == chr(47): # /
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 4

                # comentario multilinea
                elif self.txtEntrada[puntero] == chr(42): # *
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 6

            # estado para comentarios unilinea
            if self.estado == 5:
                pass

            if self.estado == 6:
                # aceptar todo todillo
                if self.txtEntrada[puntero] != chr(42): # *
                    self.token = self.toke + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 6
                # posible cierre de comentario
                else:
                    self.estado = 7

            # estado para verificar si va se cerrar comentario multilinea
            if self.estado == 7:
                pass

            if self.estado == 8:
                pass

            