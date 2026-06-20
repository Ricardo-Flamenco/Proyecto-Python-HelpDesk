import tkinter as tk
from tkinter import *
from register_tickets import register_ticket
from maker_dicts import tickets_frame_show

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

#imagen = PhotoImage(file="Proyecto-Python-HelpDesk/assets/home.png")
#label = tk.Label(screen,text="Home", image=imagen)
#label.pack(side="left")
#imagen.subsample(100, 100)

#ajustes = PhotoImage(file="Proyecto-Python-Helpdesk/assets/ajuste.png")
#label = tk.Label(screen, text="Ajustes", image=ajustes)


frame_izq = tk.Frame(screen, bg="#1E293B", width=200, height=300)
frame_izq.pack(side="left", fill="y")

frame_der = tk.Frame(screen, bg="White", width=400, height=100)
frame_der.pack(side="top", fill="x")

#importa los frames de las funciones
menu_frame_show, frame_show = tickets_frame_show(screen)
main_frame, _, _, _, = register_ticket(screen, frame_show)

#tkraise() levanta los frames encima de otros para hacer un cambio de menu
register = tk.Button(screen, text="Register", command=lambda:main_frame.tkraise())
register.place(relx=0, anchor="nw")

tickets_menu = tk.Button(screen, text="Home", command=lambda:menu_frame_show.tkraise())
tickets_menu.place(relx=0.1, anchor="ne")

screen.mainloop()