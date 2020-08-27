class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada,areaTexto):
        self.areaTexto = areaTexto
        self.txtEntrada = txtEntrada
        self.estado = 0 # estado actual del automa
        # element token error
        self.numError = 0 
        self.filaError = 1 # fila
        self.columnaError = 0 # columna
        self.token = "" # token
        self.listaErrores = [] # listado para los erroes
        self.listaReservadas = ["var","true","false","if","else","for","while","do",
        "break","return","this","console","Math","pow"]
        self.listadoSimbolos = ["!","&","(",")","*","+","+","-",".",";","<","=",">","{","|","}"]



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
        or caracter == chr(91) # [
        or caracter == chr(93) # ]
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
                # es una letra pasa al estado 1
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.estado = 1


                # es un digito pasa al estado 2
                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.estado = 2


                # es un simbolo permitido por el lenguaje pasa al estado 3
                elif self.isSymbol(self.txtEntrada[puntero]) == True:
                    self.estado = 3


                # posible comentarios pasa al estado 4
                elif self.txtEntrada[puntero] == chr(47): # /
                    self.estado = 4


                # posible cadena de texto estado 9 
                elif self.txtEntrada[puntero] == chr(34): # "
                    self.estado = 10


                # movientos en el cursos
                elif (self.txtEntrada[puntero] == ' '):
                    #ignoro paso al siguiente caracter
                    self.columnaError += 1
                    puntero += 1
                    self.estado = 0

                # tabulacion
                elif (self.txtEntrada[puntero] == '\t'
                or self.txtEntrada[puntero] == '\r'):
                    self.columnaError += 1
                    puntero += 1
                    self.estado = 0

                # salto de linea
                elif self.txtEntrada[puntero] == '\n':
                    self.filaError += 1
                    self.columnaError = 0
                    puntero += 1
                    self.estado = 0


                # ERROR LEXICO
                else:
                    #mando a lista de errores
                    self.listaErrores.append(["No."+str(self.numError),"  Fila:"+str(self.filaError),
                    "  Columna:"+str(self.columnaError),"  Error:"+self.txtEntrada[puntero]])
                    #self.columnaError += 1
                    self.numError += 1
                    #impresion del token
                    print("ERROR LEXICO: "+self.txtEntrada[puntero])
                    self.token =  ""
                    self.estado = 0
                    puntero += 1


            #-----------------------------------------------------------
            #ACEPTACION DE CADENA O ID
            # estado de letras, palabras reservadas o id
            if self.estado == 1:
                
                # aceptacion del estado L|D|_
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    #self.columnaError += 1
                    puntero += 1
                    self.estado = 1


                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    #self.columnaError += 1
                    puntero += 1
                    self.estado = 1


                elif self.txtEntrada[puntero] == chr(95): # _
                    self.token = self.token + self.txtEntrada[puntero]
                    #self.columnaError += 1
                    puntero += 1
                    self.estado = 1


                # ACEPTO
                else:
                    #impresion del token
                    print("Token: "+self.token)
                    self.token = ""
                    self.columnaError += 1
                    self.estado = 0


            #--------------------------------------------------------------
            # estado para numeros
            if self.estado == 2:
                # acpetacion para numero
                if self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]
                    #self.columnaError += 1
                    puntero += 1
                    self.estado = 2


                # ACEPTO
                else:
                    #impresion del token
                    print("Token: "+self.token)
                    self.token = ""
                    self.columnaError += 1
                    self.estado = 0



            #-----------------------------------------------------------
            # estado para simbolos
            if self.estado == 3:
                # aceptacion para algun simbolo del lenguaje JS
                if self.isSymbol(self.txtEntrada[puntero]) == True:
                    self.token = self.token + self.txtEntrada[puntero]   
                    #self.areaTexto.tag_add()                 
                    #impresion del token
                    print("Simbolo: "+self.token)                    
                    self.columnaError += 1
                    puntero +=1
                    self.token = ""
                    self.estado = 0 # regreso al estado 0



            # estados para comentarios           
            #------------------------------------------------------------------
            # estado para posibles comentarios
            if self.estado == 4:
                self.token = self.token + self.txtEntrada[puntero]
                print("Token: "+self.token)
                self.token = ""
                self.columnaError += 1
                puntero += 1

                # acpetacion del simbolo / pasa al estado 5
                if self.txtEntrada[puntero] == chr(47): # /
                    self.token = self.token + self.txtEntrada[puntero]
                    print("Token: "+self.token)
                    self.token = ""
                    self.columnaError += 1
                    puntero += 1
                    self.estado = 5 # pasa al estado 5


                # comentario multilinea paso al estado 7
                elif self.txtEntrada[puntero] == chr(42): # *
                    self.estado = 6


                # ACEPTO LA CADENA
                else:
                    #impresion del token
                    self.token = ""
                    self.columnaError += 1
                    self.estado = 0



            #--------------------------------------------------------
            #ESTADO DE ACEPTACION DE COMENTARIO UNILINEA
            # estado para comentarios unilinea
            if self.estado == 5:
                # acepto todo todillo 
                if (self.txtEntrada[puntero] != '\n'
                or puntero > len(self.txtEntrada)):
                    self.token = self.token + self.txtEntrada[puntero]
                    self.estado = 5
                    puntero += 1

                # ACEPTO LA CADENA 
                else:
                    #impresion del token
                    print("Cadena : "+self.token)
                    self.token = ""
                    self.columnaError = 0
                    self.filaError += 1
                    self.estado = 0



            #---------------------------------------------------------------
            # comentario multilinea
            if self.estado == 6:
                # aceptar todo todillo
                if self.txtEntrada[puntero] == chr(42): # *
                    self.token = self.token + self.txtEntrada[puntero]
                    #impresion del token
                    print("Token : "+self.token)
                    self.token = ""
                    puntero += 1
                    self.columnaError += 1
                    self.estado = 7

                # posible cierre de comentario
                else:
                    pass


            
            if self.estado == 7:
                # revision de posible cierre de comentario multilinea
                if self.txtEntrada[puntero] != chr(42): # *
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1
                    #self.columnaError += 1
                    self.estado = 7

                else:
                    # paso al estado 8 de aceptacion
                    self.estado = 8
                    


            #-----------------------------------------------------------------
            # estado para verificar si va se cerrar comentario multilinea
            if self.estado == 8:
                # acepto la cade de comentario multilinea 
                if (self.txtEntrada[puntero] == chr(42)
                and self.txtEntrada[puntero + 1] == chr(47)):# */
                    #impresion del token
                    print("Token : "+self.token)
                    self.token = ""
                    self.token = self.token + self.txtEntrada[puntero]
                    print("Token : "+self.token)
                    self.token = ""
                    puntero += 1
                    self.columnaError += 1

                elif self.txtEntrada[puntero] == chr(42):
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1

                elif self.txtEntrada[puntero] == chr(47): # /
                    #impresion del token
                    self.token = ""
                    self.estado = 9

                else:
                    self.token = self.token + self.txtEntrada[puntero]
                    self.estado = 7


            #ACPETACION DE COMENTARIO MULTILINEA
            if self.estado == 9:
                if self.txtEntrada[puntero] == chr(47):# /
                    self.token = self.token + self.txtEntrada[puntero]
                    #impresion del token
                    print("Token : "+self.token)
                    self.token = ""
                    puntero +=1
                    self.estado = 0



            #--------------------------------
            # estado para cadenas de string
            if self.estado == 10:
                self.token = self.token + self.txtEntrada[puntero]                 
                print("Token: "+self.token)
                self.token = ""
                puntero += 1
                # concateno todo lo que venga 
                if self.txtEntrada[puntero] == chr(34): # "
                    self.token = self.token + self.txtEntrada[puntero]                 
                    print("Token: "+self.token)
                    self.token = ""                 
                    puntero += 1
                    self.estado = 0

                # ACEPTO
                else:

                    self.token = ""
                    self.columnaError += 1
                    self.estado = 11
                    

            if self.estado == 11:
                # concateno todo hasta encontrar "
                if self.txtEntrada[puntero] != chr(34): # "
                    self.token = self.token + self.txtEntrada[puntero]
                    puntero += 1

                # ACEPTO
                else:
                    #impresion del token
                    print("Cadena: "+self.token)
                    self.token = ""
                    self.columnaError += 1
                    self.estado = 12


            if self.estado == 12:
                # 
                if self.txtEntrada[puntero] == chr(34): # "
                    self.token = self.token + self.txtEntrada[puntero]
                    #impresion del token
                    print("Token : "+self.token)
                    self.token = ""
                    puntero +=1
                    self.estado = 0



        # retorno de la lista con los error encontrados en el archivo
        return self.listaErrores

