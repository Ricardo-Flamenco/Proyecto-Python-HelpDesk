tickets = {
    1: {
        "cliente": "Sofía Morales",
        "asunto": "No puede iniciar sesión",
        "descripcion": "El usuario olvidó su contraseña.",
        "estado": "Pendiente"
    },
    2: {
        "cliente": "Ricardo Flamenco",
        "asunto": "Error en impresora",
        "descripcion": "La impresora no responde.",
        "estado": "En proceso"
    },
    3: {
        "cliente": "Eduardo García",
        "asunto": "Instalación de software",
        "descripcion": "Solicita instalar Microsoft Office.",
        "estado": "Resuelto"
    }
}


print(" ACTUALIZACIÓN DE ESTADO DEL TICKET ")


id_ticket = int(input("Ingrese el ID del ticket: "))

if id_ticket in tickets:

    print("\nInformación del ticket")

    print("Cliente:", tickets[id_ticket]["cliente"])
    print("Asunto:", tickets[id_ticket]["asunto"])
    print("Descripción:", tickets[id_ticket]["descripcion"])
    print("Estado actual:", tickets[id_ticket]["estado"])

    print("\nSeleccione el nuevo estado")
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Resuelto")

    opcion = input("Opción: ")

    if opcion == "1":
        tickets[id_ticket]["estado"] = "Pendiente"

    elif opcion == "2":
        tickets[id_ticket]["estado"] = "En proceso"

    elif opcion == "3":
        tickets[id_ticket]["estado"] = "Resuelto"

    else:
        print("\nOpción inválida.")
        exit()

    print("\nEstado actualizado correctamente")
    

    print("ID:", id_ticket)
    print("Cliente:", tickets[id_ticket]["cliente"])
    print("Asunto:", tickets[id_ticket]["asunto"])
    print("Descripción:", tickets[id_ticket]["descripcion"])
    print("Nuevo estado:", tickets[id_ticket]["estado"])

else:
    print("\nEl ticket no existe.")