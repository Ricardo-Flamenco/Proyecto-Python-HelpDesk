import tkinter as tk
from tkinter import *
from registro import register_ticket
from maker_dicts import tickets_frame_show

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

frame_show = tickets_frame_show(screen)
main_frame, _, _, _, = register_ticket(screen, frame_show)

register = tk.Button(screen, text="Register", command=lambda:main_frame.tkraise())
register.place(relx=0, anchor="nw")

tickets_menu = tk.Button(screen, text="Home", command=lambda:frame_show.tkraise())
tickets_menu.place(relx=0.1, anchor="ne")

screen.mainloop()