import tkinter as tk
from storage import tickets
from validaciones import search_ticket


def ticket_search_frame(parent, search_bar):

    searched_ticket_frame = tk.Frame(parent, bg="#FFFFFF")
    searched_ticket_frame.place(
        relx=1.0,
        rely=1.0,
        anchor="se",
        width=1065,
        height=600
    )

    placeholder = tk.Label(
        searched_ticket_frame,
        text="No tickets searched",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#555555"
    )

    placeholder.place(relx=0.5, rely=0.5, anchor="center")


    def buscar_ticket():

        ticket = search_ticket(parent, search_bar)

        if ticket is None:
            return

       
        for widget in searched_ticket_frame.winfo_children():
            widget.destroy()

        data = tickets[ticket]

        
        tk.Label(
            searched_ticket_frame,
            text=f"Ticket {ticket}",
            bg="white",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        info = tk.Frame(
            searched_ticket_frame,
            bg="white"
        )

        info.pack(pady=20)

        campos = [
            ("User", data["user"]),
            ("Problem", data["problem"]),
            ("State", data["state"]),
            ("Priority", data["priority"])
        ]

        for fila, (nombre, valor) in enumerate(campos):

            tk.Label(
                info,
                text=f"{nombre}:",
                font=("Arial", 14, "bold"),
                bg="white",
                anchor="w",
                width=12
            ).grid(row=fila, column=0, padx=20, pady=15, sticky="w")

            tk.Label(
                info,
                text=valor,
                font=("Arial", 14),
                bg="white",
                anchor="w"
            ).grid(row=fila, column=1, padx=20, pady=15, sticky="w")

        searched_ticket_frame.tkraise()

    search_bar.bind("<Return>", lambda event: buscar_ticket())

    return search_bar, searched_ticket_frame