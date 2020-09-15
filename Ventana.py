import io
import os
import subprocess
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from parseJS.ParseJS import parseJS # analizador para javaScript
from parseCSS.analizadorCSS import analizadorcss # analizador para css
from parseOperaciones.analizadorOP import analizadorOperaciones # analizador lexico para operaciones
from parseOperaciones.analizadorSintactico import analizadoSintactico # analizador sintatico op
from parseHTML.AnalizadorHTML import AnalizadorHTML # analizador lexico del html


#-------------------------------------------------------------------
#saber que tipo de archivo fue el de apertura
tipoArchivo = ""
nombreArchivo = "" 
listaTokenRecibidos = []
save = ""

# METODO PARA GUARDAR SI SE EDITA ALGO EN EL ARCHIVO Y SE EDITA
#--------------------------------------------------------------------
def guardarArchivo():
    global save
    global areaTexto
    guardarArchivo = open(save,'w')
    guardarArchivo.write(areaTexto.get(1.0,END))

# METODO PARA BORRAR LO QUE HAY EN EL ARETE DE TEXTO PRINCIPAL
#---------------------------------------------------------------------
def remplazoTexto():
    global areaTexto
    areaTexto.delete("1.0",END+"-1c")
#---------------------------------------------------------------------

# METODO PARA PINTAR LAS PALABRAS 
#---------------------------------------------------------------------
def pintarTexto():
    global listaTokenRecibidos
    if len(listaTokenRecibidos) == 0:
        pass
    else:
        remplazoTexto()
        #configuracionColores()
        for fila in range(len(listaTokenRecibidos)):
            #print(listaTokenRecibidos[fila][0])
            #for columna in range(len(listaTokenRecibidos[fila])):
            if listaTokenRecibidos[fila][0] == "Tk_reservada":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_reservada")

            elif listaTokenRecibidos[fila][0] == "Tk_id":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_id")

            elif listaTokenRecibidos[fila][0] == "Tk_string":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_string")

            elif listaTokenRecibidos[fila][0] == "Tk_digito":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_digito")

            elif listaTokenRecibidos[fila][0] == "Tk_comentario":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_comentario")

            elif listaTokenRecibidos[fila][0] == "Tk_operador":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "Tk_operador")

            elif listaTokenRecibidos[fila][0] == "otro":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "otro")

            elif listaTokenRecibidos[fila][0] == "carrito":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "otro")

            elif listaTokenRecibidos[fila][0] == "error":
                areaTexto.insert(INSERT,listaTokenRecibidos[fila][1], "error")
        

# METODO PARA BORRAR LO DEL TEXT AREA
#--------------------------------------------------------------------
def new():
    global areaTexto
    global areaTextoErrore
    areaTexto.delete("1.0",END+"-1c")
    areaTextoErrore.delete("1.0",END+"-1c")

# METODO PARA APERTURA DE UN TEXTO PARA ANALIZAR
#----------------------------------------------------------------------
def openFile():    
    global areaTexto # are de texto principal
    global areaTextoErrore # area de texto de bitacora
    global tipoArchivo #tipo de archiov de apertura 
    global nombreArchivo #nombre del archivo de entrada
    global save # variable para la funcion de guardar archivo
    areaTexto.delete("1.0",END+"-1c")
    areaTextoErrore.delete("1.0",END+"-1c")
    filename = filedialog.askopenfilename(title="Busqueda",
    filetypes=(("HTML","*.html"),("JS","*.js"),("CSS","*.css"),("RMT","*.rmt")))  
    save = filename
    #****NOMBRE DEL ARCHIVO
    nombreArchivo = Path(filename).stem
    #  
    txt_file = open(""+filename,'r',encoding='utf-8')
    lectura = txt_file.read()
    areaTexto.insert(END,lectura)
    txt_file.close()
    archivoSeperado = filename.split(".")
    tipoArchivo = archivoSeperado[1]
    areaTextoErrore.insert(INSERT,"Archivo: "+tipoArchivo+"\n")
    #areaTextoErrore.insert(INSERT,"Nombre del archivo-> "+nombreArchivo)

    # PRUEBA DE CONTEO DE LINEA
    contadorLineas()

#pruebapara colo de texto para el pintado de las letras
#------------------------------------------------------------------------

def pruebaTexto():
    global areaTexto    
    areaTexto.tag_config("tk_id", foreground="#38DF43")
    areaTexto.tag_config("tk_operador", foreground="#4371CD")
    areaTexto.tag_config("tk_numero",foreground="#FF9A1B")
    areaTexto.insert(INSERT,"var1", "tk_id")
    areaTexto.insert(INSERT," ",)
    areaTexto.insert(INSERT,"=","tk_operador")
    areaTexto.insert(INSERT,"\n",)
    areaTexto.insert(INSERT,"5555","tk_numero")


# METODO PARA ANALIZAR LOS TEXTO CON CADA ANALIZADOR LEXICO
#------------------------------------------------------------------------
def analizar():    
    
    listadoBitacoraCSS = []
    listaErroresRecibidos = []
    textoCargado = "" 
    global areaTexto
    global areaTextoErrore
    global tipoArchivo
    global listaTokenRecibidos
    #--------
    textoCargado = areaTexto.get("0.0",END+"-1c")
    textoCargado = textoCargado + "\n"    
    #areaTextoErrore.insert(INSERT,textoCargado+"\n")
    if len(textoCargado) == 0:
        areaTextoErrore.delete("1.0",END+"-1c")
        areaTextoErrore.insert(INSERT,"texto vacio!!")
        messagebox.showinfo("ALERTA","No hay texto que analizar")
    else:        
        #borro si hay algo anteriro en el area de textoErrores
        areaTextoErrore.delete("1.0",END+"-1c") 
        #verifico el archivo Cargado
        #************************************
        #ARCHIVO JS
        if tipoArchivo == "js":
            analizadorjs = parseJS(textoCargado,nombreArchivo)       
            listaErroresRecibidos,listaTokenRecibidos = analizadorjs.automata()
        #************************************
        #ARCHIVO CSS
        elif tipoArchivo == "css":
            css = analizadorcss(textoCargado,nombreArchivo)
            listaErroresRecibidos,listadoBitacoraCSS,listaTokenRecibidos = css.automata()
        #************************************
        #ARCHIVO HTML
        elif tipoArchivo == "html":
            html = AnalizadorHTML(textoCargado,nombreArchivo)
            listaErroresRecibidos,listaTokenRecibidos = html.automata()
        #************************************
        #ARCHIVO RMT
        elif tipoArchivo == "rmt":
            operacones = analizadorOperaciones(textoCargado)            
            # multiple return = erroes lexicos y los token aceptados
            listaErroresRecibidos,listaTokenRecibidos = operacones.automata()
            #envio y analisis sintactico
            #operacionesSintactico = analizadoSintactico(listaTokenRecibidos)
            #operacionesSintactico.arranque()
        


        #imprimo si tengo errore encontrados
        #---------------------------------------
        #recorrido de la lista
        if len(listaErroresRecibidos) == 0:
            areaTextoErrore.insert(INSERT,"No hay Errores lexico!!!")

            #***********************************************
            #recorrido de la bitacora de css
            if len(listadoBitacoraCSS) == 0:
                pass
            else:
                areaTextoErrore.insert(INSERT,"\n")
                areaTextoErrore.insert(INSERT,"*******************************\n")
                areaTextoErrore.insert(INSERT,"**RECORRIDOS EN EL AUTOMATA CSS**\n")
                for filaBitacora in range(len(listadoBitacoraCSS)):
                    areaTextoErrore.insert(INSERT,""+listadoBitacoraCSS[filaBitacora]+"\n")

            #CREACION DEL ARCHIVO PARA EL REPORTE DE ERRORES
            archivo = open("ReporteHTML\\ReporteErrores.html","w")
            archivo.write("<html>\n")
            archivo.write("<head>\n")
            archivo.write("<title>  !Reporte de Errores Lexicos!  </title>\n")
            archivo.write("<link rel=\"stylesheet\" href=\"style.css\" >\n")
            archivo.write("</head>")
            #*********TITULO***************
            archivo.write("<h1> NO SE ECONTRARON ERROES LEXICOS </h1>\n")
            #creacion del la tabla con los errores
            archivo.write("<body>\n")
            archivo.write("</body>\n")
            archivo.write("</head>\n")
            archivo.write("</html>\n")
            archivo.close()




        #IMPRESION DE ERRORE EN EL SGUNDO TXTBOX
        else:
            areaTextoErrore.delete("1.0",END+"-1c")
            areaTextoErrore.insert(INSERT,"Errores lexicos Encontrados!!!\n")

            #*********************************************
            #recorrido de la lista de errores de css
            for fila in range(len(listaErroresRecibidos)):
                areaTextoErrore.insert(INSERT,"No. "+listaErroresRecibidos[fila][0])
                areaTextoErrore.insert(INSERT,"  Fila: "+listaErroresRecibidos[fila][1])
                areaTextoErrore.insert(INSERT,"  Columna "+listaErroresRecibidos[fila][2])
                areaTextoErrore.insert(INSERT,"  Error: "+listaErroresRecibidos[fila][3])
                areaTextoErrore.insert(INSERT,"\n")

            #***********************************************
            #recorrido de la bitacora de css
            if len(listadoBitacoraCSS) == 0:
                pass
            else:
                areaTextoErrore.insert(INSERT,"\n")
                areaTextoErrore.insert(INSERT,"*******************************\n")
                areaTextoErrore.insert(INSERT,"**RECORRIDOS EN EL AUTOMATA CSS**\n")
                for filaBitacora in range(len(listadoBitacoraCSS)):
                    areaTextoErrore.insert(INSERT,""+listadoBitacoraCSS[filaBitacora]+"\n")



            #CREACION DEL ARCHIVO PARA EL REPORTE DE ERRORES
            archivo = open("ReporteHTML\\ReporteErrores.html","w")
            archivo.write("<html>\n")
            archivo.write("<head>\n")
            archivo.write("<meta charset=\"UTF-8\" >\n")
            archivo.write("<title>  !Reporte de Errores Lexicos!  </title>\n")
            archivo.write("<link rel=\"stylesheet\" href=\"style.css\" >\n")
            archivo.write("</head>")
            archivo.write("<body>\n")
            #*********TITULO***************
            archivo.write("<h1> TABLA DE ERROERS LEXICOS </h1>\n")
            #creacion del la tabla con los errores
            archivo.write("<table border=\"1\">\n")
            archivo.write("<thead>")
            archivo.write("<td>")
            archivo.write("No.")
            archivo.write("</td>")
            archivo.write("<td>")
            archivo.write("Fila")
            archivo.write("</td>")
            archivo.write("<td>")
            archivo.write("Columna")
            archivo.write("</td>")
            archivo.write("<td>")
            archivo.write("Error")
            archivo.write("</td>")
            archivo.write("</thead>\n")
            
            #ELEMENTOS DE LA TABLA
            for fila in range(len(listaErroresRecibidos)):
                archivo.write("<tr>\n")   
                for columna in range(len(listaErroresRecibidos[fila])):
                    archivo.write("<td>")
                    archivo.write(""+listaErroresRecibidos[fila][columna])
                    archivo.write("</td>\n")

                archivo.write("</tr>\n")
            #*****************************

            archivo.write("</table>\n")
            #--------------------------------------
            archivo.write("</body>\n")
            archivo.write("</head>\n")
            archivo.write("</html>\n")
            archivo.close()

    #PINTADO DESPUES DE ANALIZAR
    pintarTexto()
#-------------------------------------------------------------------------

#------------------------------------------------------------------------
def contadorLineas():
    global LineasTexto
    global areaTexto
    LineasTexto.delete("1.0",END+"-1c")
    total = int(areaTexto.index(END).split('.')[0])
    print(total)
    i = 0
    while i < total:
        #print(i)
        LineasTexto.insert(INSERT,str(i)+"\n")
        i += 1
#------------------------------------------------------------------------

# APERTURA DE REPORTE HMTL
#--------------------------------------------------------------------------
def reporteHtml():
    comandoApertura ='ReporteHTML\\ReporteErrores.html'
    subprocess.Popen(comandoApertura,shell=True)
#--------------------------------------------------------------------------


# APERTURA DE REPORTE GRAPHVIZ
#--------------------------------------------------------------------------
def reporteAutomata():
    comandoApertura ='ReporteGrafico\\automataJS.png'
    subprocess.Popen(comandoApertura,shell=True)
#--------------------------------------------------------------------------


# METODO PARA ABRIR EL REPORTE DE OPERACIONES
#---------------------------------------------------------------------------
def reporteOperacion():
    comandoApertura ='ReporteHTML\\Operaciones.html'
    subprocess.Popen(comandoApertura,shell=True)


# METODO PARA EL SCROLL
#---------------------------------------------------------------------------
def scroll(x, y):
    global areaTexto
    global LineasTexto
    areaTexto.yview(x,y)
    LineasTexto.yview(x,y)

#---------------------------------------------------------------------------

# creacion de la raiz
raiz=Tk()
raiz.config(background="#282a36") 
#self.elementoVentana()
#self.ComponentesEditor()
# siempre al final

# titulo de la ventana
raiz.title("Proyecto 1 OLC1")

# tamanio de la ventana
raiz.geometry("900x660+100+0")


# recibe width height
raiz.resizable(0,0)

# que se contraiga o se expanda los elementos de la columna 2

#raiz.columnconfigure(0, weight=1)
raiz.columnconfigure(1,weight=2)

# menubar
menubar = Menu(raiz)
raiz.config(menu=menubar)
nuevomenu = Menu(menubar, tearoff=0)
abrirmenu = Menu(menubar, tearoff=0)
guardarmenu = Menu(menubar, tearoff=0)
guardarComomenu = Menu(menubar, tearoff=0)
ejecutarmenu = Menu(menubar, tearoff=0)
fileReporte = Menu(menubar)


menubar.add_cascade(label="Nuevo", command=new)
menubar.add_cascade(label="Abrir",  command = openFile)
menubar.add_cascade(label="Guardar", command = guardarArchivo)
menubar.add_cascade(label="Guardar Como", menu=guardarComomenu)
menubar.add_cascade(label="Ejecutar", command=analizar)
menubar.add_cascade(label="Reportes",menu=fileReporte)
fileReporte.add_cascade(label="Reporte HTML", command=reporteHtml)
fileReporte.add_cascade(label="Reporte Graphviz",command=reporteAutomata)
fileReporte.add_cascade(label="Reporte Operaciones",command=reporteOperacion)
menubar.add_cascade(label="Salir", command=raiz.quit)



#--------------------------------------------------
# segundo scrollbar para texto 
#scrooll bar
scrollbarY = Scrollbar(raiz, orient=VERTICAL)
scrollbarY.grid(row=0,column=2,sticky="ns")

#-------------------------------------------------
LineasTexto = Text(raiz)  
LineasTexto.config(width=3,height=20,font=("Comic Sans MS",14),background="#282a36",fg='White')
LineasTexto.grid(row=0,column=0,sticky="ns")
#listaNumeros =Listbox(raiz)
#listaNumeros.config(width=3,height=20,font=("Consolas",11),borderwidth=1,background="#282a36",fg='White')
#listaNumeros.grid(row=0,column=0,sticky="ns")
# list box para mostrar las filas
#listaBox = Listbox(raiz)
#listaBox.pack()
#listaBox.config(width=3,font=("Consolas",13),borderwidth=0,background="#282a36",fg='Black')
# posicion y que se expanda de alto
#listaBox.grid(row=0,column=0,sticky="ns")



#scrollbarX = Scrollbar(raiz, orient=HORIZONTAL)
#scrollbarX.grid(row=1,column=1,sticky="ew")



# area de texto para mostar el texto a analizar
# 282a36
areaTexto = Text(raiz)        
areaTexto.config(height=20, width = 10,
font=("Comic Sans MS",14),borderwidth=0,background="#282a36",fg='White',selectbackground="#779ECB"
,insertbackground='white',wrap="none")
# posicion en la matriz y que se expanda en los cuatro puntos cardinales
areaTexto.grid(row=0,column=1,sticky="ew")

#config del funcion scrooll
LineasTexto.config(yscrollcommand=scrollbarY.set)
areaTexto.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=scroll)


scrollbarX = Scrollbar(raiz,orient=HORIZONTAL)
scrollbarX.grid(row=1,column=1,sticky="ew")
scrollbarX.config(command=areaTexto.xview)
areaTexto.config(xscrollcommand=scrollbarX.set)

#*******************************************
#colores predeterminados para el area de texto
areaTexto.tag_config("Tk_reservada", foreground="#F80047")#palabras reservadas
areaTexto.tag_config("Tk_id", foreground="#00E656")#variables
areaTexto.tag_config("Tk_string", foreground="#FFFC00")#string y char
areaTexto.tag_config("Tk_digito", foreground="#25CCF7")#enteros y boolean
areaTexto.tag_config("Tk_comentario", foreground="#747d8c")#comentarios
areaTexto.tag_config("Tk_operador", foreground="#FFA700")#operadores
areaTexto.tag_config("otro",foreground="#c8d6e5")#otros
areaTexto.tag_config("error", background="red", foreground="white")


# separador
#-----------------------------------------------
areaTextoErrore = Text(raiz)
areaTextoErrore.config(height=10)
areaTextoErrore.grid(row=2,column=1,sticky="ew")

scrollbarErrorY = Scrollbar(raiz, orient=VERTICAL,bg="#282a36", troughcolor="steel blue")
scrollbarErrorY.grid(row=2,column=2,sticky="ns")

#
areaTextoErrore.config(yscrollcommand=scrollbarErrorY.set,
font=("Consolas",13),borderwidth=1,background="#282a36",fg='White')

#pruebaTexto()

# bucle infinito
raiz.mainloop()



        
        