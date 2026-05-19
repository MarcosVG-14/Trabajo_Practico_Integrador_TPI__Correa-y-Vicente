from funciones_validaciones import *
from funciones import *
#Agregar país
def agregar_pais(lista):
    pais=validar_texto("Ingrese el nombre del país: ")
    if pais in [p["pais"] for p in lista]:
        print("El país ya se encuentra cargado en el sistema.")
        print("Volviendo al menú...")
        print()
        return lista
    else:
      print("Agregando país...")
      poblacion=validar_entero("Ingrese la población del país (Aprox): ","Ingreso exitoso!")
      superficie=validar_flotante("Ingrese la superficie del país (Aprox): ","Ingreso exitoso!")
      continente=validar_texto("Ingrese el continente en el que está ubicado el país: ","Ingreso exitoso!")
      nuevo_pais={"pais":pais, "población":poblacion, "superficie":superficie, "continente":continente}
      lista.append(nuevo_pais)
      guardar_archivo(lista)
    return lista

def mostrar_paises(lista):
    for p in lista:
        print(f"País: {p['pais']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

# Buscar un país por nombre
def buscar_por_nombre(lista):
    busqueda = validar_texto("Ingrese el nombre del país a buscar: ")
    encontrado = False
    for pais in lista:
        if pais["pais"].lower() == busqueda.lower() or pais["pais"].lower().startswith(busqueda.lower()):
            mostrar_paises([pais])
            encontrado = True
            break
    if not encontrado:
      print(f"El país '{busqueda}' no se encuentra en el sistema.")