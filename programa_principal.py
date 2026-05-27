from funciones_paralelas import *
from funciones_programa import *
def menu():
    while True:
        paises = cargar_archivo()
        ANCHO = 55
    
        # --- ENCABEZADO AUTOMÁTICO ---
        print("=" * ANCHO)
        print(f" {'BIBLIOTECA DE PAISES'.center(ANCHO - 2)} ")
        print(f" {'& Gestión de Datos Continentales'.center(ANCHO - 2)} ")
        print("=" * ANCHO)
        
        # --- CUADRO DE OPCIONES DINÁMICO ---
        print("╔" + "═" * (ANCHO - 2) + "╗")
        print(f"║ {'- Menú de Acciones -'.center(ANCHO - 4)} ║")
        print("╠" + "═" * (ANCHO - 2) + "╣")
        print(f"║ {'[1] Añadir un país'.ljust(ANCHO - 4)} ║")
        print(f"║ {'[2] Actualizar datos de un país'.ljust(ANCHO - 4)} ║")
        print(f"║ {'[3] Buscar un país'.ljust(ANCHO - 4)} ║")
        print(f"║ {'[4] Filtrado de países'.ljust(ANCHO - 4)} ║")
        print(f"║ {'[5] Ordenamiento de países'.ljust(ANCHO - 4)} ║")
        print(f"║ {'[6] Estadísticas de países'.ljust(ANCHO - 4)} ║")
        print("║" + " " * (ANCHO - 2) + "║")  # Línea en blanco para respirar
        print(f"║ {'[7] Salir del menú'.ljust(ANCHO - 4)} ║")
        print("╚" + "═" * (ANCHO - 2) + "╝")
        print()
        opcion = input("Ingrese una opción: ").strip().lower()
        print() 
        match opcion:
            case "1" | "uno":
                limpiado_consola()
                cantidad = validar_entero("Cuántos paises desea cargar al sistema (O 'S' para volver al menú): ", "Ingresando al sistema de carga...")
                if cantidad == "salir":
                    print("Volviendo al menú principal...")
                else:
                    agregar_pais(paises, cantidad)
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
                # Mensaje de despedida en Verde
                print("""¡Muchas gracias por usar nuestro sistema!
Hasta luego.""")
                break
            case _:
                print("Error... Comando incorrecto.")
                print()
