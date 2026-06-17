import tkinter as tk
from tkinter import *
from registro import register_ticket

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

register_ticket(screen)

screen.mainloop()