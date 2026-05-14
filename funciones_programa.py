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

