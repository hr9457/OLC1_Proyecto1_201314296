import os
import io

class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0 # estado actual del automa
        # element token error
        self.numeroError = 1 
        self.fila = 0 # fila
        self.columna = 0 # columna
        self.token = "" # token
        self.listaErrores = [] # listado para los erroes
        self.listaToken = []
        self.listaReservadas = ["var","if","else","for","do","while","console",
        "continue","break","return","false","true","this","constructor",
        "Math","function","class"] # lista de palabras reservadas
        #ruta de salida para el archivo en limpio
        self.rutaSalida  =  ""



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
        or caracter == chr(44) # ,
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
    def addToken(self,lexema,token):
        self.listaToken.append([lexema,token])

    # error lexico
    def errorLexico(self,numero,fila,columna,token):
        self.listaErrores.append([""+str(numero),""+str(fila),
        ""+str(columna),token])



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
                if (self.isLetter(self.txtEntrada[puntero]) == True
                or self.txtEntrada[puntero] == chr(95)):
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
                    self.addToken("carrito"," ")
                    self.columna += 1
                    self.estado = 0

                # tabulacion
                elif (self.txtEntrada[puntero] == '\t'
                or self.txtEntrada[puntero] == '\r'):
                    self.addToken("carrito","\t")

                # salto de linea
                elif self.txtEntrada[puntero] == '\n':
                    self.addToken("carrito","\n")
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
                    #buscando la concatenacion en la lista de palabras reservadas
                    if self.token in self.listaReservadas:
                        self.addToken("Tk_reservada",self.token)
                        print("RESERVADA : "+self.token)
                        self.token = ""
                        self.columna += 1
                        self.estado = 0
                        puntero -= 1
                    else:
                        self.addToken("Tk_id",self.token)
                        print("ID : "+self.token)
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


                # para nuemros decimales
                elif self.txtEntrada[puntero] == chr(46): # punto .
                    self.token += self.txtEntrada[puntero]
                    self.estado = 15


                # ACEPTO
                else:
                    self.addToken("Tk_digito",self.token)
                    print("Numero : "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            
            


            #-----------------------------------------------------------
            #ESTADO DE ACEPTACION PARA SIMBOLOS
            # estado para simbolos
            elif self.estado == 3:
                lex = self.txtEntrada[puntero]
                self.addToken("Tk_operador",self.token)
                print("Operador: "+self.token)
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
                    self.addToken("Tk_operador",self.token)
                    print("operador : "+self.token)
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
                    self.addToken("Tk_comentario",self.token)
                    print("COMENTARIO : "+self.token)
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
                    #self.token += self.txtEntrada[puntero]
                    puntero -= 1
                    self.estado = 6

                else:
                    # paso al estado 8 de aceptacion
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8
                    


            #-----------------------------------------------------------------
            # estado para verificar si va se cerrar comentario multilinea
            elif self.estado == 8:
                self.addToken("Tk_comentario",self.token)
                print("COMENTARIO : "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0
                puntero -= 1



            #---------------------------------------------------------------------
            # estado para cadenas de string
            elif self.estado == 9:
                #self.addToken(self.token)
                #print("Token: "+self.token)
                #self.token = ""
                #self.columna += 1
                if self.txtEntrada[puntero] == chr(34): # ""
                    self.token += self.txtEntrada[puntero]
                    self.estado = 11

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
                    #self.addToken(self.token)
                    #print("Cadena: "+self.token)
                    #self.token = ""  
                    #self.columna += 1
                    self.token += self.txtEntrada[puntero]
                    self.estado = 11
                    puntero -= 1


            # acpetacion de las comillas dobles
            elif self.estado == 11:
                #self.token = self.txtEntrada[puntero]
                self.addToken("Tk_string",self.token)
                print("CADEMA : "+self.token)
                self.token = ""  
                self.columna += 1
                self.estado = 0



            # si viene un ' comilla simple en la cadena
            elif self.estado == 12:
                #lex = self.txtEntrada[puntero]
                #self.addToken(self.token)
                #print("Token: "+self.token)
                #self.token = ""
                #self.columna += 1
                #si viene un comilla simple
                if self.txtEntrada[puntero] == chr(39): # '
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14
                    puntero -= 1

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13


            # contenido de todas las comillas en el contenido
            elif self.estado == 13:
                if self.txtEntrada[puntero] != chr(39): # '
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13
                else:
                    #impresion del token
                    #self.addToken(self.token)
                    #print("Cadena: "+self.token)
                    #self.token = ""  
                    #self.columna += 1
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14
                    puntero -= 1


            # aceptacion de las comillas simples
            elif self.estado == 14:
                #self.token = self.txtEntrada[puntero]
                self.addToken("Tk_string",self.token)
                print("CADENA : "+self.token)
                self.token = ""  
                self.columna += 1
                self.estado = 0


            # para punto decimal
            elif self.estado == 15:
                if self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 16

                else:                    
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    print("Error lexico: "+self.token)                    
                    self.token = ""
                    self.numeroError += 1
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #---------------------------------------------------------------
            #ACEPTACION PARA NUMEROS DECIMALES
            elif self.estado == 16:
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 16

                else:
                    self.addToken("Tk_digito",self.token)
                    print("DIGITO :"+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1

            
            #pasa al siguiente caracter
            #y sigue con ele while
            puntero += 1



        self.destino()
        # retorno de la lista con los error encontrados en el archivo
        return self.listaErrores
        



    #----------------------------------------------------------------------------------------------
    #metodo para la creacion de la carpet destino para el archivo de JS
    def destino(self):
        if len(self.listaToken) == 0:
            print("---->No hay elementos en la lista")
        else:
            #guardo la ruta 
            self.rutaSalida = self.listaToken[0][1]
            print("---------->"+self.rutaSalida)
            separacionArchivo = self.rutaSalida.split("output")
            print(""+separacionArchivo[1])
            carpetaDestino = 'salidaArchivos\\'+separacionArchivo[1]
            os.makedirs(carpetaDestino)
            archivoSalidaJS = open(""+carpetaDestino+"\\Salida.js","w")
            #********************************************************
            #ESCIRTURA PARA EL ARCHIVO DE SALIDA
            for fila in range(len(self.listaToken)):
                archivoSalidaJS.write(""+self.listaToken[fila][1])

            archivoSalidaJS.close()

