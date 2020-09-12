from parseOperaciones.analizadorSintactico import analizadoSintactico # analizador sintatico op

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
        self.operacion = ""
        self.inicioOperacion = 0
        self.listaErrorOperaciones = []
        self.contador = 0


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
        if caracter == chr(40): # (
            self.addToken("Tk_apertura",caracter)
            return True
        elif caracter == chr(41): # )
            self.addToken("Tk_cierre",caracter)
            return True
        elif caracter == chr(42): # *
            self.addToken("Tk_multipliacion",caracter)
            return True
        elif caracter == chr(43): # +
            self.addToken("Tk_suma",caracter)
            return True
        elif caracter == chr(45): # -  
            self.addToken("Tk_resta",caracter)  
            return True    
        elif caracter == chr(47): # /
            self.addToken("Tk_division",caracter)
            return True
        else:
            return False


    # agreacion de token
    def addToken(self,tipo,token):
        self.listaToken.append([tipo,token])


    # error lexico
    def errorLexico(self,numero,fila,columna,token):
        self.listaErrores.append([""+str(numero),""+str(fila),
        ""+str(columna),""+token])


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
                    # concatengo toda la operacion 
                    self.operacion += self.txtEntrada[puntero]

                #revision si viene un digito
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                #si viene un letra
                elif self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                # si viene un espacio en blanco
                elif self.txtEntrada[puntero] == " ":
                    self.columna += 1  


                # si viene un tabulacion o un retorno de carro
                elif (self.txtEntrada[puntero] == "\t"
                or self.txtEntrada[puntero] == "\r"):
                    pass

                    
                # si vien un salto de linea
                elif self.txtEntrada[puntero] == "\n":
                    self.addToken("tk_salto",self.txtEntrada[puntero])
                    #print("Fin Op: "+self.token)
                    #**************************************************
                    finalLista = len(self.listaToken) #tamanio de la lista = posicion final
                    copiaListaToken = self.listaToken[self.inicioOperacion:finalLista] # creo una copia de la lista
                    #print(copiaListaToken)

                    operacionesSintactico = analizadoSintactico(copiaListaToken)
                    self.contador = operacionesSintactico.arranque()

                    #tamanio de la operacion
                    tamanioOperacion = finalLista - self.inicioOperacion
                    #print("FINAL LISTA---->"+str(finalLista))
                    #print("INICIO OPERACION---->"+str(self.inicioOperacion))
                    #print("TAMANIO OPERACION---->"+str(tamanioOperacion))
                    #print("RETURN---->"+str(self.contador))
                    

                    #verifico si se analizo toda la cadena
                    if self.contador == tamanioOperacion:
                        print("OPERACION: "+self.operacion+"  CORRECTA")
                    else:
                        print("OPERACION: "+self.operacion+"  INCORRECTA")

                    #cambio el inicio desde donde empiez la operacion
                    self.inicioOperacion = len(self.listaToken)

                    #***************************************************
                    # se cumple el final de una operacion
                    #self.addToken("tk_salto",self.token)
                    self.columna = 0
                    self.fila += 1
                    self.operacion = ""


                else:
                    #numero fila columna token
                    self.token += self.txtEntrada[puntero]
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    #self.addToken("ERROR",self.token)
                    print("Error lexico: "+self.token)  
                    self.numeroError += 1
                    self.columna += 1
                    self.token = ""

            
            #------------------------------------------------------------------
            # ESTADO PARA SIMBOLOS y/o ACEPTACION
            elif self.estado == 1:
                #self.addToken("Tk_operador",self.token)
                print("operador: "+self.token)
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
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                # si viene un punto en la cadena
                elif self.txtEntrada[puntero] == chr(46): # .
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]


                #aceptacion
                else:
                    # concatengo toda la operacion 
                    self.operacion += self.token
                    self.addToken("Tk_digito",self.token)
                    print("digito: "+self.token)
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
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                #ACEPTACION
                else:
                    #error en la cadena
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    #self.addToken("ERROR",self.token)
                    print("Error lexico: "+self.token)
                    #self.addToken(self.token)
                    #print("token: "+self.token)
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
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]


                #ACEPTACION
                else:
                    self.operacion += self.token
                    self.addToken("Tk_digito",self.token)
                    print("digito: "+self.token)
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
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                # si viene un numero
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                # si viene un guien bajo _
                elif self.txtEntrada[puntero]==chr(95):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5
                    # concatengo toda la operacion 
                    #self.operacion += self.txtEntrada[puntero]

                #ACEPTACION DE LA CADENA
                else:
                    self.operacion += self.token
                    self.addToken("Tk_id",self.token)
                    print("variable: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #muevo el puntero para el siguiente caracter
            #dentro del texto
            puntero += 1


        #retorno la lista de erroes si existieran
        return self.listaErrores





#*******************************************************************************
#   ESCRITURA DEL REPORTE DE ERRORES