import tkinter as tk
import customtkinter as ctk
import manager_json
from tkinter import *
from PIL import Image, ImageTk
from register_tickets import register_ticket
from ticket_make import tickets_frame_show
from update_state_menu import update_state_frame
from delete_ticket import delete_tickets_menu
from search_tickets import ticket_search_frame
from consultar_tickets import consult_tickets
from notifications import images_init

manager_json.cargar_tickets()

screen = tk.Tk()
screen.title("HelpTrack")
screen.state("zoomed")
screen.iconbitmap("assets/logo_helptrack.ico")

home = Image.open("assets/house-solid.ico")
home = home.resize((38, 38), Image.Resampling.LANCZOS)
home = ImageTk.PhotoImage(home)

logo = Image.open("assets/logotipo_helptrack.ico")
logo = logo.resize((180, 180), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(logo)

clipboard = Image.open("assets/clipboard-list-solid.ico")
clipboard = clipboard.resize((38, 38), Image.Resampling.LANCZOS)
clipboard = ImageTk.PhotoImage(clipboard)

glass = Image.open("assets/magnifying-glass-solid.ico")
glass = glass.resize((28, 28), Image.Resampling.LANCZOS)
glass = ImageTk.PhotoImage(glass)

glass_menu = Image.open("assets/magnifying-glass-solid-menu.ico")
glass_menu = glass_menu.resize((38, 38), Image.Resampling.LANCZOS)
glass_menu = ImageTk.PhotoImage(glass_menu)

pen = Image.open("assets/pen-to-square-solid.ico")
pen = pen.resize((38, 38), Image.Resampling.LANCZOS)
pen = ImageTk.PhotoImage(pen)

trash_bin = Image.open("assets/trash-solid.ico")
trash_bin = trash_bin.resize((38, 38), Image.Resampling.LANCZOS)
trash_bin = ImageTk.PhotoImage(trash_bin)

folder = Image.open("assets/folder-solid.ico")
folder = folder.resize((38, 38), Image.Resampling.LANCZOS)
folder = ImageTk.PhotoImage(folder)

x = Image.open("assets/x-solid.ico")
x = x.resize((20, 20), Image.Resampling.LANCZOS)
x = ImageTk.PhotoImage(x)

copy = Image.open("assets/copy-solid.ico")
copy = copy.resize((20, 20), Image.Resampling.LANCZOS)
copy = ImageTk.PhotoImage(copy)

frame_izq = tk.Frame(screen, bg="#1E293B", width=300)
frame_izq.pack(side="left", fill="y")

frame_der = ctk.CTkFrame(screen, fg_color="#121924", width=400, height=100, corner_radius=0)
frame_der.pack(side="top", fill="x")

#FRAME DER
search_bar = ctk.CTkEntry(frame_der, fg_color="#ffffff", text_color="#000000", placeholder_text="Enter a ticket ID", font=("Arial", 13), corner_radius=10, width=400)
search_bar.place(x=100, y=30, anchor="w")
glass_icon = tk.Label(frame_der, image=glass ,bg="#121924")
glass_icon.place(x=50, y=30, anchor="w")

search_information = tk.Label(frame_der, bg="#121924", text="Search tickets by ID", fg="#ffffff", font=("Arial", 13, "bold"))
search_information.place(x=520, y=30, anchor="w")

#Basic info
#importa los frames de las funciones
menu_frame_show, frame_show, canva_show = tickets_frame_show(screen)
menu_main_frame, _, _, _ = register_ticket(screen, frame_show, canva_show)
menu_update_frame = update_state_frame(screen)
menu_delete_frame = delete_tickets_menu(screen)
_, menu_search_frame = ticket_search_frame(screen, search_bar)
menu_consult_frame = consult_tickets(screen)
images_init()


#FRAME IZQ

logo_helptrack = tk.Label(frame_izq, bg="#1e293b", image=logo)
logo_helptrack.place(x=10, y=660, anchor="w")
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
    elif active_button == 4:
        menu_buttons[4].config(bg="#10164e")

#tkraise() levanta los frames encima de otros para hacer un cambio de menu
tickets_menu = tk.Button(frame_izq, image=home, width=300, padx=6, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Home", font=("Arial", 15, "bold"), bd=0, cursor="hand2", command=lambda:(menu_frame_show.tkraise(), activate_buttons(0), search_bar.configure(state="normal", fg_color="#ffffff")))
tickets_menu.place(x=0, y=50, anchor="w")

register = tk.Button(frame_izq, image=clipboard, width=300, padx=6, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Create a new ticket", font=("Arial", 15, "bold"), bd=0, cursor="hand2", command=lambda:(menu_main_frame.tkraise(), activate_buttons(1), search_bar.configure(state="normal", fg_color="#ffffff")))
register.place(x=0, y=120, anchor="w")

state = tk.Button(frame_izq, image=pen, width=300, padx=6, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Update state of a ticket", font=("Arial", 15, "bold"), bd=0, cursor="hand2", command=lambda:(menu_update_frame.tkraise(), activate_buttons(2), search_bar.configure(state="normal", fg_color="#ffffff")))
state.place(x=0, y=190, anchor="w")

delete = tk.Button(frame_izq, image=trash_bin, width=300, padx=6, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Delete a ticket", font=("Arial", 15, "bold"), bd=0, cursor="hand2", command=lambda:(menu_delete_frame.tkraise(), activate_buttons(3), search_bar.configure(state="normal", fg_color="#ffffff")))
delete.place(x=0, y=260, anchor="w")

consult = tk.Button(frame_izq, image=folder, width=300, padx=6, anchor="w", activebackground="#1e293b", bg="#1e293b", fg="#ffffff", compound="left", text="Consult tickets", font=("Arial", 15, "bold"), bd=0, cursor="hand2", command=lambda:(menu_consult_frame.tkraise(), activate_buttons(4), search_bar.configure(state="normal", fg_color="#ffffff")))
consult.place(x=0, y=330, anchor="w")

#lista que tiene todos los botones de menu
menu_buttons = [tickets_menu, register, state, delete, consult]
menu_frame_show.tkraise()

screen.mainloop()