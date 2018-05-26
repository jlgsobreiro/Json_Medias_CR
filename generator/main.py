from tkinter import *
from tkinter import ttk
import generator.randomHeroGenerator as hg

def Cumprimente():
    hello.set("Olá, você!")

gui = Tk()

gui.title("Py5 - Python + Tkinter")
gui.geometry("400x300")
texto = Text(gui, width=30, height=1)
texto.pack()
btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.pack()

lista = StringVar()
combo = ttk.Combobox(gui, textvariable=lista,text="Classes")
combo["values"] = hg.classeLista()
combo.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()