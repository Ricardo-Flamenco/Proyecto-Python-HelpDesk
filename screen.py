import tkinter as tk
from tkinter import *
from registro import register_ticket
from maker_dicts import tickets_frame_show, show_tickets

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

register_ticket(screen)
tickets_frame_show(screen)

register = tk.Button(screen, text="Register")
register.pack()

tickets_menu = tk.Button(screen, text="Home")
tickets_menu.place(y=100)

screen.mainloop()