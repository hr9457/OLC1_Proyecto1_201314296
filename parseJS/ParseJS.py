class parseJS:

    # metodo constructor
    def __init__(self,txtEntrada):
        self.txtEntrada = txtEntrada
        self.numError = 0
        self.filaError = 0
        self.columnaError = 0
        self.token = ""
        self.listaErrores = []

    # metodo para analizar token por token
    def automata(self):
        pass