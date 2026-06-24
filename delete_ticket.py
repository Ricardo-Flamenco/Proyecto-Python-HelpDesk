import tkinter as tk
from tkinter import *
from data import tickets
 
def delete_tickets_menu(parent): 
    delete_menu_frame = tk.Frame(parent) 
    delete_menu_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)

    Ticket_label=tk.Label(delete_menu_frame, text="Enter a ticket ID to delete that ticket", font=("Arial", 15, "bold"))
    Ticket_label.place(rely=0.2, relx=0.5, anchor="center")
    
    id_delete = tk.Entry(delete_menu_frame, font=("Arial", 12))
    id_delete.place(rely=0.5, relx=0.5, anchor="center")
    
    delete_button = tk.Button(delete_menu_frame, text="Delete Ticket", bg="red", fg="white")
    delete_button.place(rely=0.7, relx=0.5, anchor="center")

    return delete_menu_frame, id_delete

def delete_ticket(id_delete):
    if id_delete in tickets:
        del tickets[id_delete]
        return True
    return False