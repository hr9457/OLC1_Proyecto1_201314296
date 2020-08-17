# anlizar para la parte del archivo en html
class AnalizadorHTML:
    
    # metodo contructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.estado = 0
        self.etiqueta = ""
        self.numeroError = 1
        self.fila = 0        
        self.columna = 0        
        self.caracter = ''
        self.listadoEtiquetas = ["<html>","</html>","<head>","</head>","<body>","</body>"
        ,"<h1>","</h1>","<h2>","</h2>","<h3>","</h3>","<h4>","</h4>","<h5>","</h5>","<h6>","</h6>"
        ,"<p>","</p>","<ul>","</ul>","<li>","</li>","<tr>","</tr>","<td>","</td>","<caption>","</caption>"
        ,"<colgroup>","</colgroup>","<col>","</col>","<thead>","</thead>","<tbody>","</tbody>"
        ,"<tfoot>","</tfoot>"]
        self.listadoErrores = []


    def automata(self):
        # guardo el tamanio de la cadena de entrada
        largoCadena = len(self.listadoToken)
        # para recorrer caracater por caracter la cadena 
        puntero = 0

        # leng da el tamanio del texto
        while indice < len(self.txtEntrada):  

            # estasdo 0 de simbolos
            # simbolos de etiquetas principales < / > 
            if self.estado == 0: 

                # revision para aceptacion de una etiqueta
                if (self.txtEntrada[puntero] == chr(60)
                and self.txtEntrada[puntero + 1] != ' ' ):

                    # concateno para la verificacion de la etiquetas
                    self.etiqueta = self.etiqueta + self.txtEntrada[puntero]
                    puntero += 1
                    self.estado = 1


                # verificiando la etiquetas de cierre
                elif self.txtEntrada[puntero] == chr(62):
                    
                    # concateno
                    self.etiqueta = self.etiqueta + self.txtEntrada[puntero]
                    
                    # busco si es etiqueta valida
                    if self.etiqueta in self.listadoEtiquetas:
                        pass
                    else:
                        self.listadoErrores.append([self.numeroError,self.fila,self.columna,self.etiqueta])

                    # paso al siguiente caracter
                    self.etiqueta = ""
                    puntero += 1


            # estado para letras 
            elif self.estado == 1:

                # verifico si es una letra en la cadena
                if ( (self.txtEntrada[puntero] >= chr(65) 
                and self.txtEntrada[puntero] <= chr(90))
                or (self.txtEntrada[puntero] >= chr(97)
                and self.txtEntrada[puntero] <= chr(122)) ):

                    # concateno para la verificion de etiquetas
                    self.etiqueta = self.etiqueta + self.txtEntrada[puntero]

                # numero en la cadena
                elif (self.txtEntrada[puntero] >= chr(48)
                and self.txtEntrada[puntero] <= chr(57)):

                    # paso al estado 2 de numeros
                    self.estado = 2 


                # moviento en el cursos 
                elif (self.txtEntrada[puntero] == ' ' 
                or self.txtEntrada[puntero] == '\n' 
                or self.txtEntrada[puntero] == '\t'):

                    # concateno en la etiqueta
                    self.etiqueta = self.etiqueta + self.txtEntradap[puntero]
                    puntero += 1


                # en caso contrario
                else:
                    self.estado = 0



            # estado para verificar numeros
            elif self.estado == 2:
                pass
                
