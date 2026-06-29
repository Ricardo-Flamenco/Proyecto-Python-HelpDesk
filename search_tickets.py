import tkinter as tk
from tkinter import *
from storage import tickets
from validations import search_ticket

def ticket_search_frame(parent, search_bar):

    search_bar.bind_all("<Return>", lambda event:(search_ticket(parent, search_bar), show_searched_ticket(search_ticket(parent, search_bar))))
    searched_ticket_frame = tk.Frame(parent, bg="#FFFFFF")
    searched_ticket_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    label_placeholder = tk.Label(searched_ticket_frame, text="No tickets searched", font=("Arial", 20, "bold"), fg="#414141", bg="#ffffff")
    label_placeholder.place(relx=0.5, rely=0.2, anchor="center")

    def show_searched_ticket(ticket):
        
        if ticket == None:
            return
        else:
            label_placeholder.destroy()
            searched_ticket_frame.tkraise()

            label_id = tk.Label(searched_ticket_frame,  text=f"{ticket}", font=("Arial", 20, "bold"))
            label_id.place(relx=0.5, rely=0.1, anchor="center") 

            label_user = tk.Label(searched_ticket_frame, text=f"{tickets[ticket]["user"]}", font=("Arial", 20, "bold"))  
            label_user.place(relx=0.3, rely=0.4, anchor="center")

            label_problem = tk.Label(searched_ticket_frame, text=f"{tickets[ticket]["problem"]}", font=("Arial", 20, "bold"))  
            label_problem.place(relx=0.3, rely=0.6, anchor="center")

            label_state = tk.Label(searched_ticket_frame, text=f"{tickets[ticket]["state"]}", font=("Arial", 20, "bold"))  
            label_state.place(relx=0.3, rely=0.8, anchor="center")

            label_priority = tk.Label(searched_ticket_frame, text=f"{tickets[ticket]["priority"]}", font=("Arial", 20, "bold"))  
            label_priority.place(relx=0.6, rely=0.4, anchor="center")
    
    return search_bar, searched_ticket_frame
    