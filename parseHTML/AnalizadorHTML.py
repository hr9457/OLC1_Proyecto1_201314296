import io
import os
import subprocess
import subprocess
from tkinter import messagebox
from tkinter import filedialog

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
        self.textoSalida = []


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

    # agregar texto y devolver
    def addTexto(self,lexema,token):
        self.textoSalida.append([lexema,token])





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

                # movientos en el cursos
                elif (self.txtEntrada[puntero] == ' '):
                    pass

                # tabulacion
                elif (self.txtEntrada[puntero] == '\t'
                or self.txtEntrada[puntero] == '\r'):
                    self.addToken("carrito","\t")
                    self.addTexto("carrito","\t")

                # salto de linea
                elif self.txtEntrada[puntero] == '\n':
                    self.addToken("carrito","\n")
                    self.addTexto("carrito","\n")
                    self.fila += 1
                    self.columna = 0
                    self.estado = 0


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
                    self.addTexto("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = ""                    
                    #paso al analizador interno de etiquetas
                    self.token += self.txtEntrada[puntero]
                    self.estado = 2


                #si viene un signo  / para el cierre de etiqueta
                elif self.txtEntrada[puntero] == chr(47): # /
                    # aceptamos el token <
                    self.addToken("Tk_operador",self.token)
                    self.addTexto("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = "" 
                    self.token += self.txtEntrada[puntero]
                    self.estado = 9


                # SI  VIENE UN SIGNO DE ADMIRACION ES UNA POSIBLE COMENTARIO
                elif self.txtEntrada[puntero] == chr(33): # !
                    self.token += self.txtEntrada[puntero]
                    self.estado = 12


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
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
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
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
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
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""
                    else:
                        pass
                    
                    self.addToken("carrito",self.txtEntrada[puntero])
                    self.addTexto("carrito",self.txtEntrada[puntero])
                    self.estado = 2



                # si en la cadena viene >
                elif self.txtEntrada[puntero]==chr(62):
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""

                    else:
                        pass

                        
                    #********************************************
                    self.token += self.txtEntrada[puntero]
                    self.estado = 3



                #captura de errores dentro de las etiquetas
                else:                    
                    if self.token != "":
                        #acepto la cadena
                        if self.token.lower() in self.palabrasReservadas:
                            self.addToken("Tk_reservada",self.token)
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""
                    else:
                        pass

                    self.errorLexico(self.numeroError,self.fila,self.columna,self.txtEntrada[puntero])
                    self.addTexto("error",self.txtEntrada[puntero])
                    print("ERROR LEXICO ETIQUETAS: "+self.txtEntrada[puntero])
                    self.numeroError += 1
                    self.columna += 1




            #*********************************************************************
            # CIERRE DE ETIQUETA
            elif self.estado == 3:
                self.addToken("Tk_operador",self.token)
                self.addTexto("Tk_operador",self.token)
                print("SIGNO : "+self.token)
                self.token = ""                    
                self.columna += 1
                self.estado = 0
                puntero -= 1                 



            elif self.estado == 4:
                self.addToken("Tk_operador",self.token)
                self.addTexto("Tk_operador",self.token)
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
                self.addTexto("Tk_string",self.token)
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
                    self.addTexto("otro",self.token)
                    print("TEXTO: "+self.token)
                    self.token = ""
                    self.estado = 1
                    self.token+=self.txtEntrada[puntero]
                    #puntero -= 1


                # si viene una </
                elif (self.txtEntrada[puntero] == chr(60)
                and self.txtEntrada[puntero+1] == chr(47)):
                    self.addToken("otro",self.token)
                    self.addTexto("otro",self.token)
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
                    self.addTexto("Tk_operador",self.token)
                    print("SIGNO: "+self.token)
                    self.token = "" 
                    self.token += self.txtEntrada[puntero]
                    self.estado = 10

                # que no venga un letra despues 
                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.txtEntrada[puntero])
                    self.addTexto("error",self.txtEntrada[puntero])
                    print("ERROR LEXICO ETIQUETA CIERRE: "+self.txtEntrada[puntero])
                    self.numeroError += 1
                    self.columna += 1




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
                            self.addTexto("Tk_reservada",self.token)
                            print("PALABRA RESERVADA : "+self.token)
                            self.token = ""                        
                        else:
                            self.addToken("Tk_id",self.token)
                            self.addTexto("Tk_id",self.token)
                            print("ID : "+self.token)
                            self.token = ""

                    else:
                        pass

                    self.token += self.txtEntrada[puntero]
                    self.estado = 11


                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.txtEntrada[puntero])
                    self.addTexto("error",self.txtEntrada[puntero])
                    print("ERROR LEXICO ETIQUETA CIERRE: "+self.txtEntrada[puntero])
                    self.numeroError += 1
                    self.columna += 1




            #---------------------------------------------------------------
            # aceptacion para una etiqueta de cierre
            elif self.estado == 11:
                #aceptamos 
                self.addToken("Tk_operador",self.token)
                self.addTexto("Tk_operador",self.token)
                print("SIGNO : "+self.token)
                self.token = "" 
                self.estado = 0
                self.columna += 1
                puntero -= 1 


            #--------------------------------------------------------------------
            # comentario html <!-- comentario
            elif self.estado == 12:
                # si viene un guion en el comentario
                if self.txtEntrada[puntero] == chr(45): # -
                    self.token += self.txtEntrada[puntero]
                    self.estado = 13

                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    self.addTexto("error",self.token)
                    print("ERROR LEXICO COMENTARIO: "+self.token)
                    self.token = ""
                    self.numeroError += 1
                    self.columna += 1
                    puntero -= 1
                    self.estado = 0



            elif self.estado == 13:
                # si viene un guien en el comentario
                if self.txtEntrada[puntero] == chr(45): # -
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14

                else:
                    self.errorLexico(self.numeroError,self.fila,self.columna,self.token)
                    self.addTexto("error",self.token)
                    print("ERROR LEXICO COMENTARIO: "+self.token)
                    self.token = "" 
                    self.numeroError += 1
                    self.columna += 1
                    puntero -= 1
                    self.estado = 0



            elif self.estado == 14:
                # concateno todo hasta que venga un guion 
                if self.txtEntrada[puntero] != chr(45): # -
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 15



            elif self.estado == 15:
                # si viene un guien en la cadena
                if self.txtEntrada[puntero] == chr(45):
                    self.token += self.txtEntrada[puntero]
                    self.estado = 16

                # si no viene otro guion en la cadena
                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14 # regreso al estado anterior tiene que cumplir el doble --
            


            elif self.estado == 16:
                # si viene un > para cierre de comentario
                if self.txtEntrada[puntero] == chr(62): # >
                    self.token += self.txtEntrada[puntero]
                    self.estado = 17

                else:
                    self.token += self.txtEntrada[puntero]
                    self.estado = 14




            #*********************************************************************
            # aceptacion para el comentario en html
            elif self.estado == 17:
                #aceptamos 
                self.addToken("Tk_comentario",self.token)
                self.addTexto("Tk_comentario",self.token)
                print("COMENTARIO : "+self.token)
                self.token = "" 
                self.estado = 0
                self.columna += 1
                puntero -= 1 




            #movimiento del puntero
            puntero += 1
            # fin del ciclo while




        #para la escritura del archivo html
        self.BusquedaRuta()
        # RETORNO UNA LISTA CON TODOS LOS ERRORES
        return self.listaErrores,self.textoSalida






    #*********************************************************************************************

    #escritura del archivo en limpio en la ruta entradas
    def destino(self,rutaWindows):
        #guardo la ruta 
        self.rutaSalida = rutaWindows
        print("---------->"+self.rutaSalida)
        separacionArchivo = self.rutaSalida.split("output") #separo por la palabra output
        print(""+separacionArchivo[1])

        CarpetasdelArchivo = ""+separacionArchivo[1] # solo  seleciono las carpetas a crear

        archivoSinCierre = CarpetasdelArchivo.split("-") # quito el cierre del comentario
        print(""+archivoSinCierre[0])

        carpetaDestino = 'salidaArchivos\\'+archivoSinCierre[0].rstrip()
        print("------>"+carpetaDestino)

        #verificacion de la existencias de de las rutas
        if os.path.isdir(carpetaDestino)==True:
            archivo = carpetaDestino + "\\"+self.nombreArchivo
            print("---->"+archivo)
            archivoSalidaJS = open(""+carpetaDestino+"\\"+self.nombreArchivo+".html","w")
            #********************************************************
            #ESCIRTURA PARA EL ARCHIVO DE SALIDA
            for fila in range(len(self.listaToken)):
                archivoSalidaJS.write(""+self.listaToken[fila][1])

            archivoSalidaJS.close()

        else:
            #metodo para la creacion de archivos
            os.makedirs(carpetaDestino)#metodo que crea carpetas
            archivoSalidaJS = open(""+carpetaDestino+"\\"+self.nombreArchivo+".html","w")
            #********************************************************
            #ESCIRTURA PARA EL ARCHIVO DE SALIDA
            for fila in range(len(self.listaToken)):
                archivoSalidaJS.write(""+self.listaToken[fila][1])

            archivoSalidaJS.close()



    #----------------------------------------------------------------------------------------------
    #metodo para la creacion de la carpet destino para el archivo de JS
    def BusquedaRuta(self):
        rutaWindows = ""
        # si el archivo no contiene nada analizado
        if len(self.listaToken) == 0:
            print("---->No hay elementos en la lista")

        # busqued de la ruta en las dos priemras lineas
        else:

            #buscar los primeros comentarios
            for fila in range(len(self.listaToken)):
                if self.listaToken[fila][0] == "Tk_comentario":
                    if self.listaToken[fila][1].find("PATHW") > -1:
                        rutaWindows = self.listaToken[fila][1]
                        self.destino(rutaWindows)
                        print("Ruta en la primera en la linea: ")
                        break

            # si no encuentra la ruta de salida para el archivo en limpio
            if rutaWindows == "":
                # por si no hay ruta de salida
                messagebox.showinfo("ALERTA","NO se econtro ruta de salida")
            '''
            #busqueda de la ruta en las dos primeras lineas
            if self.listaToken[0][1].find("PATHW") > -1:
                rutaWindows = self.listaToken[0][1]
                self.destino(rutaWindows)
                print("Ruta en la primera linea")

            # busqueda de la ruta en la segundo linea
            elif self.listaToken[2][1].find("PATHW") > -1:
                rutaWindows = self.listaToken[2][1]
                self.destino(rutaWindows)
                print("Ruta en la segunda linea")

            # por si no viene la ruta en el archivo
            else:
                pass
            '''
