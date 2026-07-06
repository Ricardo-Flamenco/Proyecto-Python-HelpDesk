import json
import os
import storage
 
ARCHIVO = "backend.json"
 
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump({"tickets": {}}, archivo, indent=4)
 
def cargar_tickets():
 
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
 
    storage.tickets = datos["tickets"]

def guardar_tickets():
    datos = {
        "tickets": storage.tickets
    }

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)