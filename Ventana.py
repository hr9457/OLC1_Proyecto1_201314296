from tkinter import *
from tkinter import ttk
from tkinter import filedialog



#----------------------------------------------------------------------
def openFile():
    global areaTexto
    filename = filedialog.askopenfilename(title="Busqueda",
    filetypes=(("HTML","*.html"),("JS","*.js"),("CSS","*.css")))
    txt_file = open(""+filename,'r',encoding='utf-8')
    lectura = txt_file.read()
    areaTexto.insert(END,lectura)
    txt_file.close()

#------------------------------------------------------------------------
# creacion de la raiz
raiz=Tk() 
#self.elementoVentana()
#self.ComponentesEditor()
# siempre al final

# titulo de la ventana
raiz.title("Proyecto 1 OLC1")

# tamanio de la ventana
raiz.geometry("1080x720+0+0")

# recibe width height
raiz.resizable(1,1)

# que se contraiga o se expanda los elementos de la columna 2
raiz.columnconfigure(1,weight=1)

# menubar
menubar = Menu(raiz)
raiz.config(menu=menubar)
nuevomenu = Menu(menubar, tearoff=0)
abrirmenu = Menu(menubar, tearoff=0)
guardarmenu = Menu(menubar, tearoff=0)
guardarComomenu = Menu(menubar, tearoff=0)
ejecutarmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Nuevo", menu=nuevomenu)
menubar.add_cascade(label="Abrir",  command = openFile)
menubar.add_cascade(label="Guardar", menu=guardarmenu)
menubar.add_cascade(label="Guardar Como", menu=guardarComomenu)
menubar.add_cascade(label="Ejecutar", menu=ejecutarmenu)
menubar.add_cascade(label="Salir", command=raiz.quit)

# list box para mostrar las filas
listaBox = Listbox(raiz)
listaBox.pack()
listaBox.config(width=3,font=("Consolas",13),borderwidth=2,background="#C1C2C4",fg='Black')
# posicion y que se expanda de alto
listaBox.grid(row=0,column=0,sticky="ns")

#scrooll bar
scrollbar = Scrollbar(raiz, orient=VERTICAL)
scrollbar.grid(row=0,column=2,sticky="ns")

# area de texto para mostar el texto a analizar
areaTexto = Text(raiz)        
areaTexto.config(yscrollcommand=scrollbar.set,font=("Consolas",13),borderwidth=3,background="#4C5658",fg='White')
# posicion en la matriz y que se expanda en los cuatro puntos cardinales
areaTexto.grid(row=0,column=1,sticky="nsew")

#config del funcion scrooll
scrollbar.config(command=areaTexto.yview)

# separador
labelSeparador = Label(raiz)
labelSeparador.grid(row=1,column=1)

#areta de texto para mostar la salida de los errores lexicos
areaTextoErrores = Text(raiz)
areaTextoErrores.config(font=("Consolas",15,"bold"),borderwidth=3,background="#4C5658",fg='White')
# poscion en la matriz y que se expanda en los cuatros puntos cardinales
areaTextoErrores.grid(row=2,column=1,sticky="nsew")

# separador
labelSeparador2 = Label(raiz)
labelSeparador2.grid(row=3,column=1)

# bucle infinito
raiz.mainloop()



        
        