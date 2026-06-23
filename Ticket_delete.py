import tkinter as tk
from tkinter import *
 
screen = tk.Tk()
screen.title("Delete ticket")
screen.geometry("400x250")
 
Ticket_label=tk.Label(screen, text="Enter Ticket ID", font=("Arial", 12))
Ticket_label.pack(pady=10)
 
entry_ID= tk.Entry(screen, font=("Arial", 12))
entry_ID.pack(pady=5)
 
tk.Button(screen, text="Delete Ticket", bg="red", fg="white").pack(pady=20)
 
screen.mainloop()