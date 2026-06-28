tickets = []

def register_ticket(ticket_id, user, issue, priority):

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return "Error: Duplicate ID"

    if user == "" or issue == "":
        return "Error: Required fields"

    if priority not in ["High", "Medium", "Low"]:
        return "Error: Invalid priority"

    new_ticket = {
        "id": ticket_id,
        "user": user,
        "issue": issue,
        "priority": priority,
        "status": "Pending"
    }

    tickets.append(new_ticket)
    return "Ticket registered"

def view_tickets():
    return tickets

def search_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return "Ticket not found"

def change_status(ticket_id, new_status):

    if new_status not in ["Pending", "In Progress", "Resolved"]:
        return "Invalid status"

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = new_status
            return "Status updated"

    return "Ticket not found"