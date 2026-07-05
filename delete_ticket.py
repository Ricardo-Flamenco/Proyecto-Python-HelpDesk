import tkinter as tk
from tkinter import *
from storage import tickets
from ticket_make import visual_tickets_dict
from notifications import notification_popup
import customtkinter as ctk
 
def delete_tickets_menu(parent): 
    delete_menu_frame = tk.Frame(parent, bg="#FFFFFF") 
    delete_menu_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)

    ticket_label=tk.Label(delete_menu_frame, text="Enter a ticket ID to delete that ticket", font=("Arial", 11, "bold"), bg="#FFFFFF")
    ticket_label.place(x=55, y=30)
    
    entry_delete = ctk.CTkEntry(delete_menu_frame, width=350, font=("Arial", 12), fg_color="#ffffff", text_color="#000000", placeholder_text="Delete tickets by ID", corner_radius=10)
    entry_delete.place(x=55, y=60)
    entry_delete.bind("<KeyRelease>", lambda e: show_match())
    
    delete_button = tk.Button(delete_menu_frame, text="Delete Ticket", bg="red", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=lambda:delete_ticket(entry_delete))
    delete_button.place(x=500, y=55, width=150, height=35)

    frame_show_ticket_eliminate = tk.Frame(delete_menu_frame, padx=55, pady=15, bd=2, relief="ridge", bg="#FFFFFF")
    frame_show_ticket_eliminate.place(rely=0.25, relx=0.05, relheight=0.65, relwidth=0.9)

    tk.Label(
        delete_menu_frame,
        text="Ticket being deleted:",
        bg="white",
        font=("Arial", 11, "bold")
    ).place(relx=0.05, rely=0.2)

    def show_match():

        ticket_match = entry_delete.get()
        if ticket_match in tickets:
            for widget in frame_show_ticket_eliminate.winfo_children():
                widget.destroy()
            tk.Label(
            frame_show_ticket_eliminate,
            text=f"Ticket #{tickets[ticket_match]["id"]}",
            font=("Arial", 20, "bold"),
            bg="white"
            ).pack(pady=15)

            tk.Label(
                frame_show_ticket_eliminate,
                text="User",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=60, y=100)

            tk.Label(frame_show_ticket_eliminate, text=f"{tickets[ticket_match]["user"][:45] + "..." if len(tickets[ticket_match]["user"]) > 45 else tickets[ticket_match]["user"]}",
                font=("Arial", 13),
                bg="white",
                justify="left"
            ).place(x=60, y=130)

            tk.Label(
                frame_show_ticket_eliminate,
                text="Description",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=60, y=160)

            tk.Label(
                frame_show_ticket_eliminate,
                text=f"{tickets[ticket_match]["problem"][:55] + "..." if len(tickets[ticket_match]["problem"]) > 55 else tickets[ticket_match]["problem"]}",
                font=("Arial", 13),
                bg="white",
                justify="left"
            ).place(x=60, y=190)
           
            tk.Label(
                frame_show_ticket_eliminate,
                text="Priority",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=500, y=100)

            tk.Label(
                frame_show_ticket_eliminate,
                text=f"{tickets[ticket_match]["priority"]}",
                bg="white",
                font=("Arial", 13),
                justify="left"
            ).place(x=520, y=130)
            priority_box = tk.Canvas(frame_show_ticket_eliminate, bd=0)
            match tickets[ticket_match]["priority"]:
                case "Low":
                    priority_box.configure(bg="#00A035")
                case "Medium":
                    priority_box.configure(bg="#f8c24d")
                case "High":
                    priority_box.configure(bg="#da3535")
            priority_box.place(x=500, y=130, width=20, height=20)
            
            tk.Label(
                frame_show_ticket_eliminate,
                text="State",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=500, y=160)
            tk.Label(
                frame_show_ticket_eliminate,
                text=f"Current state: {tickets[ticket_match]["state"]}",
                font=("Arial", 13),
                bg="white",
                justify="left"
            ).place(x=500, y=190)
           
        else:
            for widget in frame_show_ticket_eliminate.winfo_children():
                widget.destroy()
            tk.Label(
                frame_show_ticket_eliminate,
                text="ID doesn´t match any ticket",
                font=("Arial", 18, "bold"),
                bg="white"
            ).place(relx=0.5, rely=0.5, anchor="center")
        


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