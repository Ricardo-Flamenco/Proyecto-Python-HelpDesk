import tkinter as tk
from tkinter import ttk
from tkinter import *
from data import tickets


i = 0

def tickets_frame_show(parent):
    
    frame_show = tk.Frame(parent, bg="#AF7D7D")
    frame_show.place(relx=1.0, rely=1.0, anchor="se", width=900, height=600)

    return frame_show

def show_tickets(frame_show):

    global i

    for key in tickets.keys():
        visual_ticket = tk.Frame(frame_show, relief="raised", bd=3, width=700, height=90 )
        visual_ticket.grid(row=i, column=0, padx=20, pady=30, sticky="e")

        id = tk.Label(visual_ticket, text=f"{key}", font=("Arial", 15, "bold"))
        id.place(relx=0.05, rely=0.5, anchor="center")

        user = tk.Label(visual_ticket, text=f"{tickets[key]["user"]}", font=("Arial", 10))
        user.place(relx=0.25, rely=0.5, anchor="center")

        problem = tk.Label(visual_ticket, text=f"{tickets[key]["problem"]}", font=("Arial", 10))
        problem.place(relx=0.45, rely=0.5, anchor="center")

        priority = tk.Label(visual_ticket, text=f"{tickets[key]["priority"]}", font=("Arial", 10))
        priority.place(relx=0.65, rely=0.5, anchor="center")

        priority_box = ttk.Combobox(visual_ticket, values=["pending", "in progress", "resolved"], state="readonly", width=20)
        priority_box.current(0)
        priority_box.place(relx=0.85, rely=0.5, anchor="center")

    i += 1