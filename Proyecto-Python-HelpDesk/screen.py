import tkinter as tk
from tkinter import *

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

imagen = PhotoImage(file="Proyecto-Python-HelpDesk/assets/home.png")
label = tk.Label(screen,text="Home", image=imagen)
label.pack(side="left")
imagen.subsample(100, 100)

ajuste = PhotoImage(file="Proyecto-Python-Helpdesk/assets/ajuste.png")
frame_izq = tk.Frame(screen, bg="#1E293B", width=200, height=300)
frame_izq.pack(side="left", fill="y")

frame_der = tk.Frame(screen, bg="White", width=400, height=100)
frame_der.pack(side="top", fill="x")

screen.mainloop()