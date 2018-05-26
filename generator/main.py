from tkinter import *

def Cumprimente():
    hello.set("Olá, você!")

gui = Tk()

gui.title("Py5 - Python + Tkinter")
gui.geometry("400x300")

btn = Button(gui, text="Cumprimente", command=Cumprimente)
texto = Text(gui, width=30, height=1)
texto.pack()
btn.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()