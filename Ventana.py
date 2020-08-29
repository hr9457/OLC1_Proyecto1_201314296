import io
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from parseJS.ParseJS import parseJS
from parseCSS.analizadorCSS import analizadorcss



tipoArchivo = ""

#--------------------------------------------------------------------
def new():
    global areaTexto
    global areaTextoErrore
    areaTexto.delete("1.0",END+"-1c")
    areaTextoErrore.delete("1.0",END+"-1c")

#----------------------------------------------------------------------
def openFile():    
    global areaTexto
    global areaTextoErrore
    global tipoArchivo
    areaTexto.delete("1.0",END+"-1c")
    areaTextoErrore.delete("1.0",END+"-1c")
    filename = filedialog.askopenfilename(title="Busqueda",
    filetypes=(("HTML","*.html"),("JS","*.js"),("CSS","*.css"),("RMT","*.rmt")))    
    txt_file = open(""+filename,'r',encoding='utf-8')
    lectura = txt_file.read()
    areaTexto.insert(END,lectura)
    txt_file.close()
    archivoSeperado = filename.split(".")
    tipoArchivo = archivoSeperado[1]
    areaTextoErrore.insert(INSERT,"Archivo: "+tipoArchivo)

#------------------------------------------------------------------------

def pruebaTexto():
    global areaTexto
    areaTexto.tag_config("print",foreground="blue")

#------------------------------------------------------------------------
def analizar():    
    
    listaErroresRecibidos = []
    textoCargado = "" 
    global areaTexto
    global areaTextoErrore
    global tipoArchivo
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
        if tipoArchivo == "js":
            analizadorjs = parseJS(textoCargado)       
            listaErroresRecibidos = analizadorjs.automata()
        elif tipoArchivo == "css":
            css = analizadorcss(textoCargado)
            listaErroresRecibidos = css.automata()
        elif tipoArchivo == "html":
            pass
        elif tipoArchivo == "rmt":
            pass
         
        #imprimo si tengo errore encontrados
        #---------------------------------------
        #recorrido de la lista
        if len(listaErroresRecibidos) == 0:
            areaTextoErrore.insert(INSERT,"No hay Errores lexico!!!")
        else:
            areaTextoErrore.delete("1.0",END+"-1c")
            areaTextoErrore.insert(INSERT,"Errores lexicos Encontrados!!!\n")
            elemento = 0
            for fila in listaErroresRecibidos:
                for elemento in fila:
                    areaTextoErrore.insert(INSERT,elemento)
                    #print(elemento)
                areaTextoErrore.insert(INSERT,"\n")
#-------------------------------------------------------------------------

#------------------------------------------------------------------------
def contadorLineas():
    global LineasTexto
    global areaTexto
    texto = areaTexto.get("0.0",END+"-1c")
    lineasTxt = len(texto.read())
    print(lineasTxt)
#------------------------------------------------------------------------




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
raiz.columnconfigure(1,weight=1)
#raiz.rowconfigure(1, weight=1)

# menubar
menubar = Menu(raiz)
raiz.config(menu=menubar)
nuevomenu = Menu(menubar, tearoff=0)
abrirmenu = Menu(menubar, tearoff=0)
guardarmenu = Menu(menubar, tearoff=0)
guardarComomenu = Menu(menubar, tearoff=0)
ejecutarmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Nuevo", command=new)
menubar.add_cascade(label="Abrir",  command = openFile)
menubar.add_cascade(label="Guardar")
menubar.add_cascade(label="Guardar Como", menu=guardarComomenu)
menubar.add_cascade(label="Ejecutar", command=analizar)
menubar.add_cascade(label="Salir", command=raiz.quit)


#-------------------------------------------------
LineasTexto = Text(raiz)  
LineasTexto.config(width=3,height=20,font=("Consolas",13),borderwidth=1,background="#282a36",fg='White')
LineasTexto.grid(row=0,column=0)
# list box para mostrar las filas
#listaBox = Listbox(raiz)
#listaBox.pack()
#listaBox.config(width=3,font=("Consolas",13),borderwidth=0,background="#282a36",fg='Black')
# posicion y que se expanda de alto
#listaBox.grid(row=0,column=0,sticky="ns")


#scrooll bar
scrollbar = Scrollbar(raiz, orient=VERTICAL)
scrollbar.grid(row=0,column=2,sticky="ns")

#--------------------------------------------------
# segundo scrollbar para texto 
scrollbarX = Scrollbar(raiz, orient=HORIZONTAL)
scrollbarX.grid(row=1,column=1,sticky="ew")


# area de texto para mostar el texto a analizar
areaTexto = Text(raiz)        
areaTexto.config(height=20,xscrollcommand=scrollbarX.set,yscrollcommand=scrollbar.set,
font=("Consolas",13),borderwidth=0,background="#282a36",fg='White',selectbackground="#779ECB"
,insertbackground='white')
# posicion en la matriz y que se expanda en los cuatro puntos cardinales
areaTexto.grid(row=0,column=1,sticky="ew")

#config del funcion scrooll
scrollbarX.config(command=areaTexto.xview)
scrollbar.config(command=areaTexto.yview)


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


# bucle infinito
raiz.mainloop()



        
        