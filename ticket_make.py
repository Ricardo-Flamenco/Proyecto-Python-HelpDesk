import tkinter as tk
from tkinter import ttk
from tkinter import *
import storage

row = 0
state_label_dict = {}
visual_tickets_dict = {}

#Se crea el frame donde se crearan los tickets con un scroll parent es screen y es asignado en screen.py
def tickets_frame_show(parent):
    
    menu_frame_show = tk.Frame(parent, bg="#FFFFFF")
    canva_show = tk.Canvas(menu_frame_show, bg="#FFFFFF")
    frame_show = tk.Frame(canva_show, bg="#ffffff")

    #Un label que es tapado cuando se crea el primer ticket
    information_menu = tk.Label(menu_frame_show, text="Created tickets will appear here", font=("Arial", 15, "bold"), fg="#414141", bg="#ffffff")
    information_menu.place(x=10, relwidth=0.98)

    scroll = tk.Scrollbar(menu_frame_show, orient="vertical", command=canva_show.yview)
    scroll.pack(side="right", fill="y")    
    canva_show.create_window((0,0), window=frame_show, anchor="nw")

    canva_show.configure(yscrollcommand=scroll.set)
    frame_show.bind("<Configure>", lambda e: canva_show.configure(scrollregion=canva_show.bbox("all")))

    menu_frame_show.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    canva_show.place(relx=0, rely=0, anchor="nw", width=1065, height=600)

    canva_show.bind_all("<MouseWheel>", lambda event:move_scroll(event))
    show_tickets(frame_show)


    def move_scroll(event):

        if frame_show.winfo_height() > canva_show.winfo_height():
            movement = event.delta

            if movement > 0:
                canva_show.yview_scroll(-2, "units")
            elif movement < 0:
                canva_show.yview_scroll(2, "units")

    return menu_frame_show, frame_show, information_menu

def show_tickets(frame_show):

    global row
    for widget in frame_show.winfo_children():
        widget.destroy()

    #de data.py es importado tickets y en base al ultimo elemento el que es creado se crea visual_tickets 
    for key in storage.tickets:

        visual_ticket = tk.Frame(frame_show, relief="raised", bd=2, width=800, height=90 )
        visual_ticket.grid(row=row, column=0, padx=20, pady=30, sticky="e")

        visual_tickets_dict[key] = visual_ticket

        #IDs
        id_label = tk.Label(visual_ticket, text="ID:")
        id_label.place(x=60, rely=0.15, anchor="center")
        id = tk.Label(visual_ticket, text=f"# {key}", font=("Arial", 10, "bold"), wraplength=144)
        id.place(x=60, rely=0.5, anchor="center")

        #USER
        user_label = tk.Label(visual_ticket, text="User:")
        user_label.place(x=204, rely=0.15, anchor="center")
        user = tk.Label(visual_ticket, text=f"{storage.tickets[key]["user"][:30] + "..." if len(storage.tickets[key]["user"]) > 31 else storage.tickets[key]["user"]}", font=("Arial", 10), wraplength=144)
        user.place(x=204, rely=0.5, anchor="center")

        #PROBLEM
        problem_label = tk.Label(visual_ticket, text="Description:")
        problem_label.place(x=378, rely=0.15, anchor="center")
        problem = tk.Label(visual_ticket, text=f"{storage.tickets[key]["problem"][:35] + "..." if len(storage.tickets[key]["problem"]) > 35 else storage.tickets[key]["problem"]}", font=("Arial", 10), wraplength=164)
        problem.place(x=378, rely=0.5, anchor="center")

        #PRIORITY
        priority = tk.Label(visual_ticket, text=f"{storage.tickets[key]["priority"]}", font=("Arial", 10), anchor="w", wraplength=144)
        priority.place(x=552, rely=0.5, anchor="w")
        priority_box = tk.Canvas(visual_ticket, bd=0)
        match storage.tickets[key]["priority"]:
            case "Low":
                priority_box.configure(bg="#00A035")
            case "Medium":
                priority_box.configure(bg="#f8c24d")
            case "High":
                priority_box.configure(bg="#da3535")
        priority_box.place(x=537, rely=0.5, anchor="center", width=20, height=20)

        #STATE
        state_label = tk.Label(visual_ticket, text=f"{storage.tickets[key]["state"]}", font=("Arial", 10, "bold"), anchor="w", wraplength=144)
        state_label.place(x=726, rely=0.5, anchor="center")

        state_label_dict[key] = state_label
        row += 1
    return True