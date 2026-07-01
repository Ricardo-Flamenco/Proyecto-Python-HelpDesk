import tkinter as tk
from tkinter import *
from screen import frame_der
tickets = {}
number = 0

current_tickets = len(tickets)
ticket_count = tk.Label(frame_der, text=current_tickets)
ticket_count.place(x=50, y=90, anchor="center")