class analizadorOperaciones:
    #metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.numeroError = 1
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
        if( caracter == chr(40) # (
        or caracter == chr(41) # )
        or caracter == chr(42) # *
        or caracter == chr(43) # +
        or caracter == chr(45) # -        
        or caracter == chr(47)): # /
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


    #automata
    def automata(self):
        #apuntador para saber en que parte de la cadena
        puntero = 0

        #recorrido de la cadena hasta llegar al final
        while puntero < len(self.txtEntrada):
            
            #----------------------------------------------------------------
            # ESTADO INICIAL ESTADO 0 
            if self.estado == 0:
                # revision si viene un simbolo en la cadena
                if self.isSymbol(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1

                #revision si viene un digito
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2

                #si viene un letra
                elif self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                # si viene un espacio en blanco
                elif self.txtEntrada[puntero] == " ":
                    self.columna += 1  


                # si viene un tabulacion o un retorno de carro
                elif (self.txtEntrada[puntero] == "\t"
                or self.txtEntrada[puntero] == "\r"):
                    pass

                    
                # si vien un salto de linea
                elif self.txtEntrada[puntero] == "\n":
                    self.columna = 0
                    self.fila += 1


                else:
                    #numero fila columna token
                    self.token += self.txtEntrada[puntero]
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    print("Error lexico: "+self.token)  
                    self.numeroError += 1
                    self.columna += 1
                    self.token = ""

            
            #------------------------------------------------------------------
            # ESTADO PARA SIMBOLOS y/o ACEPTACION
            elif self.estado == 1:
                self.addToken(self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0
                puntero -= 1

            #-------------------------------------------------------------------
            # ESTADO PARA DIGITOS
            elif self.estado == 2:
                # si viene un numero en la cadena
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2

                # si viene un punto en la cadena
                elif self.txtEntrada[puntero] == chr(46): # .
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3


                #aceptacion
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1



            # ESTADO PARA PUNTO
            elif self.estado == 3:
                #si viene un digito
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 4

                #ACEPTACION
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            # ESTADO PARA ACEPTACION DE NUMEROS DECIMAL
            elif self.estado == 4:
                #si viene un digito
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 4


                #ACEPTACION
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1



            #----------------------------------------------------------------------
            # ESTADO PARA IDENTIFICADORES
            elif self.estado == 5:
                # si viene una letr en la cadena
                if self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                # si viene un numero
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                # si viene un guien bajo _
                elif self.txtEntrada[puntero]==chr(95):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                #ACEPTACION DE LA CADENA
                else:
                    self.addToken(self.token)
                    print("Token: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #muevo el puntero para el siguiente caracter
            #dentro del texto
            puntero += 1


        #retorno la lista de erroes si existieran
        return self.listaErrores