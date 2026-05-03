from funciones import *
while True:
    print(" | BIBLIOTECA Y GESTIÓN DE DATOS CONTINENTALES |")
    print(""" - Menú de acciones - 
    1- Añadir un país (Nombre, población, superficie cubierta, continente)
    2- Actualizar población y superficie de un país
    3- Buscar país
    4- Filtrar país ###Acá por continente, rango de población o rango de superficie
    5- Lista de países ###Acá por nombre, población o por superficie 
    6- Estadísticas ### mayor menor poblacion, promedio de poblacion, promedio de sup, cant de paises por continente
    7- Salir del menú""")
    print()
    opcion=input("Ingrese una opción: ").strip()
    print()
    match opcion:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("""Muchas gracias por usar nuestro sistema!
Hasta Luego!""")
            break
        case _:
            print("ERROR... Comando correcto")
            print()