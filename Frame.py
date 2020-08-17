from tkinter import *

# creacion de la raiz
raiz=Tk()

# titulo de la ventana
raiz.title("Proyecto 1 OLC1")

# tamanio de la ventana
raiz.geometry("1080x720")

# recibe width height
raiz.resizable(1,1)

# menubar
menubar = Menu(raiz)
raiz.config(menu=menubar)
Nuevo = Menu(menubar, tearoff=0)
Abrir = Menu(menubar, tearoff=0)
Guardar = Menu(menubar, tearoff=0)
GuardarComo = Menu(menubar, tearoff=0)
EjecutarAnalisis = Menu(menubar, tearoff=0)
Salir = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Nuevo", menu=Nuevo)
menubar.add_cascade(label="Abrir", menu=Abrir)
menubar.add_cascade(label="Guardar", menu=Guardar)
menubar.add_cascade(label="Guardar Como", menu=GuardarComo)
menubar.add_cascade(label="Ejecutar", menu=EjecutarAnalisis)
menubar.add_cascade(label="Salir", menu=Salir)



# ---------------------------
# creacion del frame
frame = Frame()

# se pone el frame dentro de la ventana
frame.pack(fill="both", expand ="True")

# siempre al final
# bucle infinito
raiz.mainloop()

