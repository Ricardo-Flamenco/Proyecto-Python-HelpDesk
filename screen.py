import tkinter as tk
from tkinter import *

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

frame = tk.Frame(screen, bg="#1A53CF")
frame.place(x=50, y=50, width=1000, height=1500)

screen.mainloop()