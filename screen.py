import tkinter as tk
from tkinter import *
from register_tickets import register_ticket
from ticket_make import tickets_frame_show
from update_state_menu import update_state_frame
from delete_ticket import delete_tickets_menu

screen = tk.Tk()
screen.title("HelpDesk")
screen.state("zoomed")

home = PhotoImage(file="assets/house-solid.png")
home = home.subsample(15, 15)

clipboard = PhotoImage(file="assets/clipboard-list-solid.png")
clipboard = clipboard.subsample(15, 15)

glass = PhotoImage(file="assets/magnifying-glass-solid.png")
glass = glass.subsample(25, 25)

pen = PhotoImage(file="assets/pen-to-square-solid.png")
pen = pen.subsample(15, 15)

trash_bin = PhotoImage(file="assets/trash-solid.png")
trash_bin = trash_bin.subsample(15, 15)

frame_izq = tk.Frame(screen, bg="#1E293B", width=300, height=300)
frame_izq.pack(side="left", fill="y")

frame_der = tk.Frame(screen, bg="#30a862", width=400, height=100)
frame_der.pack(side="top", fill="x")

#importa los frames de las funciones
menu_frame_show, frame_show = tickets_frame_show(screen)
menu_main_frame, _, _, _, = register_ticket(screen, frame_show)
menu_update_frame = update_state_frame(screen)
menu_delete_frame = delete_tickets_menu(screen)

#FRAME DER
search_bar = tk.Entry(frame_der, bg="#ffffff", width=45, font=("Arial", 13))
search_bar.place(relx=0.5, y=30, anchor="center")

glass_icon = tk.Label(frame_der, image=glass ,bg="#30a862")
glass_icon.place(relx=0.28, y=30, anchor="center")



#FRAME IZQ
#Buttons
active_button = 0

def activate_buttons(active):

    global active_button

    for button in menu_buttons:
        button.config(bg="#1e293b")

    active_button = active

    if active_button == 0:
        menu_buttons[0].config(bg="#10164E")
    elif active_button == 1:
        menu_buttons[1].config(bg="#10164e")
    elif active_button == 2:
        menu_buttons[2].config(bg="#10164e")
    elif active_button == 3:
        menu_buttons[3].config(bg="#10164e")

#tkraise() levanta los frames encima de otros para hacer un cambio de menu
tickets_menu = tk.Button(frame_izq, image=home, width=300, padx=10, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Home", font=("Arial", 15, "bold"), bd=0, command=lambda:(menu_frame_show.tkraise(), activate_buttons(0)))
tickets_menu.place(x=0, y=50, anchor="w")

register = tk.Button(frame_izq, image=clipboard, width=300, padx=10, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Register", font=("Arial", 15, "bold"), bd=0, command=lambda:(menu_main_frame.tkraise(), activate_buttons(1)))
register.place(x=0, y=120, anchor="w")

state = tk.Button(frame_izq, image=pen, width=300, padx=10, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Update state", font=("Arial", 15, "bold"), bd=0, command=lambda:(menu_update_frame.tkraise(), activate_buttons(2)))
state.place(x=0, y=190, anchor="w")

delete = tk.Button(frame_izq, image=trash_bin, width=300, padx=10, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Delete", font=("Arial", 15, "bold"), bd=0, command=lambda:(menu_delete_frame.tkraise(), activate_buttons(3)))
delete.place(x=0, y=260, anchor="w")

#lista que tiene todos los botones de menu
menu_buttons = [tickets_menu, register, state, delete]

screen.mainloop()