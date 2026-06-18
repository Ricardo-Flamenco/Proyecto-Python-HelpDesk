import tkinter as tk
from tkinter import *

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

imagen = PhotoImage(file="Proyecto-Python-HelpDesk/assets/home.png")
label = tk.Label(screen, text="HOLA SICI SOS EL G.O.A.T", image=imagen)
label.pack()

screen.mainloop()