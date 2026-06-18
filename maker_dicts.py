import tkinter as tk
from tkinter import *
from registro import tickets


i = 0

def tickets_frame_show(parent):

    frame_show = tk.Frame(parent, bg="#924141")
    frame_show.place(relx=1.0, rely=1.0, anchor="se", width=900, height=600)

    return frame_show

def show_tickets(frame_show):

    global i

    visual_ticket = tk.Frame(frame_show, bg="#0F9B9B", height=150, width=600)
    visual_ticket.grid(row=i, column=0, padx=20, pady=10, sticky="e")
    visual_ticket.grid_propagate(False)

    i += 1