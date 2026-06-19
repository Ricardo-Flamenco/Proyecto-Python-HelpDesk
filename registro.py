import tkinter as tk
from tkinter import ttk
from data import save_ticket
from maker_dicts import show_tickets

def register_ticket(parent, frame_show):

    menu_register_frame = tk.Frame(parent, bg="#ff0000")
    main_frame = tk.Frame(menu_register_frame, bg="white", padx=20, pady=20)
    menu_register_frame.place(relx=1.0, rely=1.0, anchor="se", width=700, height=500)
    main_frame.place(x=0, y=0, anchor="nw", width=700, height=500)

    title_label = tk.Label(main_frame, text="Reggister a New Ticket", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e3a8a")
    title_label.pack(pady=20)

    id_label = tk.Label(main_frame, text="Ticket ID", bg="white", font=("Arial", 12))
    id_label.pack(anchor="w")
    ticket_id_entry = tk.Entry(main_frame, width=40)
    ticket_id_entry.pack(pady=5)

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

    save_button = tk.Button(buttons_frame, text="Save", bg="#2563eb", fg="white", width=15, command=lambda:(save_ticket(ticket_id_entry, user_name_entry, problem_text, priority_box), show_tickets(frame_show)))
    save_button.grid(row=0,column=0,padx=10)

    clear_button = tk.Button(buttons_frame,text="Clear Form",bg="#6b7280",fg="white",width=15)
    clear_button.grid(row=0,column=1,padx=10)

    return menu_register_frame, ticket_id_entry, user_name_entry, problem_text, priority_box