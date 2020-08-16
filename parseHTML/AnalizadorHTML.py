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
            # simbolos de etiquetas principales < / > 
            if self.estado == 0: 

                # comparacion con codigo ascii 60 = <
                # si el siguiente char diferente de espacio en blanco es tiqueta
                if (self.txtEntrada[indice] == chr(60)
                and self.txtEntrada[indice + 1] != ' '):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_<"])
                    indice += 1

                # espacio en blanco despues no es etiqueta es texto
                elif (self.txtEntrada[indice] == chr(60)
                and self.txtEntrada[indice + 1] == ' '):
                    self.estado = 2 # paso al estado 2 para concatenar todo lo que viene


                # 47 = /
                elif self.txtEntrada[indice] == chr(47):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_/"])
                    indice += 1

                # 62 = >
                # cierre etiqueta y busco si existe
                elif self.txtEntrada[indice] == chr(62):
                    # self.listadoToken.append([self.txtEntrada[indice],"Tk_>"])
                    indice += 1

                # si el caracter es una letra
                elif (self.txtEntrada[indice].isalpha()
                or self.txtEntrada[indice].isnumeric()):
                    indice += 1

                # errores lexicos dentro de etiquetas
                else:
                    self.listadoErroresLexico.append([self.numeroError,self.fila,
                    self.columna,self.txtEntrada[indice]])
                    self.numeroError += 1
                    indice += 1
                    

                

            # estado 1 de numeros
            elif self.estado == 1: 
                
                pass


            # estado 2 textos 
            elif self.estado == 2: 
                
                # es una etiqueta 
                if (self.txtEntrada[indice] == chr(60)
                and self.txtEntrada[indice + 1] != ' '):
                    self.estado = 0 # regreso al estado de etiquetas

                # no es una etiqueta es un texto para algo
                else:
                    pass
