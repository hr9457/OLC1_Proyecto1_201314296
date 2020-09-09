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
        self.etiqueta =  ""
        self.cierreEtiqueta = ""
        self.listaErrores = []
        self.listaToken = []
        self.palabrasReservadas = ["html","head","title","body","h1","h2","h3","h4","h5","h6",
        "p","br","img","src","a","href","ul","li","p","style","table","border","caption","tr",
        "td","table","colgroup","col","thed","tbody","tfoot"]


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


    # movimiento del carrito en el texto
    def isMoveInsert(self,caracter):
        if (caracter == " "
        or caracter == "\t"
        or caracter == "\r"):
            return True

        elif caracter == "\n":
            self.fila += 1
            self.columna = 0
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

        #puntero para recorrer caracter por caracter la cadena
        puntero = 0

        #ciclo hacer para recoorrer todo la cadena de texto
        while puntero < len(self.txtEntrada):



            #ESTADO 0 
            # ESTADO DE INICIO DEL AUTOMA
            if self.estado == 0:

                # apertura de comentario | etiqueta 
                if self.txtEntrada[puntero] == chr(60): # <
                    self.token += self.txtEntrada[puntero]
                    self.estado = 1


                elif self.isMoveInsert(self.txtEntrada[puntero])==True:
                    pass


                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8





            #********************************************************************
            # APERTURA DE ETIQUETA
            elif self.estado == 1:
                #si viene una letra 
                if self.isLetter(self.txtEntrada[puntero])==True:
                    #acepto el token de <
                    self.addToken("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = ""                    
                    #paso al analizador interno de etiquetas
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                #si viene un signo  / para el cierre de etiqueta
                elif self.txtEntrada[puntero] == chr(47): # /
                    # aceptamos el token <
                    self.addToken("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = "" 
                    self.token += self.txtEntrada[puntero]
                    self.estado = 9


                # en caso contrario no es una etiqueta
                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8






            elif self.estado == 2:
                # si en la cadena viene una letra
                if self.isLetter(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2

                # si en la cadena viene un numero
                elif self.isNumber(self.txtEntrada[puntero])==True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                # si vie una cadena de texto dentro de la etiqueta
                elif self.txtEntrada[puntero] == chr(34): # ""
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""
                        
                    #********************************************
                    self.token += self.txtEntrada[puntero]
                    self.estado = 5




                # si viene un sigo de igualdad en la cadena
                elif self.txtEntrada[puntero]==chr(61): # =
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""
                        
                    #********************************************
                    self.token += self.txtEntrada[puntero]
                    self.estado = 4




                # si viene un moviento en puntero antes del cierre de la etiqueta
                elif self.isMoveInsert(self.txtEntrada[puntero])==True:
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""
                    else:
                        pass
                        
                    self.estado = 2



                # si en la cadena viene >
                elif self.txtEntrada[puntero]==chr(62):
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""

                    else:
                        pass

                        
                    #********************************************
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3



                #captura de errores dentro de las etiquetas
                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.txtEntrada[puntero])
                    print("ERROR LEXICO ETIQUETAS: "+self.txtEntrada[puntero])
                    self.numeroError += 1
                    self.columna += 1




            #*********************************************************************
            # CIERRE DE ETIQUETA
            elif self.estado == 3:
                self.addToken("Tk_operador",self.token)
                print("SIGNO : "+self.token)
                self.token = ""                    
                self.columna += 1
                self.estado = 0
                puntero -= 1                 



            elif self.estado == 4:
                self.addToken("Tk_operador",self.token)
                print("SIGNO : "+self.token)
                self.token = ""                    
                self.columna += 1
                self.estado = 2
                puntero -= 1  





            elif self.estado == 5:
                # si vienen unas comillas simples en la cadenas
                if self.txtEntrada[puntero] == chr(34): # ""
                    self.token += self.txtEntrada[puntero]
                    self.estado = 7
                
                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 6



            elif self.estado == 6:
                #acepto todo en la cadena mientras no vengan las commillas simples
                if self.txtEntrada[puntero] != chr(34): # ""
                    self.token += self.txtEntrada[puntero]
                    self.estado = 6

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 7



            #*************************************************************
            # aceptacion del string
            elif self.estado == 7:
                self.addToken("Tk_string",self.token)
                print("CADENA : "+self.token)
                self.token = "" 
                self.estado = 2
                puntero -= 1 




            #*****************************************************************
            # cadenas de texto en html
            elif self.estado == 8:
                # mientra sea diferente de < posible etiqueta
                if self.txtEntrada[puntero] != chr(60):
                    #si viene un salto de linea
                    if self.txtEntrada[puntero] == "\n":
                        self.fila += 1
                        self.columna = 0
                    #---------------------------    
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8

                # si viene una <LD
                elif (self.txtEntrada[puntero] == chr(60)
                and self.isLetter(self.txtEntrada[puntero+1])):
                    self.addToken("otro",self.token)
                    print("TEXTO: "+self.token)
                    self.token = ""
                    self.estado = 1
                    self.token+=self.txtEntrada[puntero]
                    #puntero -= 1


                # si viene una </
                elif (self.txtEntrada[puntero] == chr(60)
                and self.txtEntrada[puntero+1] == chr(47)):
                    self.addToken("otro",self.token)
                    print("TEXTO: "+self.token)
                    self.token = ""
                    self.estado = 1
                    self.token+=self.txtEntrada[puntero]
                    #puntero -= 1


                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 8






            #---------------------------------------------------------------
            # entrada para una etiqueta de cierre
            elif self.estado == 9:
                # si viene una lentra en la cadena
                if self.isLetter(self.txtEntrada[puntero])==True:
                    # aceptamos el token /
                    self.addToken("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = "" 
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10

                else:
                    pass




            elif self.estado == 10:
                # si viene una letra en la cadena
                if self.isLetter(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10


                # si viene una digito 
                elif self.isNumber(self.txtEntrada[puntero]) == True:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10


                # si viene una etiqueta de cierre >
                elif self.txtEntrada[puntero] == chr(62):
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""

                    else:
                        pass

                    self.token += self.txtEntrada[puntero]
                    self.estado = 11


                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.txtEntrada[puntero])
                    print("ERROR LEXICO ETIQUETA CIERRE: "+self.txtEntrada[puntero])
                    self.numeroError += 1
                    self.columna += 1




            #---------------------------------------------------------------
            # aceptacion para una etiqueta de cierre
            elif self.estado == 11:
                #aceptamos 
                self.addToken("Tk_operador",self.token)
                print("SIGNO : "+self.token)
                self.token = "" 
                self.estado = 0
                self.columna += 1
                puntero -= 1 



            elif self.estado == 12:
                pass


            elif self.estado == 13:
                pass


            elif self.estado == 14:
                pass


            elif self.estado == 15:
                pass


            elif self.estado == 16:
                pass


            elif self.estado == 17:
                pass


            elif self.estado == 18:
                pass




            #movimiento del puntero
            puntero += 1
            # fin del ciclo while


        return self.listaErrores
