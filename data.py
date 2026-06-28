import tkinter as tk
from validaciones import validate_ticket
from notifications import notification_popup
import storage

#Obtiene todos los valores de registro para guardar la informacion
def save_ticket(user_name_entry, problem_text, priority_box, parent):

    #crea las IDs
    ticket_id = f"{storage.number:04d}"
    
    #Obtiene lo demas
    user_name = user_name_entry.get()
    problem = problem_text.get("1.0", tk.END).strip()
    priority = priority_box.get()

    result = validate_ticket(ticket_id, user_name, problem, priority)

    #si los datos estan incompletos o vacios rechaza si no agrega toda la informacion a un diccionario
    if result is None:
        return False
    elif result == "Complete forms":
        notification_popup(parent, "Please complete all required fields")
        return False
    else:
        id_checked, user_checked, problem_checked, priority_checked = result
        storage.tickets[ticket_id] = {"id": id_checked,
        "user": user_checked,
        "problem": problem_checked,
        "priority": priority_checked,
        "state": "Pending"
       }

        storage.number += 1
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