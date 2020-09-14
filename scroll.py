import tkinter as tk

HEIGHT = 200
WIDTH = 300

def scroll(x, y):
    l_textbox.yview(x,y)
    m_textbox.yview(x,y)
    r_textbox.yview(x,y)

root = tk.Tk()

canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH, bg = "white")
canvas.pack()

frame = tk.Frame(root, bg ='white')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

scrollbar = tk.Scrollbar(frame)

l_label = tk.Label (frame, text = "Left")
l_label.place(relx=0, rely=0)

m_label = tk.Label (frame, text= "Middle")
m_label.place(relx=0.3, rely=0)

r_label = tk.Label (frame, text= "Right")
r_label.place(relx=0.6, rely=0)

l_textbox = tk.Text(frame, yscrollcommand = scrollbar.set)
l_textbox.config(font = ('Arial',9))
l_textbox.place(relx=0, rely=0.2,relwidth=0.3,relheight=0.8)

m_textbox = tk.Text(frame, yscrollcommand = scrollbar.set)
m_textbox.config(font = ('Arial',9))
m_textbox.place(relx=0.3, rely=0.2,relwidth=0.3,relheight=0.8)

r_textbox = tk.Text(frame, yscrollcommand = scrollbar.set)
r_textbox.config(font = ('Arial',9))
r_textbox.place(relx=0.6, rely=0.2,relwidth=0.3,relheight=0.8)

scrollbar.config( command = scroll)
scrollbar.place(relx = 0.9, relwidth = 0.1,relheight = 1)

for i in range(0, 100):
    l_textbox.insert(tk.INSERT, str(i)+"\n")
    m_textbox.insert(tk.INSERT, str(i)+"\n")
    r_textbox.insert(tk.INSERT, str(i)+"\n")
    l_textbox.place()
    m_textbox.place()
    r_textbox.place()

root.mainloop()