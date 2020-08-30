class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0 # estado actual del automa
        # element token error
        self.numeroError = 0 
        self.fila = 0 # fila
        self.columna = 0 # columna
        self.token = "" # token
        self.listaErrores = [] # listado para los erroes
        self.listaToken = []
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
        or caracter == chr(91) # [
        or caracter == chr(93) # ]
        or caracter == chr(123) # {
        or caracter == chr(124) # |
        or caracter == chr(125)): # }
            return True
        else:
            return False

    # agreacion de token
    def addToken(self,token):
        self.listaToken.append(token)

    # error lexico
    def errorLexico(self,numero,fila,columna,token):
        self.listaErrores.append(["No :"+str(numero),"  Fila: "+str(fila),
        "  Columna: "+str(columna),"  Error: "+token])



    #*********************************************************************************
    #---------------------------------------------------------------------------------
    # metodo para analizar token por token
    # verificacion de la cadena
    def automata(self):
        # puntero indica que parte de la cadena vamos
        puntero = 0

        # while mientras no hemos llegado al final de la cadena
        while puntero < len(self.txtEntrada):
            
            #----------------------------------------------------------------------
            #ESTADO INICIAL
            # estado inicial
            if self.estado == 0:
                # revision de de entrada en la cadena
                # es una letra pasa al estado 1
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1


                # es un digito pasa al estado 2
                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                # es un simbolo permitido por el lenguaje pasa al estado 3
                elif self.isSymbol(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3


                # posible comentarios pasa al estado 4
                elif self.txtEntrada[puntero] == chr(47): # /
                    self.token += self.txtEntrada[puntero]
                    self.estado = 4


                # posible cadena de texto estado 9  ""
                elif self.txtEntrada[puntero] == chr(34): # "
                    self.token += self.txtEntrada[puntero]
                    self.estado = 9

                #posibilidad de caracter
                elif self.txtEntrada[puntero] == chr(39):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 12


                # movientos en el cursos
                elif (self.txtEntrada[puntero] == ' '):
                    #ignoro paso al siguiente caracter
                    self.columna += 1
                    self.estado = 0

                # tabulacion
                elif (self.txtEntrada[puntero] == '\t'
                or self.txtEntrada[puntero] == '\r'):
                    pass

                # salto de linea
                elif self.txtEntrada[puntero] == '\n':
                    self.fila += 1
                    self.columna = 0
                    self.estado = 0


                # ERROR LEXICO
                else:
                    #numero fila columna token
                    self.token += self.txtEntrada[puntero]
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    print("Error lexico: "+self.token)                    
                    self.token = ""
                    self.numeroError += 1
                    self.columna += 1


            #-----------------------------------------------------------
            #ACEPTACION DE CADENA O ID
            # estado de letras, palabras reservadas o id
            elif self.estado == 1:
                
                # aceptacion del estado L|D|_
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1


                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1


                elif self.txtEntrada[puntero] == chr(95): # _
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1


                # ACEPTO
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #--------------------------------------------------------------
            # ESTADO ACEPTACION DE NUMEROS
            # estado para numeros
            elif self.estado == 2:
                # acpetacion para numero
                if self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                # ACEPTO
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1



            #-----------------------------------------------------------
            #ESTADO DE ACEPTACION PARA SIMBOLOS
            # estado para simbolos
            elif self.estado == 3:
                lex = self.txtEntrada[puntero]
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0
                puntero -= 1





            # estados para comentarios           
            #------------------------------------------------------------------
            # estado para posibles comentarios
            elif self.estado == 4:
                # acpetacion del simbolo / pasa al estado 5
                if self.txtEntrada[puntero] == chr(47): # /  
                    self.token +=  self.txtEntrada[puntero]
                    self.estado = 5 # pasa al estado 5

                # comentario multilinea paso al estado 7
                elif self.txtEntrada[puntero] == chr(42): # *
                    self.token +=  self.txtEntrada[puntero]
                    self.estado = 6


                # ACEPTO LA CADENA
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #--------------------------------------------------------
            #ESTADO DE ACEPTACION DE COMENTARIO UNILINEA
            # estado para comentarios unilinea
            elif self.estado == 5:
                # acepto todo todillo 
                if self.txtEntrada[puntero] != '\n':
                    self.token +=  self.txtEntrada[puntero]
                    self.estado = 5

                # ACEPTO LA CADENA 
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #---------------------------------------------------------------
            # comentario multilinea
            elif self.estado == 6:
                # aceptar todo todillo
                if self.txtEntrada[puntero] != chr(42): # *
                    self.token += self.txtEntrada[puntero]
                    self.estado = 6

                # posible cierre de comentario
                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 7


            
            elif self.estado == 7:
                # revision de posible cierre de comentario multilinea
                if self.txtEntrada[puntero] != chr(47): # /
                    self.token += self.txtEntrada[puntero]
                    self.estado = 6

                else:
                    # paso al estado 8 de aceptacion
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8
                    


            #-----------------------------------------------------------------
            # estado para verificar si va se cerrar comentario multilinea
            elif self.estado == 8:
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0
                puntero -= 1



            #---------------------------------------------------------------------
            # estado para cadenas de string
            elif self.estado == 9:
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                if self.txtEntrada[puntero] == chr(34):
                    self.estado = 11
                    puntero -= 1

                # ACEPTO
                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10
                    
            
            elif self.estado == 10:
                # concateno todo hasta encontrar "
                if self.txtEntrada[puntero] != chr(34): # "
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10

                # ACEPTO
                else:
                    #impresion del token
                    self.addToken(self.token)
                    print("Cadena: "+self.token)
                    self.token = ""  
                    self.columna += 1
                    self.estado = 11
                    puntero -= 1


            # acpetacion de las comillas dobles
            elif self.estado == 11:
                self.token = self.txtEntrada[puntero]
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""  
                self.columna += 1
                self.estado = 0



            # si viene un ' comilla simple en la cadena
            elif self.estado == 12:
                lex = self.txtEntrada[puntero]
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                #si viene un comilla simple
                if self.txtEntrada[puntero] == chr(39):
                    self.estado = 14
                    puntero -= 1

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13


            # contenido de todas las comillas en el contenido
            elif self.estado == 13:
                if self.txtEntrada[puntero] != chr(39):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13
                else:
                    #impresion del token
                    self.addToken(self.token)
                    print("Cadena: "+self.token)
                    self.token = ""  
                    self.columna += 1
                    self.estado = 14
                    puntero -= 1


            # aceptacion de las comillas simples
            elif self.estado == 14:
                self.token = self.txtEntrada[puntero]
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""  
                self.columna += 1
                self.estado = 0


            
            #pasa al siguiente caracter
            #y sigue con ele while
            puntero += 1



        # retorno de la lista con los error encontrados en el archivo
        return self.listaErrores

