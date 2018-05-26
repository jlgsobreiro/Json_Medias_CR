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

listaClasse = StringVar()
comboClasse = ttk.Combobox(gui, textvariable=listaClasse,text="Classes")
comboClasse["values"] = hg.classeLista()
comboClasse.pack()

listaRaca = StringVar()
comboRaca = ttk.Combobox(gui, textvariable=listaRaca,text="Raca")
comboRaca["values"] = hg.racaLista()
comboRaca.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()