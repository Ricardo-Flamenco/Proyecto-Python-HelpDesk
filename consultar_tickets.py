import tkinter as tk
from tkinter import ttk
import storage 
from notifications import notification_popup

def consult_tickets(parent):
    frame_consult_tickets = tk.Frame(parent, width=800, height=500, bg="#ffffff")
    frame_consult_tickets.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)

    title_label = tk.Label(frame_consult_tickets, text="View tickets", font=("Arial", 20, "bold"), bg="#ffffff",fg="#1e3a8a")
    title_label.pack(pady=20)

    table_frame = tk.Frame(frame_consult_tickets, bg="white")
    table_frame.pack(padx=20, pady=10, fill="both", expand=True)

    stats_frame = tk.Frame(frame_consult_tickets, bg="#ffffff", width=560, height=30, bd=2, relief="groove")
    stats_frame.place(x=30, y=70)

    ticket_count = tk.Label(stats_frame, text=f"Amount of tickets: {len(storage.tickets.keys())}", font=("Arial", 10, "bold"), bg="#ffffff")
    ticket_count.grid(row=0, column=0, padx=20, sticky="w")

    resolved_tickets = tk.Label(stats_frame, text=f"Resolved tickets: 0", font=("Arial", 10, "bold"), bg="#ffffff")
    resolved_tickets.grid(row=0, column=1, padx=20, sticky="w")

    pending_tickets = tk.Label(stats_frame, text=f"Pending tickets: 0", font=("Arial", 10, "bold"), bg="#ffffff")
    pending_tickets.grid(row=0, column=2, padx=20, sticky="w")

    high_tickets = tk.Label(stats_frame,  text=f"High priority tickets: 0", font=("Arial", 10, "bold"), bg="#ffffff")
    high_tickets.grid(row=0, column=3, padx=20, sticky="w")


    tickets_table = ttk.Treeview(table_frame,columns=("ID", "User", "Priority", "Status"),show="headings",height=12)

    tickets_table.heading("ID", text="Ticket ID")
    tickets_table.heading("User", text="User Name")
    tickets_table.heading("Priority", text="Priority")
    tickets_table.heading("Status", text="Status")

    tickets_table.column("ID", width=100, anchor="center")
    tickets_table.column("User", width=220, anchor="center")
    tickets_table.column("Priority", width=120, anchor="center")
    tickets_table.column("Status", width=120, anchor="center")

    tickets_table.pack(fill="both", expand=True, padx=(10, 0), pady=10)
    
    scrollbar = ttk.Scrollbar(tickets_table, orient="vertical", command=tickets_table.yview)
    tickets_table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y", padx=(0,0))

    buttons_frame = tk.Frame(frame_consult_tickets, bg="#ffffff")
    buttons_frame.pack(pady=20)

    refresh_button = tk.Button(buttons_frame,text="Refresh", width=15, height=2, font=("Arial", 11, "bold"), bg="#2563eb",fg="white", cursor="hand2", command=lambda:(refresh_table(), notification_popup(parent, "Table refreshed")))
    refresh_button.grid(row=0, column=0, padx=10)

    def refresh_table():
        # Vaciar la tabla
        tickets_resolved = 0
        tickets_high = 0
        tickets_pending = 0

        tickets_table.delete(*tickets_table.get_children())

        # Volver a llenarla
        for ticket_id in storage.tickets:
            tickets_table.insert("", tk.END, values=(ticket_id, storage.tickets[ticket_id]["user"], storage.tickets[ticket_id]["priority"], storage.tickets[ticket_id]["state"]))

        for ticket in storage.tickets:
            if storage.tickets[ticket]["state"] == "Resolved":
                tickets_resolved += 1

        for ticket in storage.tickets:
            if storage.tickets[ticket]["state"] == "Pending":
                tickets_pending += 1

        for ticket in storage.tickets:
            if storage.tickets[ticket]["priority"] == "High":
                tickets_high += 1

        ticket_count.config(text=f"Amount of tickets: {len(storage.tickets.keys())}")

        resolved_tickets.config(text=f"Resolved tickets: {tickets_resolved}")

        pending_tickets.config(text=f"Pending tickets: {tickets_pending}")

        high_tickets.config(text=f"High priority tickets: {tickets_high}")

    refresh_table()

    return frame_consult_tickets