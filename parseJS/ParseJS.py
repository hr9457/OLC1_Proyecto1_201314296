class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0 # estado actual del automa
        # element token error
        self.numError = 0 
        self.filaError = 0 # fila
        self.columnaError = 0 # columna
        self.token = "" # token
        self.listaErrores = [] # listado para los erroes

    # metodo para analizar token por token
    def automata(self):
        # puntero indica que parte de la cadena vamos
        puntero = 0

        # while mientras no hemos llegado al final de la cadena
        while puntero < len(self.txtEntrada):
            
            # estado 0 aceptacion de todos los simbolos aceptados por el lenguaje
            if self.estado == 0:
                
                # comentarios dentro de la cadena // o  /*
                if ( (self.txtEntrada[puntero] == chr(47) and self.txtEntrada[puntero + 1] == chr(47)) 
                or (self.txtEntrada[puntero] == chr(47) and self.txtEntrada[puntero + 1] == chr(42)) ):
                    self.estado = 3

                # letras en la cadena
                elif ( self.txtEntrada[puntero] >= chr(65) and self.txtEntrada[puntero] <= chr(90) 
                or (self.txtEntrada[puntero] >= chr(97) and self.txtEntrada[puntero] <= chr(122) ) ):
                    self.estado = 1

                # numeros en la cadena
                elif ( self.txtEntrada[puntreo] >= chr(48) and self.txtEntrada[puntero] <= chr(57) ):
                    self.estado = 2

                elif self.txtEntrada[puntero] == chr(61):
                    self.estado = 0

                else:
                    # agrego a la lista numero error,fila,columna,carcter
                    self.listaErrores.append([self.numError,self.filaError,self.columnaError,self.txtEntrada[puntero]])
                    self.numError += 1
                    puntero += 1


            # estado para letras 
            elif self.estado == 1:

                # letras en la cadena
                if ( self.txtEntrada[puntero] >= chr(65) and self.txtEntrada[puntero] <= chr(90) 
                or (self.txtEntrada[puntero] >= chr(97) and self.txtEntrada[puntero] <= chr(122) ) ): 
                    pass

                # verificar cuando se termine las letras de concatenar son los saltos

                # comentarios dentro de la cadena // o  /*
                elif ( (self.txtEntrada[puntero] == chr(47) and self.txtEntrada[puntero + 1] == chr(47)) 
                or (self.txtEntrada[puntero] == chr(47) and self.txtEntrada[puntero + 1] == chr(42)) ):
                    self.estado = 3

                # numeros en la cadena
                elif ( self.txtEntrada[puntreo] >= chr(48) and self.txtEntrada[puntero] <= chr(57) ):
                    self.estado = 2

                # si viene un carcter conocido estado 0

                # si comentario o texto estado 3

            # estado para verificacion de numeros
            elif self.estado == 2:
                # numeros en la cadena
                if ( self.txtEntrada[puntreo] >= chr(48) and self.txtEntrada[puntero] <= chr(57) ):
                    self.estado = 2


            # estado para verificacion de comentarios
            # y cadenas de texto
            elif self.estado == 3:
                
                # verficar si se termino el comentario multiple
                if (self.txtEntrada[puntero] != chr(42) 
                and self.txtEntrada[puntero + 1] != chr(47) ):
                    pass

            