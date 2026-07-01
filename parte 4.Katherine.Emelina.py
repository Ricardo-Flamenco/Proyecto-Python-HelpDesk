#Entrasda de datos
id_search = int(input("Enter the ID of the ticke to updae:"))

#Busqeda del billete
ticket_found = None
for ticket in ticket_found:
    if ticket["id"] == id_search:
        ticket_found = ticket
        break

    #validacion de existencia
    if ticket_found is None:
        print("Error: The Id entered does not exist.")

        #seleccion del nuevo estado 
    print ("\nSelect the new  status for the ticket:") 
    print("A. Pending")
    print("B. In process")
    print ("C. Result")
    option = input("Chose an option(A-C):")


#Modificacion del diccionario

if option == "A":
    ticket_found["status"] = "Pending"
    print ("Status updated to pending with sucess")
elif option == "B":
    ticket["status"] = "In process"
    print ("Status updated to in process successfuly")
elif option == "C":
    ticket_found["status"] = "Resolved"
    print("Status updated to resolved successfully")
    
    print ("Invalid option.")