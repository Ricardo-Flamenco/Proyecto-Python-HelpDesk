import tkinter as tk
from tkinter import ttk
from tkinter import *
from data import tickets


i = 0

#Se crea el frame donde se crearan los tickets con un scroll parent es screen y es asignado en screen.py
def tickets_frame_show(parent):
    
    menu_frame_show = tk.Frame(parent, bg="#FFFFFF")
    canva_show = tk.Canvas(menu_frame_show, bg="#FFFFFF")
    frame_show = tk.Frame(canva_show, bg="#ffffff")

    #Un label que es tapado cuando se crea el primer ticket
    information_menu = tk.Label(frame_show, text="Created tickets will appear here", font=("Arial", 20, "bold"), fg="#414141", bg="#ffffff")
    information_menu.grid(padx=260, pady=40, sticky="e")

    scroll = tk.Scrollbar(menu_frame_show, orient="vertical", command=canva_show.yview)
    scroll.pack(side="right", fill="y")    
    canva_show.create_window((0,0), window=frame_show, anchor="nw")

    canva_show.configure(yscrollcommand=scroll.set)
    frame_show.bind("<Configure>", lambda e: canva_show.configure(scrollregion=canva_show.bbox("all")))

    menu_frame_show.place(relx=1.0, rely=1.0, anchor="se", width=960, height=600)
    canva_show.place(relx=0, rely=0, anchor="nw", width=960, height=600)

    return menu_frame_show, frame_show

def show_tickets(frame_show):

    global i

    #de data.py es importado tickets y en base al ultimo elemento el que es creado se crea visual_tickets 
    key = next(reversed(tickets))

    visual_ticket = tk.Frame(frame_show, relief="raised", bd=3, width=900, height=90 )
    visual_ticket.grid(row=i, column=0, padx=20, pady=30, sticky="e")

    id = tk.Label(visual_ticket, text=f"{key}", font=("Arial", 15, "bold"), wraplength=144)
    id.place(x=30, rely=0.5, anchor="center")

    user = tk.Label(visual_ticket, text=f"{tickets[key]["user"]}", font=("Arial", 10), wraplength=144)
    user.place(x=204, rely=0.5, anchor="center")

    problem = tk.Label(visual_ticket, text=f"{tickets[key]["problem"]}", font=("Arial", 10), wraplength=164)
    problem.place(x=378, rely=0.5, anchor="center")

    priority = tk.Label(visual_ticket, text=f"{tickets[key]["priority"]}", font=("Arial", 10), wraplength=144)
    priority.place(x=552, rely=0.5, anchor="center")

    state_box = ttk.Combobox(visual_ticket, values=["pending", "in progress", "resolved"], state="readonly", width=20)
    state_box.current(0)
    state_box.place(x=726, rely=0.5, anchor="center")

    #si el contenido es mucho para que quepa en el ticket se hace lo siguiente para adaptar el ticket la contenido 
    needed_user_height = user.winfo_reqheight()
    needed_problem_height = problem.winfo_reqheight()

    needed_height = max(needed_user_height, needed_problem_height)

    if needed_height > 90 :
        visual_ticket.configure(height=needed_height + 40)

    i += 1