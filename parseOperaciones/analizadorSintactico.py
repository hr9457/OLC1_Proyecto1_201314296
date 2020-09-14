class analizadoSintactico:

    #contructor
    def __init__(self,listaToken):
        self.listaToken = listaToken
        self.token = listaToken[0][0]
        self.posicion = 0
        self.listaErrores = []
        self.contador = 1
        self.tokenAnterior = ""


    #-------------------------------------------------------------------------------
    def estadoError(self,tokenActual):
        if (tokenActual == "Tk_multipliacion"# *
        or tokenActual == "Tk_suma"# +
        or tokenActual == "Tk_resta"# - 
        or tokenActual == "Tk_division"
        or tokenActual == "Tk_apertura"):# /
            print("se esperaba un DIGITO")
            self.contador -= 1

    #--------------------------------------------------------------------------------
    #metodo de parea
    def match(self,preanalisis):
        if preanalisis != self.token:
            print("se esperaba: "+preanalisis)
            self.contador -= 1

        elif preanalisis == self.token:            
            print("*****"+self.token+"*****")

        if self.posicion < len(self.listaToken)-1:
            self.posicion += 1
            self.tokenAnterior = self.token
            self.token = self.listaToken[self.posicion][0]
            self.contador += 1 # aumento en uno las operaciones verificadas



    #arranque
    def arranque(self):
        #print(self.listaToken)
        self.operando1()
        return self.contador #retorno cuantas operaciones se verificaron en el sintactico

    #producciones
    # A -> BA'
    def operando1(self):  
        self.operando3()#B    
        self.operando2()#A'

    #A' -> +BA' | NADA
    def operando2(self):
        if self.token == "Tk_suma":
            self.match("Tk_suma")#+
            #print(" + ")
            self.operando3()#B
            self.operando2()#A'
        else:
            pass#NADA

    #B -> CB'
    def operando3(self):
        self.operando5()#C
        self.operando4()#B'

    #B' -> -CB' | NADA    
    def operando4(self):
        if self.token == "Tk_resta":
            self.match("Tk_resta")#+
            #print(" - ")
            self.operando5()#C
            self.operando4()#B'
        else:
            pass#NADA

    #C -> DC'    
    def operando5(self):
        self.operando7()#D
        self.operando6()#C'

    #C' -> *DC' | nada
    def operando6(self):
        if self.token == "Tk_multipliacion":
            self.match("Tk_multipliacion")#*
            #print(" * ")
            self.operando7()#D
            self.operando6()#C'
        else:
            pass#NADA

    #D -> ED'
    def operando7(self):
        self.operando9()#E
        self.operando8()#D'

    #D' -> /ED' | nada
    def operando8(self):
        if self.token == "Tk_division":
            self.match("Tk_division")#/
            #print(" / ")
            self.operando9()#E 
            self.operando8()#D'
        else:
            pass#NADA

    #E -> -G | G
    def operando9(self):
        if self.token == "Tk_resta":
            self.match("Tk_resta")#-
            #print(" - ")
            self.operando10()#G
        else:
            self.operando10()#G

    #G -> (A) | numero | variable 
    def operando10(self):
        if self.token == "Tk_apertura":
            self.match("Tk_apertura")
            #print(" ( ")
            self.operando1()#A
            self.match("Tk_cierre")
            #print(" ) ")

        elif self.token == "Tk_digito":
            self.match("Tk_digito")
            #print(" DIGITO ")

        elif self.token == "Tk_id":
            self.match("Tk_id")
            #print(" ID ")

        else:
            #self.match("ERROR")
            #self.posicion += 1
            self.estadoError(self.tokenAnterior)
