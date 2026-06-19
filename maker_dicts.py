import tkinter as tk
from tkinter import ttk
from tkinter import *
from data import tickets


i = 0

def tickets_frame_show(parent):
    
    frame_show = tk.Frame(parent, bg="#FFFFFF")
    frame_show.place(relx=1.0, rely=1.0, anchor="se", width=940, height=600)

    return frame_show

def show_tickets(frame_show):

    global i

    for key in tickets.keys():
        visual_ticket = tk.Frame(frame_show, relief="raised", bd=3, width=900, height=90 )
        visual_ticket.grid(row=i, column=0, padx=20, pady=30, sticky="e")

        id = tk.Label(visual_ticket, text=f"{key}", font=("Arial", 15, "bold"), wraplength=144)
        id.place(x=30, rely=0.5, anchor="center")

        user = tk.Label(visual_ticket, text=f"{tickets[key]["user"]}", font=("Arial", 10), wraplength=144)
        user.place(x=204, rely=0.5, anchor="center")

        problem = tk.Label(visual_ticket, text=f"{tickets[key]["problem"]}", font=("Arial", 10), wraplength=144)
        problem.place(x=378, rely=0.5, anchor="center")

        priority = tk.Label(visual_ticket, text=f"{tickets[key]["priority"]}", font=("Arial", 10), wraplength=144)
        priority.place(x=552, rely=0.5, anchor="center")

        state_box = ttk.Combobox(visual_ticket, values=["pending", "in progress", "resolved"], state="readonly", width=20)
        state_box.current(0)
        state_box.place(x=726, rely=0.5, anchor="center")

    i += 1