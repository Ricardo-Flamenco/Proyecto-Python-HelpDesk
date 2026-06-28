import tkinter as tk
from tkinter import *
from data import tickets
from notifications import notification_popup

def ticket_search_frame(parent, search_bar):

    search_bar.bind_all("<Return>", lambda event:buscar_ticket(search_bar))
    searched_ticket_frame = tk.Frame(parent, bg="#FFFFFF")
    searched_ticket_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    label_placeholder = tk.Label(searched_ticket_frame, text="No tickets searched", font=("Arial", 20, "bold"), fg="#414141", bg="#ffffff")
    label_placeholder.place(relx=0.5, rely=0.2, anchor="center")

    def buscar_ticket(search_bar):

        id_buscar = search_bar.get()

        if id_buscar == "":
            return

        if id_buscar in tickets:

            label_placeholder.destroy()
            searched_ticket_frame.tkraise()

            label_id = tk.Label(searched_ticket_frame,  text=f"{id_buscar}", font=("Arial", 20, "bold"))
            label_id.place(relx=0.5, rely=0.1, anchor="center") 

            label_user = tk.Label(searched_ticket_frame, text=f"{tickets[id_buscar]["user"]}", font=("Arial", 20, "bold"))  
            label_user.place(relx=0.3, rely=0.4, anchor="center")

            label_problem = tk.Label(searched_ticket_frame, text=f"{tickets[id_buscar]["problem"]}", font=("Arial", 20, "bold"))  
            label_problem.place(relx=0.3, rely=0.6, anchor="center")

            label_state = tk.Label(searched_ticket_frame, text=f"{tickets[id_buscar]["state"]}", font=("Arial", 20, "bold"))  
            label_state.place(relx=0.3, rely=0.8, anchor="center")

            label_priority = tk.Label(searched_ticket_frame, text=f"{tickets[id_buscar]["priority"]}", font=("Arial", 20, "bold"))  
            label_priority.place(relx=0.6, rely=0.4, anchor="center")
        else:
            notification_popup(parent, "Ticket ID has not been found")
       
        return searched_ticket_frame
    return search_bar, searched_ticket_frame
    