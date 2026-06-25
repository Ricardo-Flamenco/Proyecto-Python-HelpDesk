from data import tickets
from screen import search_bar
 
def buscar_ticket(id_buscar):
    if id_buscar in tickets:
        return tickets[id_buscar]
    return None