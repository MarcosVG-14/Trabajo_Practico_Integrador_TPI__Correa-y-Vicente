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
      nuevo_pais={"pais":pais, "poblacion":poblacion, "superficie":superficie, "continente":continente}
      lista.append(nuevo_pais)
      guardar_archivo(lista)
    return lista

#Actualizar datos
def actualizar_datos(lista):
    encontrado = False
    pais=validar_texto("Ingrese el nombre del país: ")
    print()
    for p in lista:
        if p["pais"].capitalize() == pais.capitalize():
            encontrado = True
            while True:
                opcion=input("""Qué dato desea cambiar?
1- Población
2- Superficie
3- Ambos
4- Salir
                
    - """)
                match opcion:
                    case "1":
                        nueva_poblacion=validar_entero("Ingrese el valor de población actualizado: ")
                        p["poblacion"] = nueva_poblacion
                        print("Se ejecutaron los cambios exitosamente!")
                        guardar_archivo(lista)
                        print("Volviendo al menú principal...")
                        print()
                        encontrado = True
                        return lista
                    case "2":
                        nueva_superficie=validar_flotante("Ingrese el valor de superficie actualizado: ")
                        p["superficie"] = nueva_superficie
                        print("Se ejecutaron los cambios exitosamente!")
                        guardar_archivo(lista)
                        print("Volviendo al menú principal...")
                        print()
                        encontrado = True
                        return lista
                    case "3":
                        nueva_poblacion=validar_entero("Ingrese el valor de población actualizado: ")
                        p["poblacion"] = nueva_poblacion
                        print("Población actualizada exitosamente")
                        nueva_superficie=validar_flotante("Ingrese el valor de superficie actualizado: ")
                        p["superficie"] = nueva_superficie
                        print("Superficie actualizada exitosamente")
                        guardar_archivo(lista)
                        print("Volviendo al menú principal...")
                        print()
                        encontrado = True
                        return lista
                    case "4":
                        print("Volviendo al menú principal...")
                        print()
                        encontrado = True
                        break
                    case _:
                        print("Error... Comando incorrecto.")
                        print()
    if not encontrado:
        print(f"El país {pais} no se encuentra cargado en el sistema.")
        print("Volviendo al menú...")
        print()
        return lista
    
#Mostrar estadísticas
def calculo_estadisticas(lista):
    promedio_poblacion = sum(p["poblacion"] for p in lista) / len(lista)
    promedio_superficie = sum(p["superficie"] for p in lista) / len(lista)
    menor_poblacion = min(lista, key=lambda x: x["poblacion"])
    mayor_poblacion = max(lista, key=lambda x: x["poblacion"])
    conteo_continentes = {}
    for p in lista:
        cont = p["continente"]
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1
    opcion=input("""Qué dato es el que desea consultar?
1- País con mayor cantidad de habitantes
2- País con menor cantidad de habitantes
3- Promedio de población
4- """)
    
    
    
    
    
    
    
    
    
    
    print(f""" | ESTADÍSTICAS DEL SISTEMA |
- País con mayor cantidad de habitantes: {mayor_poblacion['pais']} ({mayor_poblacion['poblacion']:,})
- País con menor cantidad de habitantes: {menor_poblacion['pais']} ({menor_poblacion['poblacion']:,})
- Promedio de población: {promedio_poblacion:,.2f} habitantes
- Promedio de superficie: {promedio_superficie:,.2f}km²
- Cantidad de paises por continente:""")
    for continente, total in conteo_continentes.items():
            print(f"  - {continente}: {total}")
    print()

