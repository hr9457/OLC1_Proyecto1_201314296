# anlizar para la parte del archivo en html
class AnalizadorHTML:
    
    # metodo contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.caracter = ''
        self.listadoToken = []

    def automata(self):
        # guardo el tamanio de la cadena de entrada
        largoCadena = len(self.listadoToken)
        # para recorrer caracater por caracter la cadena 
        indice = 0 
        # leng da el tamanio del texto
        while indice < len(self.txtEntrada):  

            # estasdo 0 de simbolos
            if self.estado == 0: 

                # comparacion con codigo ascii
                if (self.txtEntrada[indice] == chr(60) 
                or self.txtEntrada[inidice] == chr(47)):
                    self.listadoToken.append([self.txtEntrada[indice],"Tk_<"])

            # estado 1 de numeros
            elif self.estado == 1: 
                pass

            # estado 2 de letras
            elif self.estado == 2: 
                pass