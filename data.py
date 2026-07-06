import tkinter as tk
import manager_json
from validations import validate_ticket
from notifications import notification_popup, notification_popup_close
import storage 

#Obtiene todos los valores de registro para guardar la informacion
def save_ticket(user_name_entry, problem_text, priority_box, parent):
    
    #crea las IDs
    if storage.tickets:
        max_id = max(int(ticket) for ticket in storage.tickets)
        ticket_id = f"{max_id + 1:04d}"
    else:
        ticket_id = "0000"
    
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
        notification_popup_close(parent, f"A ticket has been created \n\n consult ID: {ticket_id}"),
        id_checked, user_checked, problem_checked, priority_checked = result
        storage.tickets[ticket_id] = {"id": id_checked,
        "user": user_checked,
        "problem": problem_checked,
        "priority": priority_checked,
        "state": "Pending"
       }
        
        manager_json.guardar_tickets()

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