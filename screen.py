import tkinter as tk
from tkinter import *
from registro import register_ticket
from maker_dicts import tickets_show

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

def show_menu (menu):
    menu(screen)

register = tk.Button(screen, text="Register", command=(lambda:show_menu(register_ticket)))
register.pack()

tickets_menu = tk.Button(screen, text="Home", command=(lambda:show_menu(tickets_show)))
tickets_menu.place(y=100)

screen.mainloop()