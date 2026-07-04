import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from storage import tickets
from ticket_make import state_label_dict, visual_tickets_dict
from notifications import notification_popup
from validations import change_status

def update_state_frame(parent):

    update_menu = tk.Frame(parent, bg="white")
    update_menu.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)

    update_canvas = tk.Canvas(
        update_menu,
        bg="white",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        update_menu,
        orient="vertical",
        command=update_canvas.yview
    )

    update_frame = tk.Frame(
        update_canvas,
        bg="white",
        width=1065,
        height=600
    )

    scrollbar.pack(side="right", fill="y")

    update_canvas.configure(yscrollcommand=scrollbar.set)
    update_canvas.create_window((0, 0), window=update_frame, anchor="nw")

    update_canvas.pack(fill="both", expand=True)

    update_frame.bind(
        "<Configure>",
        lambda e: update_canvas.configure(
            scrollregion=update_canvas.bbox("all")
        )
    )

    def move_scroll(event):
        update_canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    update_canvas.bind("<MouseWheel>", move_scroll)

    tk.Label(
        update_frame,
        text="Ticket ID",
        bg="white",
        font=("Arial", 11, "bold")
    ).place(x=150, y=30)

    search_bar = ctk.CTkEntry(
        update_frame,
        fg_color="#ffffff",
        text_color="#000000", 
        placeholder_text="Change the state of a tickets by ID", 
        font=("Arial", 13), 
        corner_radius=10, 
        width=275
    )

    tk.Label(
        update_frame,
        text="New Status",
        bg="white",
        font=("Arial", 11, "bold")
    ).place(x=460, y=30)

    state_box = ttk.Combobox(
        update_frame,
        state="readonly",
        width=18,
        values=[
            "Pending",
            "In process",
            "Resolved"
        ]
    )

    tk.Label(
        update_frame,
        text="Ticket being modified:",
        bg="white",
        font=("Arial", 11, "bold")
    ).place(relx=0.05, rely=0.2)

    search_bar.place(x=55, y=60)
    search_bar.bind("<KeyRelease>", lambda e: show_match())

    frame_show_ticket_eliminate = tk.Frame(update_frame, padx=55, pady=15, bd=2, relief="ridge", bg="#FFFFFF")
    frame_show_ticket_eliminate.place(rely=0.25, relx=0.05, relheight=0.65, relwidth=0.9)

    def show_match():

        ticket_match = search_bar.get()
        if ticket_match in tickets:
            for widget in frame_show_ticket_eliminate.winfo_children():
                widget.destroy()
            tk.Label(
            frame_show_ticket_eliminate,
            text=f"Ticket #{tickets[ticket_match]["id"]}",
            font=("Arial", 20, "bold"),
            bg="white"
            ).pack(pady=15)

            tk.Label(
                frame_show_ticket_eliminate,
                text="User",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=30, y=70)

            tk.Label(frame_show_ticket_eliminate, text=f"{tickets[ticket_match]["user"][:45] + "..." if len(tickets[ticket_match]["user"]) > 45 else tickets[ticket_match]["user"]}",
                font=("Arial", 13),
                bg="white",
                justify="left"
            ).place(x=30, y=100)

            tk.Label(
                frame_show_ticket_eliminate,
                text="Description",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=30, y=145)

            tk.Label(
                frame_show_ticket_eliminate,
                text=f"{tickets[ticket_match]["problem"][:55] + "..." if len(tickets[ticket_match]["problem"]) > 55 else tickets[ticket_match]["problem"]}",
                font=("Arial", 13),
                bg="white",
                justify="left"
            ).place(x=30, y=175)
           
            tk.Label(
                frame_show_ticket_eliminate,
                text="Priority",
                font=("Arial", 15, "bold"),
                bg="white"
            ).place(x=30, y=220)

            tk.Label(
                frame_show_ticket_eliminate,
                text=f"{tickets[ticket_match]["priority"]}",
                bg="white",
                font=("Arial", 13),
                justify="left"
            ).place(x=60, y=250)
            priority_box = tk.Canvas(frame_show_ticket_eliminate, bd=0)
            match tickets[ticket_match]["priority"]:
                case "Low":
                    priority_box.configure(bg="#00A035")
                case "Medium":
                    priority_box.configure(bg="#f8c24d")
                case "High":
                    priority_box.configure(bg="#da3535")
            priority_box.place(x=30, y=250, width=20, height=20)

            tk.Label(
                frame_show_ticket_eliminate,
                text=f"Current state: {tickets[ticket_match]["state"]}",
                font=("Arial", 18, "bold"),
                bg="white",
                justify="left"
            ).place(x=500, rely=0.45)
           
        else:
            for widget in frame_show_ticket_eliminate.winfo_children():
                widget.destroy()
            tk.Label(
                frame_show_ticket_eliminate,
                text="ID doesn´t match any ticket",
                font=("Arial", 18, "bold"),
                bg="white"
            ).place(relx=0.5, rely=0.5, anchor="center")
        

    state_box.current(0)

    state_box.place(x=435, y=60)

    update_button = tk.Button(
        update_frame,
        text="Update State",
        bg="#0F62FE",
        fg="white",
        font=("Arial", 11, "bold"),
        cursor="hand2",
        command=lambda: update_state_ticket(
            change_status(
                state_box,
                search_bar,
                parent
            )
        )
    )

    update_button.place(x=700, y=55, width=150, height=35)

    return update_menu


def update_state_ticket(result):

    if result is None:
        return

    new_status, parent, ticket_found = result

    tickets[ticket_found]["state"] = new_status

    colors = {
        "Pending": "#FFFFFF",
        "In process": "#f3cf6b",
        "Resolved": "#12a182"
    }

    state_label_dict[ticket_found].config(
        text=new_status,
        fg=colors[new_status]
    )

    ticket_frame = visual_tickets_dict[ticket_found]

    highlight = tk.Frame(
        ticket_frame,
        bg=colors[new_status],
        width=8
    )

    highlight.place(
        x=0,
        y=0,
        relheight=1
    )

    notification_popup(
        parent,
        f"Ticket state successfully changed to: {new_status}"
    )

    #key_realease