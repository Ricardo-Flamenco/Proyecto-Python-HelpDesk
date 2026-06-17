import tkinter as tk
from tkinter import *
from create_tickets import *

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

button = tk.Button(text="CREAR COSAS", command=lambda:(create(frame)))
button.pack()

frame = tk.Frame(screen, bg="#1A53CF")
frame.place(x=50, y=50, width=1000, height=1500)

screen.mainloop()