    #MENÚ
def menu():
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
    #FUNCIONES DE VALIDACIONES

def validar_texto(mensaje_1,mensaje_2):
    while True:
        try:
          texto = input(mensaje_1).strip()
          if texto.isalpha():
            print(mensaje_2)
            return texto
          else:
            print("ERROR... El texto solo puede contener letras.")
        except KeyboardInterrupt:
           print("Se interrumpió el programa por el usuario.")
           break
        except Exception as e:
           print(f"Hubo un error inesperado... Error: {e}.")
        
def validar_entero(mensaje_1,mensaje_2):
   while True:
      try:
        numero = int(input(mensaje_1))
        if numero < 0:
           print("ERROR... No se permiten números negativos.")
           continue
        print(mensaje_2)
        return numero
      except ValueError:
        print("ERROR... Por favor ingrese un número entero.")
      except Exception as e:
        print(f"Hubo un error inesperado... Error: {e}.")
