class analizadorcss:
    
    #contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.numeroError = 1
        self.fila = 0
        self.columna = 0
        self.token = ""
        self.listaErrores = []
        self.listaToken = []
        self.palabrasReservadas = ["color","border","text-align","font-weight","padding-left",
        "line-height","margin-top","margin-left","display","top","float","min-width",
        "background-color","Opacity","font-family","font-sieze","padding-right","padding",
        "width","margin-right","margin","position","right","clear","max-height","background-image",
        "background","font-style","font","padding-botton","display","height","margin-bottom","border-style",
        "bottom","left","max-width","min-height","absolute","center","after","before","hover","url","content","rgba"]

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
        if(caracter == chr(37) # %
        or caracter == chr(40) # (
        or caracter == chr(41) # )
        or caracter == chr(42) # *
        or caracter == chr(44) # ,
        or caracter == chr(45) # -
        or caracter == chr(46) # .
        or caracter == chr(58) # :
        or caracter == chr(59) # ;
        or caracter == chr(123) # {
        or caracter == chr(125)): # }
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


    #automata
    def automata(self):
        #puntero para saber parte del texto
        puntero = 0

        #recorrido de la cadena con un while
        #recorrido hasta que no llegue al final de la cadena
        while puntero < len(self.txtEntrada):
            
            #---------------------------------------------------------------------
            #ESTADO INCIAL ESTADO 0
            #ESTADO CERO
            if self.estado == 0:
                
                #si viene un simbolo en la cadena
                if self.isSymbol(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1 # pasa al estado 1

                
                #si viene un letra en la cadena
                elif self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                #si viene un numero en la cadena
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3


                #si viene el simbolo " posible string
                elif self.txtEntrada[puntero] == chr(34): # "
                    self.token += self.txtEntrada[puntero]
                    self.estado = 6


                # si viene un #
                elif self.txtEntrada[puntero] == chr(35):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 9
                

                # si viene un /
                elif self.txtEntrada[puntero] == chr(47):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 11


                # si viene un espacio en blanco
                elif self.txtEntrada[puntero] == " ":
                    self.addToken("carrito"," ")
                    self.columna += 1  


                # si viene un tabulacion o un retorno de carro
                elif (self.txtEntrada[puntero] == "\t"
                or self.txtEntrada[puntero] == "\r"):
                    self.addToken("carrito","\t")

                    
                # si vien un salto de linea
                elif self.txtEntrada[puntero] == "\n":
                    self.addToken("carrito","\n")
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




            #-------------------------------------------------------------
            #ESTADOS DE SIMBOLO ACEPTACION
            elif self.estado == 1:
                self.addToken("Tk_operador",self.token)
                print("Token: "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0
                puntero -= 1


            #--------------------------------------------------------------
            #ESTADO PARA LETRAS Y ACEPTACION
            elif self.estado == 2:
                #reviso si viene una letra 
                if self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2 # pasa al estado 1

                #reviso si viene un numero
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2

                # si vien un guien en la cadena
                elif self.txtEntrada[puntero] == chr(45): # -
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2

                #ACEPTACION
                else:
                    #busqueda en la palabras reservadas
                    if self.token in self.palabrasReservadas:
                        self.addToken("Tk_reservada",self.token)
                        print("RESERVADA :"+self.token)
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


            #-----------------------------------------------------------------
            #ESTADO PARA NUMEROS Y ACEPTACION
            elif self.estado == 3:
                #reviso si viene un numero 
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3

                #si viene un punto decimal
                elif self.txtEntrada[puntero] == chr(46): # .
                    self.token += self.txtEntrada[puntero]
                    self.estado = 4

                
                #ACEPTACION
                else:
                    self.addToken("Tk_digito",self.token)
                    print("Numero: "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1
                

            #punto decimal
            elif self.estado == 4:
                #si viene un digito
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                #ACEPTACION
                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    print("Error Lexico : "+self.token)
                    self.token = ""
                    self.numeroError += 1
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #----------------------------------------------------------------
            #Estado numero decimales y aceptacion
            elif self.estado == 5:
                #si viene un digito
                if self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5

                #ACEPTACION
                else:
                    self.addToken("Tk_digito",self.token)
                    print("NUMERO DECIMAL : "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1



            #----------------------------------------------------------------------
            #Estado para cadenas y/o aceptacion del simbolo "
            elif self.estado == 6:
                #si viene una comilla simple "
                #self.addToken(self.token)
                #print("Token: "+self.token)
                #self.token = ""
                #self.columna += 1
                if self.txtEntrada[puntero] == chr(34): # "
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 7


            elif self.estado == 7:
                #acepto todo lo que viene
                if self.txtEntrada[puntero] != chr(34): # ""
                    self.token += self.txtEntrada[puntero]
                    self.estado = 7

                #ACEPTACION
                else:
                    #impresion del token
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8
                    puntero -= 1

            
            #aceptacion del simbolo " cierre de un string
            elif self.estado == 8:
                # si viene comillas simples
                self.addToken("Tk_string",self.token)
                print("CADENA : "+self.token)
                self.token = ""  
                self.columna += 1
                self.estado = 0
                
            

            #-------------------------------------------------------------
            # si viene un identificad de un color
            elif self.estado == 9:
                #si viene letra o numero
                if (self.isLetter(self.txtEntrada[puntero])
                or self.isNumber(self.txtEntrada[puntero])):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10

                #aceptacion
                else:
                    self.addToken("Tk_operador",self.token)
                    print("OPERADOR : "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1


            #aceptacion de un id de un color y aceptacion
            elif self.estado == 10:
                #si viene letra o numero
                if (self.isLetter(self.txtEntrada[puntero])
                or self.isNumber(self.txtEntrada[puntero])):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10

                #aceptacion
                else:
                    self.addToken("Tk_id",self.token)
                    print("ID COLOR : "+self.token)
                    self.token = ""
                    self.columna += 1
                    self.estado = 0
                    puntero -= 1




            #---------------------------------------------------------------
            #comentarios
            elif self.estado == 11:
                # si viene un *
                if self.txtEntrada[puntero] == chr(42): # *
                    self.token += self.txtEntrada[puntero]
                    self.estado = 12

                #aceptacion
                else: # si no viene * erro para /
                    self.token += self.txtEntrada[puntero]
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    print("Error lexico: "+self.token)  
                    self.numeroError += 1
                    self.columna += 1
                    self.token = ""
                    self.estado = 0
                    puntero -= 1


            elif self.estado == 12:
                # si viene un es diferente *
                if self.txtEntrada[puntero] != chr(42):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 12

                else:# si viene un *
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13



            elif self.estado == 13:
                #mientras sea diferente a /
                if self.txtEntrada[puntero] != chr(47):
                    #self.token += self.txtEntrada[puntero]
                    puntero -= 1
                    self.estado = 12

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14


            elif self.estado == 14:
                #acepto el token
                self.addToken("Tk_comentario",self.token)
                print("Comentario : "+self.token)
                self.token = ""
                self.columna += 1
                self.estado = 0 
                puntero -= 1              




            #pasa al siguiente caracter
            #y sigue con ele while
            puntero += 1


        #termina el while y retorno
        #retorno los erros que si existieran
        return self.listaErrores
        #fin del metodo del automo




