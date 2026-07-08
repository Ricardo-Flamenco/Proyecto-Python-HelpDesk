import tkinter as tk
from tkinter import ttk
from tkinter import *
import storage

row = 0
state_label_dict = {}
visual_tickets_dict = {}
refresh_home = None

#Se crea el frame donde se crearan los tickets con un scroll parent es screen y es asignado en screen.py
def tickets_frame_show(parent):

    global refresh_home
    
    menu_frame_show = tk.Frame(parent, bg="#FFFFFF")
    canva_show = tk.Canvas(menu_frame_show, bg="#FFFFFF")
    frame_show = tk.Frame(canva_show, bg="#ffffff")

    scroll = tk.Scrollbar(menu_frame_show, orient="vertical", command=canva_show.yview)
    canva_show.create_window((0,0), window=frame_show, anchor="nw")

    canva_show.configure(yscrollcommand=scroll.set)
    frame_show.bind("<Configure>", lambda e: canva_show.configure(scrollregion=canva_show.bbox("all")))

    menu_frame_show.place(relx=1.0, rely=1.0, anchor="se", width=1065, height=600)
    canva_show.place(x=370, y=150, anchor="nw", width=700, height=440)

    canva_show.bind_all("<MouseWheel>", lambda event:move_scroll(event))
    show_tickets(frame_show, canva_show)
    menu_frame_show.after(10, lambda: canva_show.yview_moveto(1.0))

    def move_scroll(event):

        if frame_show.winfo_height() > canva_show.winfo_height():
            movement = event.delta

            if movement > 0:
                canva_show.yview_scroll(-2, "units")
            elif movement < 0:
                canva_show.yview_scroll(2, "units")

    frame_graphic = tk.Frame(menu_frame_show)
    frame_graphic.place(relx=0.01, y=150, anchor="nw", width=355, height=440)
    graphic_priority = tk.Canvas(frame_graphic)
    graphic_priority.place(x=0, y=0, width=355, height=200)

    graphic_state = tk.Canvas(frame_graphic)
    graphic_state.place(x=0, y=200, width=355, height=200)

    total_tickets = tk.Label(frame_graphic, text=f"Total tickets: {len(storage.tickets.keys())}", font=("Arial", 14, "bold"))
    total_tickets.place(x=20, y=405)

    frame_stats = tk.Frame(menu_frame_show)
    frame_stats.place(x=10, y=10, width=1045, height=130)

    priority_low = tk.Label(frame_stats, text="Low: ", font=("Arial", 12, "bold"), anchor="w")
    priority_low.place(x=60, y=25, anchor="w")
    box_low = tk.Canvas(frame_stats, bd=0, bg="#00A035")
    box_low.place(x=30, y=25, anchor="w", width=25, height=25)

    priority_medium = tk.Label(frame_stats, text="Medium: ", font=("Arial", 12, "bold"), anchor="w")
    priority_medium.place(x=60, y=65, anchor="w")
    box_medium = tk.Canvas(frame_stats, bd=0, bg="#f8c24d")
    box_medium.place(x=30, y=65, anchor="w", width=25, height=25)

    priority_high = tk.Label(frame_stats, text="High: ", font=("Arial", 12, "bold"), anchor="w")
    priority_high.place(x=60, y=105, anchor="w")
    box_high = tk.Canvas(frame_stats, bd=0, bg="#da3535")
    box_high.place(x=30, y=105, anchor="w", width=25, height=25)

    state_pending = tk.Label(frame_stats, text="Pending: ", font=("Arial", 12, "bold"), anchor="w")
    state_pending.place(x=410, y=65, anchor="w")
    box_pending = tk.Canvas(frame_stats, bd=0, bg="#9CA3AF")
    box_pending.place(x=380, y=65, anchor="w", width=15, height=100)

    state_process = tk.Label(frame_stats, text="In process: ", font=("Arial", 12, "bold"), anchor="w")
    state_process.place(x=620, y=65, anchor="w")
    box_process = tk.Canvas(frame_stats, bd=0, bg="#f3cf6b")
    box_process.place(x=590, y=65, anchor="w", width=15, height=100)

    state_resolved = tk.Label(frame_stats, text="Resolved: ", font=("Arial", 12, "bold"), anchor="w")
    state_resolved.place(x=850, y=65, anchor="w")
    box_resolved = tk.Canvas(frame_stats, bd=0, bg="#12a182")
    box_resolved.place(x=820, y=65, anchor="w", width=15, height=100)

    def show_info_dashboard():

        #Obtener datos priority
        low_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["priority"] == "Low":
                low_count += 1
        medium_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["priority"] == "Medium":
                medium_count += 1
        high_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["priority"] == "High":
                high_count += 1

        #Obtener datos state
        pending_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["state"] == "Pending":
                pending_count += 1
        process_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["state"] == "In process":
                process_count += 1
        resolved_count = 0
        for ticket in storage.tickets:
            if storage.tickets[ticket]["state"] == "Resolved":
                resolved_count += 1

        def refresh_labels():
            priority_low.config(text=f"Low: {low_count}")
            priority_medium.config(text=f"Medium: {medium_count}")
            priority_high.config(text=f"High: {high_count}")

            state_pending.config(text=f"Pending: {pending_count}")
            state_process.config(text=f"In process: {process_count}")
            state_resolved.config(text=f"Resolved: {resolved_count}")
            total_tickets.config(text=f"Total tickets: {len(storage.tickets)}")

        def create_graphics():
            
            graphic_priority.delete("all")
            graphic_state.delete("all")

            #Obtener angulos para el grafico
            if len(storage.tickets.keys()) > 0:
                low_angle = low_count / len(storage.tickets.keys()) * 360
                medium_angle = medium_count / len(storage.tickets.keys()) * 360
                high_angle = high_count / len(storage.tickets.keys()) * 360

                start_angle_priority = 90
                graphic_priority.create_arc(20, 30, 170, 180, start=start_angle_priority, extent=high_angle, fill="#DA3535", outline="white", style=tk.PIESLICE)
                start_angle_priority += high_angle
                graphic_priority.create_arc(20, 30, 170, 180, start=start_angle_priority, extent=medium_angle, fill="#f8c42d", outline="white", style=tk.PIESLICE)
                start_angle_priority += medium_angle
                graphic_priority.create_arc(20, 30, 170, 180, start=start_angle_priority, extent=low_angle, fill="#00A035", outline="white", style=tk.PIESLICE)

            else:
                low_angle = medium_angle = high_angle = 0
                graphic_priority.create_arc(20, 20, 170, 170, start=0, extent=359, fill="#5542BE", outline="#5542BE", style=tk.PIESLICE)

            graphic_priority.create_text(245, 105, text="Tickets priority\ndistribution", font=("Arial", 12, "bold"))
            graphic_state.create_text(245, 95, text="Tickets state\ndistribution", font=("Arial", 12, "bold"))


            #Obtener angulos para el grafico
            if len(storage.tickets.keys()) > 0:
                pending_angle = pending_count / len(storage.tickets.keys()) * 360
                process_angle = process_count / len(storage.tickets.keys()) * 360
                resolved_angle = resolved_count / len(storage.tickets.keys()) * 360

                start_angle_state = 90
                graphic_state.create_arc(20, 20, 170, 170, start=start_angle_state, extent=resolved_angle, fill="#12a182", outline="white", style=tk.PIESLICE)
                start_angle_state += resolved_angle
                graphic_state.create_arc(20, 20, 170, 170, start=start_angle_state, extent=process_angle, fill="#f3cf6b", outline="white", style=tk.PIESLICE)
                start_angle_state += process_angle
                graphic_state.create_arc(20, 20, 170, 170, start=start_angle_state, extent=pending_angle, fill="#9CA3AF", outline="white", style=tk.PIESLICE)
            else:
                pending_angle = process_angle = resolved_angle = 0
                graphic_state.create_arc(20, 20, 170, 170, start=0, extent=359, fill="#5542BE", outline="#5542BE", style=tk.PIESLICE)

        create_graphics()
        refresh_labels()

    refresh_home = show_info_dashboard
    
    refresh_home()
    return menu_frame_show, frame_show, canva_show

def show_tickets(frame_show, canva_show):

    global row
    for widget in frame_show.winfo_children():
        widget.destroy()

    #de data.py es importado tickets y en base al ultimo elemento el que es creado se crea visual_tickets 
    for key in storage.tickets:

        visual_ticket = tk.Frame(frame_show, relief="raised", bd=2, width=650, height=90 )
        visual_ticket.grid(row=row, column=0, padx=20, pady=30, sticky="e")

        visual_tickets_dict[key] = visual_ticket

        #IDs
        id_label = tk.Label(visual_ticket, text="ID:")
        id_label.place(relx=0.1, rely=0.15, anchor="center")
        id = tk.Label(visual_ticket, text=f"# {key}", font=("Arial", 10, "bold"), wraplength=144)
        id.place(relx=0.1, rely=0.5, anchor="center")

        #USER
        user_label = tk.Label(visual_ticket, text="User:")
        user_label.place(relx=0.3, rely=0.15, anchor="center")
        user = tk.Label(visual_ticket, text=f"{storage.tickets[key]["user"][:27] + "..." if len(storage.tickets[key]["user"]) > 27 else storage.tickets[key]["user"]}", font=("Arial", 10), wraplength=144)
        user.place(relx=0.3, rely=0.5, anchor="center")

        #PROBLEM
        problem_label = tk.Label(visual_ticket, text="Description:")
        problem_label.place(relx=0.5, rely=0.15, anchor="center")
        problem = tk.Label(visual_ticket, text=f"{storage.tickets[key]["problem"][:33] + "..." if len(storage.tickets[key]["problem"]) > 33 else storage.tickets[key]["problem"]}", font=("Arial", 10), wraplength=164)
        problem.place(relx=0.5, rely=0.5, anchor="center")

        #PRIORITY
        priority = tk.Label(visual_ticket, text=f"{storage.tickets[key]["priority"]}", font=("Arial", 10), anchor="w", wraplength=144)
        priority.place(relx=0.7, rely=0.5, anchor="w")
        priority_box = tk.Canvas(visual_ticket, bd=0)
        match storage.tickets[key]["priority"]:
            case "Low":
                priority_box.configure(bg="#00A035")
            case "Medium":
                priority_box.configure(bg="#f8c24d")
            case "High":
                priority_box.configure(bg="#da3535")
        priority_box.place(relx=0.68, rely=0.5, anchor="center", width=20, height=20)

        #STATE
        state_label = tk.Label(visual_ticket, text=f"{storage.tickets[key]["state"]}", font=("Arial", 10, "bold"), anchor="w", wraplength=144)
        state_label.place(relx=0.9, rely=0.5, anchor="center")
        colors = {
        "Pending": "#9CA3AF",
        "In process": "#f3cf6b",
        "Resolved": "#12a182"
        }
        highlight = tk.Frame(
        visual_ticket,
        bg=colors[storage.tickets[key]["state"]],
        width=8
        )

        highlight.place(
        x=0,
        y=0,
        relheight=1
        )

        state_label_dict[key] = state_label
        row += 1

        canva_show.after(10, lambda:canva_show.yview_moveto(1.0))

        if refresh_home:
            refresh_home()
    return True