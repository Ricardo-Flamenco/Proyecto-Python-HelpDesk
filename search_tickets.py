import tkinter as tk
import customtkinter as ctk
import storage 
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

    def buscar_ticket():

        ticket = search_ticket(parent, search_bar)

        if ticket is None:
            return

       
        for widget in searched_ticket_frame.winfo_children():
            widget.destroy()

        data = storage.tickets[ticket]

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

        fila = len(campos)

        tk.Label(
            info,
            text="Priority:",
            font=("Arial", 14, "bold"),
            bg="white"
        ).grid(row=fila, column=0, padx=20, pady=15, sticky="w")

        priority_frame = tk.Frame(info, bg="white")
        priority_frame.grid(row=fila, column=1, padx=20, pady=15, sticky="w")

        priority_box = tk.Canvas(
            priority_frame,
            width=20,
            height=20,
            highlightthickness=0,
            bd=0
            )

        match data["priority"]:
            case "Low":
                color = "#00A035"
            case "Medium":
                color = "#f8c24d"
            case "High":
                color = "#da3535"

        priority_box.configure(bg=color)
        priority_box.pack(side="left")
        
        tk.Label(
            priority_frame,
            text=data["priority"],
            font=("Arial", 14),
            bg="white"
        ).pack(side="left", padx=(10, 0))
        searched_ticket_frame.tkraise()

    search_bar.bind("<Return>", lambda event: buscar_ticket())

    return search_bar, searched_ticket_frame