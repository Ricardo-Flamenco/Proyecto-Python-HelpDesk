from data import tickets
 
def buscar_ticket(id_buscar):
    if id_buscar in tickets:
        return tickets[id_buscar]
    return None