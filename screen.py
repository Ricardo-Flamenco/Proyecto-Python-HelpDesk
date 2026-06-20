import tkinter as tk
from tkinter import *
from register_tickets import register_ticket
from maker_dicts import tickets_frame_show

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

home = PhotoImage(file="assets/house_solid.png")
home = home.subsample(36, 36)

ajustes = PhotoImage(file="assets/clipboard-list-solid.png")
ajustes = ajustes.subsample(10, 10)

frame_izq = tk.Frame(screen, bg="#1E293B", width=300, height=300)
frame_izq.pack(side="left", fill="y")

frame_der = tk.Frame(screen, bg="#30a862", width=400, height=100)
frame_der.pack(side="top", fill="x")

search_bar = tk.Entry(frame_der, bg="#ffffff", width=65, font=("Arial", 12))
search_bar.place(relx=0.5, y=30, anchor="center")

#importa los frames de las funciones
menu_frame_show, frame_show = tickets_frame_show(screen)
main_frame, _, _, _, = register_ticket(screen, frame_show)

#tkraise() levanta los frames encima de otros para hacer un cambio de menu
register = tk.Button(frame_izq, image=ajustes, bg="#1e293b", compound="left", text="Register", bd=0, command=lambda:main_frame.tkraise())
register.place(relx=0.5, y=150, anchor="center")

tickets_menu = tk.Button(frame_izq, image=home, bg="#1e293b", compound="left", text="Home", bd=0, command=lambda:menu_frame_show.tkraise())
tickets_menu.place(relx=0.5, y=50, anchor="center")

screen.mainloop()