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
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", command=raiz.quit)



# ---------------------------
# creacion del frame
frame = Frame()

# se pone el frame dentro de la ventana
frame.pack(fill="both", expand ="True")

# siempre al final
# bucle infinito
raiz.mainloop()

