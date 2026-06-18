import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

tickets = {}

def save_ticket(ticket_id_entry, user_name_entry, problem_text, priority_box):

    ticket_id = ticket_id_entry.get()
    user_name = user_name_entry.get()
    problem = problem_text.get("1.0", tk.END).strip()
    priority = priority_box.get()

    if ticket_id == "" or user_name == ""  or problem == "":
        messagebox.showerror("Missing Information", "Please complete all fields") 
    else:
        tickets[ticket_id] = {"id": ticket_id,
        "user": user_name,
        "problem": problem,
        "priority": priority,
        "state": "pending"
       }

