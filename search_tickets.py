import tkinter as tk
from storage import tickets
from validations import search_ticket


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

        canvas = tk.Canvas(                     
            searched_ticket_frame,              
            bg="white",                         
            highlightthickness=0                
        )                                       

        scrollbar = tk.Scrollbar(               
            searched_ticket_frame,              
            orient="vertical",                  
            command=canvas.yview                
        )                                       

        canvas.configure(yscrollcommand=scrollbar.set)      

        scrollbar.pack(side="right", fill="y")              
        canvas.place(x=0, y=0, height=600, width=1065)  

        content = tk.Frame(canvas, bg="white")              

        canvas.create_window(                               
            (0, 0),                                         
            window=content,                                 
            anchor="nw"                                     
        )                                                   

        content.bind(                                       
            "<Configure>",                                 
            lambda e: canvas.configure(                    
                scrollregion=canvas.bbox("all")            
            )                                              
        )                                                  
        
        tk.Label(
            content,
            text=f"Ticket {ticket}",
            bg="white",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        info = tk.Frame(
            content,
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
            ).grid(row=fila, column=0, padx=20, pady=15, sticky="w")

            tk.Label(
                info,
                text=valor,
                font=("Arial", 14),
                bg="white",
                anchor="w",
                wraplength=800
            ).grid(row=fila, column=1, padx=20, pady=15, sticky="w")

        searched_ticket_frame.tkraise()

    search_bar.bind("<Return>", lambda event: buscar_ticket())

    return search_bar, searched_ticket_frame