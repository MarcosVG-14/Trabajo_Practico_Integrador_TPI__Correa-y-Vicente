from programa_principal import *
from funciones_validaciones import *
from funciones_paralelas import *
from funciones_programa import *
def menu():
    paises = cargar_archivo()
    while True:
        print(" | BIBLIOTECA Y GESTIÓN DE DATOS CONTINENTALES |")
        print(""" - Menú de acciones - 
        1- Añadir un país (Nombre, población, superficie cubierta, continente)
        2- Actualizar población y superficie de un país
        3- Buscar país
        4- Filtrar país ###Acá por continente, rango de población o rango de superficie
        5- Lista de países ###Acá MOSTRAR NO GUARDAR, por nombre, población o por superficie 
        6- Estadísticas ### mayor menor poblacion, promedio de poblacion, promedio de sup, cant de paises por continente
        7- Salir del menú""")
        print()
        opcion=input("Ingrese una opción: ").strip().lower()
        print()
        match opcion:
            case "1" | "uno":
                cantidad=validar_entero("Cuantos países desea cargar al sistema: ")
                agregar_pais(paises,cantidad)
            case "2" | "dos":
                actualizar_datos(paises)
            case "3" | "tres":
                pass
            case "4" | "cuatro":
                pass
            case "5" | "cinco":
                pass
            case "6" | "seis":
                calculo_estadisticas(paises)
            case "7" | "siete":
                print("""Muchas gracias por usar nuestro sistema!
Hasta Luego!""")
                break
            case _:
                print("ERROR... Comando correcto")
                print()

