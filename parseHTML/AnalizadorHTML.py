# anlizar para la parte del archivo en html
class AnalizadorHTML:
    
    # metodo contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.token = ""
        self.numeroError = 1
        self.fila = 0        
        self.columna = 0        
        self.caracter = ''
        self.listadoEtiquetas = ["html"]
        self.listadoAtributos = ["src","href","style","border"]
        self.listadoErrores = []


    def automata(self):

        # guardo el tamanio de la cadena de entrada
        largoCadena = len(self.listadoToken)
        # para recorrer caracater por caracter la cadena 
        puntero = 0

        # leng da el tamanio del texto
        while indice < len(self.txtEntrada):  

            pass


    def letter(self,caracter):
        if ( (caracter >= chr(65) 
        and caracter <= chr(90))
        or caracter >= chr(97)
        and caracter <= chr(122)):
            return True

        else: 
            return False


    def Digit(self,caracter):
        if (caracter >= chr(48)
        and caracter <= chr(57)):
            return True

        else:
            return False



