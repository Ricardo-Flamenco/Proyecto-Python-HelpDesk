import tkinter as tk
from tkinter import *
from storage import tickets
from ticket_make import visual_tickets_dict
from notifications import notification_popup
 
def delete_tickets_menu(parent): 
    delete_menu_frame = tk.Frame(parent, bg="#FFFFFF") 
    delete_menu_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)

    ticket_label=tk.Label(delete_menu_frame, text="Enter a ticket ID to delete that ticket", font=("Arial", 15, "bold"), bg="#FFFFFF")
    ticket_label.place(rely=0.2, relx=0.5, anchor="center")
    
    entry_delete = tk.Entry(delete_menu_frame, font=("Arial", 12))
    entry_delete.place(rely=0.5, relx=0.5, anchor="center")
    
    delete_button = tk.Button(delete_menu_frame, text="Delete Ticket", bg="red", fg="white", command=lambda:delete_ticket(entry_delete))
    delete_button.place(rely=0.7, relx=0.5, anchor="center")

    def delete_ticket(entry_delete):

        id_delete = entry_delete.get()
        if id_delete == "":
            notification_popup(parent, "Enter a ticket ID to delete")
            return

        if id_delete in tickets:
            del tickets[id_delete]
            visual_tickets_dict[id_delete].destroy()
            notification_popup(parent, "Ticket deleted successfully")
        else:
            notification_popup(parent, "Ticket ID has not been found")

    return delete_menu_frame