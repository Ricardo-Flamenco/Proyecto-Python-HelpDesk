import tkinter as tk
from tkinter import *

def notification_popup(parent, text):
    notification = tk.Toplevel(parent)
    notification.geometry(f"450x50+{parent.winfo_screenwidth() - 450}+{parent.winfo_screenheight() - 150}")
    notification.overrideredirect(True)

    notification_label = tk.Label(notification, text=text, font=("Arial", 15, "bold"), bg="#ffffff", relief="raised", wraplength=400)
    notification_label.pack(fill="both", expand=True)

    notification.after(2000 ,lambda:notification.destroy())