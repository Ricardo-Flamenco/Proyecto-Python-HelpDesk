import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

close = NONE

def images_init():

    global close

    close = Image.open("assets/x-solid.ico")
    close = close.resize((20, 20), Image.Resampling.LANCZOS)
    close = ImageTk.PhotoImage(close)

def notification_popup(parent, text):
    notification = tk.Toplevel(parent)
    notification.geometry(f"450x50+{parent.winfo_screenwidth() - 450}+{parent.winfo_screenheight() - 150}")
    notification.overrideredirect(True)

    notification_label = tk.Label(notification, text=text, font=("Arial", 14, "bold"), bg="#FFFFFF", relief="raised", wraplength=400)
    notification_label.pack(fill="both", expand=True)

    notification.after(2000 ,lambda:notification.destroy())

def notification_popup_close(parent, text):

    global close

    notification = tk.Toplevel(parent)
    notification.geometry(f"400x100+{parent.winfo_screenwidth() - 400}+{parent.winfo_screenheight() - 150}")
    notification.overrideredirect(True)

    notification_label = tk.Label(notification, text=text, font=("Arial", 14, "bold"), bg="#FFFFFF", relief="raised", wraplength=400)
    notification_label.pack(fill="both", expand=True)
    close_button = tk.Button(notification, image=close, font=("Arial", 13, "bold"), bd=0, bg="#ffffff", command=lambda:notification.destroy())
    close_button.place(rely=0.1, relx=0.9, width=20, height=20)