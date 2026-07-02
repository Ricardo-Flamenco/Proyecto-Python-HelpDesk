import tkinter as tk
from tkinter import ttk

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
    ).place(x=120, y=30)

    search_bar = tk.Entry(
        update_frame,
        font=("Arial", 12),
        width=30
    )

    search_bar.place(x=30, y=60)

    
    tk.Label(
        update_frame,
        text="New Status",
        bg="white",
        font=("Arial", 11, "bold")
    ).place(x=420, y=30)

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

    state_box.current(0)

    state_box.place(x=360, y=60)

 

    update_button = tk.Button(
        update_frame,
        text="Update Status",
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

    update_button.place(x=650, y=55, width=150, height=35)

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