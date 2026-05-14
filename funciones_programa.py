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

if __name__=="__main__":
    paises=[]
    agregar_pais(paises)