tickets = [
    {
        "id": "0001",
        "cliente": "Eduardo García",
        "asunto": "No puedo iniciar sesión",
        "estado": "Abierto",
        "prioridad": "Alta",
        "tecnico": "Sofía Morales"
    },
    {
        "id": "0002",
        "cliente": "José Siciliano",
        "asunto": "Error al imprimir",
        "estado": "En proceso",
        "prioridad": "Media",
        "tecnico": "Ricardo Flamenco"
    },
    {
        "id": "0003",
        "cliente": "Jaime Cornejo",
        "asunto": "Cambio de contraseña",
        "estado": "Cerrado",
        "prioridad": "Baja",
        "tecnico": "Tatiana Cruz"
    }
]

id_buscar = input("Ingrese el ID del ticket: ").strip().upper()

encontrado = False

for ticket in tickets:
    if ticket["id"] == id_buscar:
        print("\n===== TICKET ENCONTRADO =====")
        print("ID:", ticket["id"])
        print("Cliente:", ticket["cliente"])
        print("Asunto:", ticket["asunto"])
        print("Estado:", ticket["estado"])
        print("Prioridad:", ticket["prioridad"])
        print("Técnico asignado:", ticket["tecnico"])
        encontrado = True
        break

if not encontrado:
    print("\nNo existe un ticket con ese ID.")