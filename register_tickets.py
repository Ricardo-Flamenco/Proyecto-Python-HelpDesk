import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from data import save_ticket
from ticket_make import show_tickets

#Converti el diseño a un frame para que sea parte de la app el parametro "parent" es screen y se ve que se asigna en screen.py
def register_ticket(parent, frame_show, canva_show):

    menu_register_frame = tk.Frame(parent, bg="#ffffff")
    main_frame = tk.Frame(menu_register_frame, bg="white", padx=20, pady=20)
    menu_register_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    main_frame.place(x=0, y=0, anchor="nw", width=1065, height=600)

    title_label = tk.Label(main_frame, text="Create a new ticket:", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e3a8a")
    title_label.pack(pady=20)

    user_label = tk.Label(main_frame, text="User Name", bg="white", font=("Arial", 12))
    user_label.pack(anchor="w")
    user_name_entry = ctk.CTkEntry(main_frame, width=500, fg_color="#ffffff", text_color="#000000", placeholder_text="Enter your full name", corner_radius=10)
    user_name_entry.pack(pady=5)

    problem_label = tk.Label(main_frame, text="Describe your issue: ", bg="white", font=("Arial", 12))
    problem_label.pack(anchor="w")
    problem_text = ctk.CTkTextbox(main_frame, width=500, height=200, fg_color="#ffffff", text_color="#000000", corner_radius=10, border_width=2)
    problem_text.pack(pady=5)
    
    priority_label = tk.Label(main_frame, text="Priority Level:", bg="white", font=("Arial", 12))
    priority_label.pack(anchor="w")
    priority_box = ttk.Combobox(main_frame, values=["Low", "Medium", "High"], state="readonly", width=20, cursor="hand2")
    priority_box.current(0)
    priority_box.pack(pady=5)
    
    buttons_frame = tk.Frame(main_frame, bg="white")
    buttons_frame.pack(pady=20)

    save_button = tk.Button(buttons_frame, text="Save", bg="#2563eb", fg="white", width=15, cursor="hand2", command=lambda:(save_ticket(user_name_entry, problem_text, priority_box, parent) and show_tickets(frame_show, canva_show) and delay_creation(parent, save_button)))
    save_button.grid(row=0,column=0,padx=10)

    clear_button = tk.Button(buttons_frame,text="Clear Form",bg="#6b7280",fg="white",width=15, cursor="hand2", command=lambda:(clear_form(user_name_entry, problem_text)))
    clear_button.grid(row=0,column=1,padx=10)

    #return devuelve todos los datos que has ingresado y son mandados a data.py
    return menu_register_frame, user_name_entry, problem_text, priority_box

#funcion para el boton clear_form
def clear_form(user_name_entry, problem_text):
    user_name_entry.delete(0, tk.END)
    problem_text.delete("1.0", tk.END)

def delay_creation(parent, save_button):
    save_button.config(state="disabled", bg="#112e6e", fg="#ffffff")

    parent.after(2000, lambda:save_button.config(state="normal", bg="#2563eb"))

    