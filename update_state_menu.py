import tkinter as tk
from tkinter import ttk
from data import tickets
from ticket_make import state_label_dict, visual_tickets_dict
from notifications import notification_popup

def update_state_frame(parent):
        update_menu = tk.Frame(parent, bg="#FFFFFF")
        update_canvas = tk.Canvas(update_menu, bg="#FFFFFF")
        update_frame = tk.Frame(update_canvas, width=1065, height=600, bg="#FFFFFF")

        scroll = tk.Scrollbar(update_menu, orient="vertical", command=update_canvas.yview)
        scroll.pack(side="right", fill="y")   
        update_canvas.create_window((0,0), window=update_frame, anchor="nw")

        update_canvas.configure(yscrollcommand=scroll.set)
        update_frame.bind("<Configure>", lambda e: update_canvas.configure(scrollregion=update_canvas.bbox("all")))

        update_menu.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
        update_canvas.place(relx=0, rely=0, anchor="nw", width=1065, height=600)

        update_canvas.bind("<MouseWheel>", lambda event:move_scroll(event))

        state_box = ttk.Combobox(update_frame, values=["pending", "in progress", "resolved"], state="readonly", width=20)
        state_box.current(0)
        state_box.place(x=100, y=100, anchor="center")

        search_bar = tk.Entry(update_frame, bg="#ffffff", width=45, font=("Arial", 13))
        search_bar.place(relx=0.5, y=30, anchor="center")

        update_button = tk.Button(update_frame, text="Update", command=lambda:(update_state_ticket(state_box, search_bar, parent)))
        update_button.place(relx=0.5, rely=0.5, anchor="center", width=90, height=50)

        def move_scroll(event):
            movement = event.delta

            if movement > 0:
                update_canvas.yview_scroll(-2, "units")
            elif movement < 0:
                update_canvas.yview_scroll(2, "units")

        return update_menu, parent

def update_state_ticket(state_box, search_bar, parent):

    #Entrasda de datos
    id_search = search_bar.get()
    if id_search == "":
        notification_popup(parent, "Enter a ticket ID to update it")
        return 

    #Busqeda del billete
    ticket_found = None
    for ticket in tickets:
        if ticket == id_search:
            ticket_found = ticket
            break

    #validacion de existencia
    if ticket_found is None:
        notification_popup(parent, "Ticket ID has not been found")
        return

    highlight = tk.Canvas(visual_tickets_dict[ticket_found])
    highlight.place(width=0, height=0)

    #Modificacion del diccionario
    if state_box.current() == 0:
        tickets[ticket_found]["state"] = "Pending"
        state_label_dict[ticket_found].config(text="Pending")
        highlight.place()
        
        notification_popup(parent, "Ticket state successfully changed to: Pending")

    elif state_box.current() == 1:
        tickets[ticket_found]["state"] = "In process"
        state_label_dict[ticket_found].config(text="In process", fg="#f3cf6b")
        highlight.config(bg="#f3cf6b")
        highlight.place(x=-3, y=-1, width=20, height=180)
        
        notification_popup(parent, "Ticket state successfully changed to: in process")

    elif state_box.current() == 2:
        tickets[ticket_found]["state"] = "Resolved"
        state_label_dict[ticket_found].config(text="Resolved", fg="#12a182")
        highlight.config(bg="#12a182")
        highlight.place(x=-3, y=-1, width=20, height=180)        
        
        notification_popup(parent, "Ticket state successfully changed to: Resolved")