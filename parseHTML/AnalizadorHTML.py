# anlizar para la parte del archivo en html
class AnalizadorHTML:
    
    # metodo contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.fila = 0
        self.token = ""
        self.columna = 0
        self.numeroError = 1
        self.caracter = ''
        self.listadoToken = []
        self.listadoErroresLexico = []

    def automata(self):
        # guardo el tamanio de la cadena de entrada
        largoCadena = len(self.listadoToken)
        # para recorrer caracater por caracter la cadena 
        indice = 0 
        # leng da el tamanio del texto
        while indice < len(self.txtEntrada):  

            # estasdo 0 de simbolos
            if self.estado == 0: 

                # comparacion con codigo ascii 60 = <
                if self.txtEntrada[indice] == chr(60):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_<"])
                    indice += 1

                # 47 = /
                elif self.txtEntrada[indice] == chr(47):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_/"])
                    indice += 1

                # 62 = >
                elif self.txtEntrada[indice] == chr(62):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_>"])
                    indice += 1

                # numero
                elif ((self.txtEntrada[indice] >= chr(48)) 
                and self.txtEntrada[indice] <= chr(57)):
                    self.estado = 1

                # rango entre la A and Z
                elif ((self.txtEntrada[indice] >= chr(65) 
                and self.txtEntrada[indice] <= chr(90))
                or (self.txtEntrada[indice] >= chr(97) 
                and self.txtEntrada[indice] <= chr(122))):
                    self.estado = 2

                

            # estado 1 de numeros
            elif self.estado == 1: 
                
                # verifico que se un numero lo que estoy viendo de caracter
                if ((self.txtEntrada[indice] >= chr(48)) 
                and self.txtEntrada[indice] <= chr(57)):
                    indice +=1

                # rango entre la A and Z
                elif ((self.txtEntrada[indice] >= chr(65) 
                and self.txtEntrada[indice] <= chr(90))
                or (self.txtEntrada[indice] >= chr(97) 
                and self.txtEntrada[indice] <= chr(122))):
                    self.estado = 2

                #  <  /  >
                elif (self.txtEntrada[indice] == chr(62)
                or self.txtEntrada[indice] == chr(60) 
                or self.txtEntrada[indice] == chr(47)):
                    #busco si es una palabra reservada
                    self.estado = 0  


            # estado 2 de letras
            elif self.estado == 2: 
                
                # comparacion cuando un caracter es un letra
                # rango entre la A and Z
                if ((self.txtEntrada[indice] >= chr(65) 
                and self.txtEntrada[indice] <= chr(90))
                or (self.txtEntrada[indice] >= chr(97) 
                and self.txtEntrada[indice] <= chr(122))):

                    # self.token = self.token + self.txtEntrada[indice]
                    indice += 1

                # <  /  >
                elif (self.txtEntrada[indice] == chr(62)
                or self.txtEntrada[indice] == chr(60) 
                or self.txtEntrada[indice] == chr(47)):
                    #busco si es una palabra reservada
                    self.estado = 0 


                # numero
                elif ((self.txtEntrada[indice] >= chr(48)) 
                and self.txtEntrada[indice] <= chr(57)):
                    self.estado = 1


                # manejo de error lexico
                # remplazo por un espacio en blanco
                else:
                    # mando al listado de erroes
                    self.listadoErroresLexico.append([self.numeroError,self.fila,self.columna,self.txtEntrada[indice]])
                    self.numeroError += 1
                    self.token = self.token + " "
                    indice += 1
                    pass