from programa_principal import *
from funciones_paralelas import *
from funciones_programa import *
def menu():
    paises = cargar_archivo()
    while True:
        print(" | BIBLIOTECA Y GESTIÓN DE DATOS CONTINENTALES |")
        print(""" - Menú de acciones - 
1- Añadir un país
2- Actualizar datos de un país
3- Buscar un país
4- Filtrado de países
5- Ordenamiento de países
6- Estadísticas de países
7- Salir del menú""")
        print()
        opcion=input("Ingrese una opción: ").strip().lower()
        print()
        match opcion:
            case "1" | "uno":
                limpiado_consola()
                cantidad=validar_entero("Cuántos paises desea cargar al sistema: ","Ingresando al sistema de carga...")
                agregar_pais(paises,cantidad)
            case "2" | "dos":
                limpiado_consola()
                actualizar_datos(paises)
            case "3" | "tres":
                limpiado_consola()
                buscar_por_nombre(paises)
            case "4" | "cuatro":
                limpiado_consola()
                filtar_paises(paises)
            case "5" | "cinco":
                limpiado_consola()
                ordenar_paises(paises)
            case "6" | "seis":
                limpiado_consola()
                calculo_estadisticas(paises)
            case "7" | "siete":
                limpiado_consola()
                print("""Muchas gracias por usar nuestro sistema!
Hasta Luego!""")
                break
            case _:
                print("ERROR... Comando correcto")
                print()

