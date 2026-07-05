from storage import tickets
from notifications import notification_popup

def validate_ticket(ticket_id, user_name, problem, priority):

    for ticket in tickets:
        if ticket == ticket_id:
            return

    if user_name == "" or problem == "":
        return "Complete forms"

    if priority not in ["High", "Medium", "Low"]:
        return
    
    return ticket_id, user_name, problem, priority

def search_ticket(parent, search_bar):

    ticket_id = search_bar.get().strip()
    if ticket_id == "":
        return

    for ticket in tickets:
        if ticket == ticket_id:
            notification_popup(parent, "Ticket found")
            return ticket

    notification_popup(parent, "Ticket not found")
    return 

def change_status(state_box, search_bar, parent):

    ticket_id = search_bar.get().strip()
    new_status = state_box.get()

    if ticket_id == "":
        notification_popup(parent, "Enter a ticket ID to update it")
        return 

    if new_status not in ["Pending", "In process", "Resolved"]:
        notification_popup(parent, "Invalid status")
        return

    for ticket in tickets:
        if ticket == ticket_id:
            return new_status, parent, ticket

    notification_popup(parent, "Ticket not found")
    return