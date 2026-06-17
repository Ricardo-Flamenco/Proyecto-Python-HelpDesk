import tkinter as tk
from tkinter import *
from registro import tickets

def tickets_show(parent):
    box_show = tk.Canvas(parent, bg="#303030")
    frame_tickets = tk.Frame()
    box_show.place(relx=1.0, rely=1.0, anchor="se", width=900, height=600)