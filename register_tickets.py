import tkinter as tk
from tkinter import ttk
from data import save_ticket
from ticket_make import show_tickets

#Converti el diseño a un frame para que sea parte de la app el parametro "parent" es screen y se ve que se asigna en screen.py
def register_ticket(parent, frame_show):

    menu_register_frame = tk.Frame(parent, bg="#ffffff")
    main_frame = tk.Frame(menu_register_frame, bg="white", padx=20, pady=20)
    menu_register_frame.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    main_frame.place(x=0, y=0, anchor="nw", width=960, height=600)

    title_label = tk.Label(main_frame, text="Reggister a New Ticket", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e3a8a")
    title_label.pack(pady=20)

    user_label = tk.Label(main_frame, text="User Name", bg="white", font=("Arial", 12))
    user_label.pack(anchor="w")
    user_name_entry = tk.Entry(main_frame, width=40)
    user_name_entry.pack(pady=5)

    problem_label = tk.Label(main_frame, text="Problem Description", bg="white", font=("Arial", 12))
    problem_label.pack(anchor="w")
    problem_text = tk.Text(main_frame,width=50,height=5)
    problem_text.pack(pady=5)

    priority_label = tk.Label(main_frame, text="Priority Level", bg="white", font=("Arial", 12))
    priority_label.pack(anchor="w")
    priority_box = ttk.Combobox(main_frame, values=["Low", "Medium", "High"],state="readonly", width=20)
    priority_box.current(0)
    priority_box.pack(pady=5)
    
    buttons_frame = tk.Frame(main_frame, bg="white")
    buttons_frame.pack(pady=20)

    save_button = tk.Button(buttons_frame, text="Save", bg="#2563eb", fg="white", width=15, command=lambda:(save_ticket(user_name_entry, problem_text, priority_box) and show_tickets(frame_show) and notification(parent)))
    save_button.grid(row=0,column=0,padx=10)

    clear_button = tk.Button(buttons_frame,text="Clear Form",bg="#6b7280",fg="white",width=15, command=lambda:(clear_form(user_name_entry, problem_text)))
    clear_button.grid(row=0,column=1,padx=10)

    #return devuelve todos los datos que has ingresado y son mandados a data.py
    return menu_register_frame, user_name_entry, problem_text, priority_box

#funcion para el boton clear_form
def notification(parent):
    notification = tk.Toplevel(parent)
    notification.geometry(f"350x50+{parent.winfo_screenwidth() - 350}+{parent.winfo_screenheight() - 150}")
    notification.overrideredirect(True)
    notification_label = tk.Label(notification, text="A ticket has been created", font=("Arial", 20, "bold"), bg="#ffffff", relief="raised")
    notification_label.pack(fill="both", expand=True)

    notification.after(2000, lambda:notification.destroy())

def clear_form(user_name_entry, problem_text):
    user_name_entry.delete(0, tk.END)
    problem_text.delete("1.0", tk.END)