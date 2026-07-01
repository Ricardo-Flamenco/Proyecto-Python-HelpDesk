import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Help Desk System")
window.geometry("800x500")
window.config(bg="#f3f4f6")

title_label = tk.Label(window, text="View Tickets", font=("Arial", 20, "bold"),bg="#f3f4f6",fg="#1e3a8a")

title_label.pack(pady=20)

table_frame = tk.Frame(window, bg="white")
table_frame.pack(padx=20, pady=10, fill="both", expand=True)

tickets_table = ttk.Treeview(table_frame,columns=("ID", "User", "Priority", "Status"),show="headings",height=12)

tickets_table.heading("ID", text="Ticket ID")
tickets_table.heading("User", text="User Name")
tickets_table.heading("Priority", text="Priority")
tickets_table.heading("Status", text="Status")

tickets_table.column("ID", width=100, anchor="center")
tickets_table.column("User", width=220, anchor="center")
tickets_table.column("Priority", width=120, anchor="center")
tickets_table.column("Status", width=120, anchor="center")

tickets_table.pack(fill="both", expand=True, padx=10, pady=10)

tickets_table.insert("",tk.END,values=("001", "Carlos", "High", "Pending"))

tickets_table.insert("",tk.END,values=("002", "Ana", "Medium", "Resolved"))

tickets_table.insert("",tk.END,values=("003", "Luis", "Low", "In Progress"))

buttons_frame = tk.Frame(window, bg="#f3f4f6")
buttons_frame.pack(pady=20)

refresh_button = tk.Button(buttons_frame,text="Refresh",width=15,bg="#2563eb",fg="white")

refresh_button.grid(row=0, column=0, padx=10)

back_button = tk.Button( buttons_frame, text="Back", width=15, bg="#6b7280", fg="white")

back_button.grid(row=0, column=1, padx=10)

window.mainloop()