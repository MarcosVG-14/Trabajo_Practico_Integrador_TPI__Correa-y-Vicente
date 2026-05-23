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

# Filtar paises
def filtar_paises(lista):
    while True:
        print(''' Elija una opción de filtrado:
        1. Filtrar por continente
        2. Filtrar por rango de población
        3. Filtrar por rango de superficie
        4. Volver al menú principal ''')
        print()
        opcion=input("Ingrese una opción: ").strip()
        print()
        match opcion.lower():
            case "1" | "uno":
                continente = validar_texto("Ingrese el continente para filtrar: ")
                filtrados = [pais for pais in lista if pais["continente"].lower() == continente.lower()]
                if filtrados:
                    mostrar_paises(filtrados)
                else:
                    print(f"No se encontraron países en el continente '{continente}'.")

            case "2" | "dos":
                poblacion_min = validar_entero("Ingrese la población mínima: ")
                poblacion_max = validar_entero("Ingrese la población máxima: ")
                filtrados = [pais for pais in lista if poblacion_min <= pais["poblacion"] <= poblacion_max]
                # acá arriba recorre los paises en la lista y los compara con los valores ingresados por el usuario, si el pais cumple la condicion se agrega a la lista "filtrados"
                if filtrados:
                    mostrar_paises(filtrados)
                else:
                    print(f"No se encontraron países con población entre {poblacion_min} y {poblacion_max}.")

            case "3" | "tres":
                superficie_min = validar_flotante("Ingrese la superficie mínima: ")
                superficie_max = validar_flotante("Ingrese la superficie máxima: ")
                filtrados = [pais for pais in lista if superficie_min <= pais["superficie"] <= superficie_max]
                if filtrados:
                    mostrar_paises(filtrados)
                else:
                    print(f"No se encontraron países con superficie entre {superficie_min} y {superficie_max} km².")

            case "4" | "cuatro":
                print("Volviendo al menú principal...")
                print()
                break
            case _:
                print("Opción inválida. Por favor, ingrese una opción válida.")
                print()

# Funciones auxiliares para ordenar
def clave_nombre(pais):
    return pais["pais"]

def clave_poblacion(pais):
    return pais["poblacion"]

def clave_superficie(pais):
    return pais["superficie"]

# estas funciones buscan la clave que se le asigna a cada país, por ejemplo, la función "clave_nombre" devuelve el valor del nombre del país, 
# nos permite ordenar la lista de países segun nombre, poblacion o superficie

# Funcion para ordenar países
def ordenar_paises(lista):
    while True:
        print(''' Elija una opción de ordenamiento:
        1. Ordenar por nombre
        2. Ordenar por población
        3. Ordenar por superficie
        4. Volver al menú principal ''')
        print()
        opcion = input("Ingrese una opción: ").strip()
        print()

        match opcion.lower():
            case "1" | "uno":
                orden = input("¿Desea orden ascendente (A) o descendente (D)? ").strip().lower()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_nombre, reverse=False)
                else:
                    lista_ordenada = sorted(lista, key=clave_nombre, reverse=True)
                mostrar_paises(lista_ordenada)

            case "2" | "dos":
                orden = input("¿Desea orden ascendente (A) o descendente (D)? ").strip().lower()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_poblacion, reverse=False)
                else:
                    lista_ordenada = sorted(lista, key=clave_poblacion, reverse=True)
                mostrar_paises(lista_ordenada)


            case "3" | "tres":
                orden = input("¿Desea orden ascendente (A) o descendente (D)? ").strip().lower()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_superficie, reverse=False)
                else:
                    lista_ordenada = sorted(lista, key=clave_superficie, reverse=True)
                mostrar_paises(lista_ordenada)

            case "4" | "cuatro":
                print("Volviendo al menú principal...")
                print()
                break

            case _:
                print("Opción inválida. Por favor, ingrese una opción válida.")
                print()
