from funciones_paralelas import *
ANCHO = 55

# Agregar país
def agregar_pais(lista, cantidad):
    for i in range(cantidad):
        print("╔" + "═" * (ANCHO - 2) + "╗")
        print(f"║ {f"Registrando país n°{i+1} de {cantidad}".center(ANCHO - 4)} ║")
        print("╚" + "═" * (ANCHO - 2) + "╝")
        print()
        pais = validar_texto("Ingrese el nombre del país (O 'Enter' para saltar): ", "", "Carga actual interrumpida.", permitir_campo_vacio=True)
        if pais is None:
            print("-" * ANCHO)
            continue   
        if pais in [p["pais"] for p in lista]:
            print()
            print("┌" + "─" * (ANCHO - 2) + "┐")
            print(f"│ {"El país ya se encuentra en el sistema.".ljust(ANCHO - 4)} │")
            print(f"│ {"Volviendo al menú principal...".ljust(ANCHO - 4)} │")
            print("└" + "─" * (ANCHO - 2) + "┘")
            print()
            continuar()
            limpiado_consola()
            return lista
        else:
            print(f"\n * Agregando datos para: {pais.upper()} *")
            print("-" * ANCHO)
            poblacion = validar_entero("Ingrese la población del país: ", "Ingreso exitoso!")
            superficie = validar_flotante("Ingrese la superficie del país: ", "Ingreso exitoso!")
            while True:
                opcion = input("""Ingrese el continente en el que se encuentra el país: 
1- América
2- Europa
3- África
4- Asia
5- Oceanía
6- Antártida

    - """)
                match opcion:
                    case "1" | "uno":
                        continente = "America"
                        break
                    case "2" | "dos":
                        continente = "Europa"
                        break
                    case "3" | "tres":
                        continente = "Africa"
                        break
                    case "4" | "cuatro":
                        continente = "Asia"
                        break
                    case "5" | "cinco":
                        continente = "Oceania"
                        break
                    case "6" "seis":
                        continente = "Antartida"
                        break
                    case _:
                        print("Error... Ese continente no existe.")
            nuevo_pais = {"pais": pais, "poblacion": poblacion, "superficie": superficie, "continente": continente}
            lista.append(nuevo_pais)
            print()
            print("┌" + "─" * (ANCHO - 2) + "┐")
            print(f"│ {"¡País guardado con éxito!".ljust(ANCHO - 4)} │")
            print("└" + "─" * (ANCHO - 2) + "┘")
            print()
            continuar()
            limpiado_consola()
            guardar_archivo(lista)   
    return lista

# Actualizar datos
def actualizar_datos(lista):
    if not lista:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"Error... Actualmente no hay datos cargados en el sistema.".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
        return lista
    encontrado = False
    pais = validar_texto("Ingrese el nombre del país a modificar: ")
    print()
    for p in lista:
        if p["pais"].capitalize() == pais.capitalize():
            encontrado = True
            while True:
                print("┌" + "─" * (ANCHO - 2) + "┐")
                print(f"│ {f"Modificando datos de: {pais.upper()}".center(ANCHO - 4)} │")
                print("├" + "─" * (ANCHO - 2) + "┤")
                print(f"│ {" [1] Población".ljust(ANCHO - 4)} │")
                print(f"│ {" [2] Superficie".ljust(ANCHO - 4)} │")
                print(f"│ {" [3] Ambos campos".ljust(ANCHO - 4)} │")
                print(f"│ {" [4] Volver sin cambiar".ljust(ANCHO - 4)} │")
                print("└" + "─" * (ANCHO - 2) + "┘")
                print()
                opcion = input("Seleccione una opción: ").strip()
                print() 
                match opcion:
                    case "1":
                        print("-" * ANCHO)
                        nueva_poblacion = validar_entero("Ingrese la nueva población: ")
                        p["poblacion"] = nueva_poblacion
                        print("-" * ANCHO)
                        print("¡Población modificada con éxito!")
                        guardar_archivo(lista)
                        continuar()
                        limpiado_consola()
                        return lista    
                    case "2":
                        print("-" * ANCHO)
                        nueva_superficie = validar_flotante("Ingrese la nueva superficie: ")
                        p["superficie"] = nueva_superficie
                        print("-" * ANCHO)
                        print("¡Superficie modificada con éxito!")
                        guardar_archivo(lista)
                        continuar()
                        limpiado_consola()
                        return lista
                    case "3":
                        print("-" * ANCHO)
                        nueva_poblacion = validar_entero("Ingrese la nueva población: ")
                        p["poblacion"] = nueva_poblacion
                        nueva_superficie = validar_flotante("Ingrese la nueva superficie: ")
                        p["superficie"] = nueva_superficie
                        print("-" * ANCHO)
                        print("¡Ambos campos modificados con éxito!")
                        guardar_archivo(lista)
                        continuar()
                        limpiado_consola()
                        return lista  
                    case "4":
                        print("Volviendo al menú principal...")
                        continuar()
                        limpiado_consola()
                        return lista     
                    case _:
                        print("Error... Comando incorrecto.")
                        print()
                        continuar()
                        limpiado_consola()                    
    if not encontrado:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {f"El país {pais} no se encuentra cargado en el sistema.".ljust(ANCHO - 4)} │")
        print(f"│ {"Volviendo al menú principal...".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
    return lista

# Buscar un país por nombre
def buscar_por_nombre(lista):
    if not lista:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"Error... Actualmente no hay datos cargados en el sistema.".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
        return
    busqueda = validar_texto("Ingrese el nombre del país a buscar: ")
    print()
    encontrado = False
    for pais in lista:
        if pais["pais"].capitalize() == busqueda.capitalize() or pais["pais"].capitalize().startswith(busqueda.capitalize()):
            mostrar_paises([pais])
            encontrado = True
            print("-" * ANCHO)
            continuar()
            limpiado_consola()
            break       
    if not encontrado:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {f"El país {pais} no se encuentra cargado en el sistema.".ljust(ANCHO - 4)} │")
        print(f"│ {'Volviendo al menú principal...'.ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()

# Filtar paises
def filtar_paises(lista):
    if not lista:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"Error... Actualmente no hay datos cargados en el sistema.".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
        return
    while True:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"- Elija una opción de filtrado -".center(ANCHO - 4)} │")
        print("├" + "─" * (ANCHO - 2) + "┤")
        print(f"│ {" [1] Por continente".ljust(ANCHO - 4)} │")
        print(f"│ {" [2] Por rango de población".ljust(ANCHO - 4)} │")
        print(f"│ {" [3] Por rango de superficie".ljust(ANCHO - 4)} │")
        print(f"│ {" [4] Volver al menú principal".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        opcion = input("Ingrese una opción: ").strip()
        limpiado_consola()
        match opcion.lower():
            case "1" | "uno":
                continente = validar_texto("Ingrese el continente: ")
                print()
                filtrados = [pais for pais in lista if pais["continente"].capitalize() == continente.capitalize()]
                if filtrados:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {f"Países en el continente: {continente.upper()}".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(filtrados)
                else:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {f"No se encontraron países en el continente '{continente}.".ljust(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘") 
                print("-" * ANCHO)
                continuar()
                limpiado_consola()   
            case "2" | "dos":
                poblacion_min = validar_entero("Ingrese la población mínima: ")
                poblacion_max = validar_entero("Ingrese la población máxima: ")
                print()
                filtrados = [pais for pais in lista if poblacion_min <= pais["poblacion"] <= poblacion_max]
                # acá arriba recorre los paises en la lista y los compara con los valores ingresados por el usuario, si el pais cumple la condicion se agrega a la lista "filtrados"
                if filtrados:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Resultados por rango de población".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(filtrados)
                else:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {f"No se encontraron países con población entre {poblacion_min} y {poblacion_max}.".ljust(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                print("-" * ANCHO)
                continuar()
                limpiado_consola()
            case "3" | "tres":
                superficie_min = validar_flotante("Ingrese la superficie mínima: ")
                superficie_max = validar_flotante("Ingrese la superficie máxima: ")
                print()
                filtrados = [pais for pais in lista if superficie_min <= pais["superficie"] <= superficie_max]
                if filtrados:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Resultados por rango de superficie".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(filtrados)
                else:
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {f"No se encontraron países con superficie entre {superficie_min} y {superficie_max} km².".ljust(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")     
                print("-" * ANCHO)
                continuar()
                limpiado_consola()
            case "4" | "cuatro":
                print("Volviendo al menú principal...")
                continuar()
                limpiado_consola()
                break   
            case _:
                print("┌" + "─" * (ANCHO - 2) + "┐")
                print(f"│ {"Error... Comando incorrecto.".ljust(ANCHO - 4)} │")
                print("└" + "─" * (ANCHO - 2) + "┘")
                print()
                continuar()
                limpiado_consola()

# Ordenar países
def ordenar_paises(lista):
    if not lista:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"Error... Actualmente no hay datos cargados en el sistema.".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
        return
    while True:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"- Elija una opción de ordenado -".center(ANCHO - 4)} │")
        print("├" + "─" * (ANCHO - 2) + "┤")
        print(f"│ {" [1] Por nombre".ljust(ANCHO - 4)} │")
        print(f"│ {" [2] Por población".ljust(ANCHO - 4)} │")
        print(f"│ {" [3] Por superficie".ljust(ANCHO - 4)} │")
        print(f"│ {" [4] Volver al menú principal".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print() 
        opcion = input("Ingrese una opción: ").strip()
        print()
        match opcion.lower():
            case "1" | "uno":
                orden = input(" -> ¿Desea orden ascendente (A) o descendente (D)?: ").strip().lower()
                print()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_nombre, reverse=False)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Nombre (Ascendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print() 
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                elif orden in ["d", "descendente"]:
                    lista_ordenada = sorted(lista, key=clave_nombre, reverse=True)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Nombre (Descendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                else:
                    print("Error... Comando incorrecto.")
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
            case "2" | "dos":
                orden = input("¿Desea orden ascendente (A) o descendente (D)?: ").strip().lower()
                print()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_poblacion, reverse=False)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Población (Ascendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                elif orden in ["d", "descendente"]:
                    lista_ordenada = sorted(lista, key=clave_poblacion, reverse=True)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Población (Descendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                else:
                    print("Error... Comando incorrecto.")
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola() 
            case "3" | "tres":
                orden = input("¿Desea orden ascendente (A) o descendente (D)?: ").strip().lower()
                print()
                if orden in ["a", "ascendente"]:
                    lista_ordenada = sorted(lista, key=clave_superficie, reverse=False)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Superficie (Ascendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                elif orden in ["d", "descendente"]:
                    lista_ordenada = sorted(lista, key=clave_superficie, reverse=True)
                    print("┌" + "─" * (ANCHO - 2) + "┐")
                    print(f"│ {"Países ordenados por Superficie (Descendente)".center(ANCHO - 4)} │")
                    print("└" + "─" * (ANCHO - 2) + "┘")
                    print()
                    mostrar_paises(lista_ordenada)
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()
                else:
                    print("Error... Comando incorrecto.")
                    print("-" * ANCHO)
                    continuar()
                    limpiado_consola()         
            case "4" | "cuatro":
                print("Volviendo al menú principal...")
                continuar()
                limpiado_consola()
                break
            case _:
                print("Error... Comando incorrecto.")
                print("-" * ANCHO)
                continuar()
                limpiado_consola()

#Mostrar estadísticas
def calculo_estadisticas(lista):
    if not lista:
        print("┌" + "─" * (ANCHO - 2) + "┐")
        print(f"│ {"Error... Actualmente no hay datos cargados en el sistema.".ljust(ANCHO - 4)} │")
        print("└" + "─" * (ANCHO - 2) + "┘")
        print()
        continuar()
        limpiado_consola()
        return
    promedio_poblacion = sum(p["poblacion"] for p in lista) / len(lista)
    promedio_superficie = sum(p["superficie"] for p in lista) / len(lista)
    menor_poblacion = lista[0]
    mayor_poblacion = lista[0]
    for p in lista:
        if p["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = p
        if p["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = p     
    conteo = {} #Bloque para contar continentes
    for p in lista:
        continente = p["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1 
    print("╔" + "═" * (ANCHO - 2) + "╗")
    print(f"║ {"REPORTE ESTADÍSTICO GLOBAL".center(ANCHO - 4)} ║")
    print("╠" + "═" * (ANCHO - 2) + "╣")
    print(f"║ {"[ Máximos y Mínimos ]".center(ANCHO - 4)} ║")
    print(f"║  • Mayor Población: {mayor_poblacion["pais"].upper()}".ljust(ANCHO - 4) + "  ║")
    print(f"║    Habitantes: {mayor_poblacion["poblacion"]:,}".ljust(ANCHO - 4) + "  ║")
    print(f"║  • Menor Población: {menor_poblacion["pais"].upper()}".ljust(ANCHO - 4) + "  ║")
    print(f"║    Habitantes: {menor_poblacion["poblacion"]:,}".ljust(ANCHO - 4) + "  ║")
    print("╠" + "═" * (ANCHO - 2) + "╣")
    print(f"║ {"[ Promedios Generales ]".center(ANCHO - 4)} ║")
    print(f"║  • Población media: {promedio_poblacion:,.2f} hab.".ljust(ANCHO - 4) + "  ║")
    print(f"║  • Superficie media: {promedio_superficie:,.2f} km²".ljust(ANCHO - 4) + "  ║")
    print("╠" + "═" * (ANCHO - 2) + "╣")
    print(f"║ {"[ Cantidad de Países por Continente ]".center(ANCHO - 4)} ║")
    print("╚" + "═" * (ANCHO - 2) + "╝")
    imprimir_diccionario(conteo, "Continente", "Países")
    print("-" * ANCHO)
    continuar()
    limpiado_consola()