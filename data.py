import tkinter as tk
from tkinter import messagebox

tickets = {}
number = 0

#Obtiene todos los valores de registro para guardar la informacion
def save_ticket(user_name_entry, problem_text, priority_box):

    #crea las IDs
    global number
    ticket_id = f"{number:04d}"
    
    #Obtiene lo demas
    user_name = user_name_entry.get()
    problem = problem_text.get("1.0", tk.END).strip()
    priority = priority_box.get()

    #si los datos estan incompletos o vacios rechaza si no agrega toda la informacion a un diccionario
    if user_name == ""  or problem == "":
        messagebox.showerror("Missing Information", "Please complete all fields") 
        return False
    else:
        tickets[ticket_id] = {"id": ticket_id,
        "user": user_name,
        "problem": problem,
        "priority": priority,
        "state": "pending"
       }

        number += 1
        return True
    
#la estructura del diccionario es:
#   tickets
#   │
#   ├── ticket_id_1
#   │   ├── id
#   │   ├── user
#   │   ├── problem
#   │   ├── priority
#   │   └── state
#   │
#   ├── ticket_id_2
#   │   ├── id
#   │   ├── user
#   │   ├── problem
#   │   ├── priority
#   │   └── state
#   │
#   └── ticket_id_n
#       ├── id
#       ├── user
#       ├── problem
#       ├── priority
#       └── state