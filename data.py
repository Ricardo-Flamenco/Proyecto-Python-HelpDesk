import tkinter as tk
from tkinter import messagebox

tickets = {}
number = 0

def save_ticket(user_name_entry, problem_text, priority_box):

    global number
    ticket_id = f"{number:04d}"

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
        
        number += 1
