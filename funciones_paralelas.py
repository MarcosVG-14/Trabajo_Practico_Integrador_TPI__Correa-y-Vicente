import csv
import os

# ====================================================================================================== #
# ====================================================================================================== #
# ====================================================================================================== #

#Bloque de validaciones

def validar_texto(mensaje_1,mensaje_2=None,mensaje_3=None,permitir_campo_vacio=False):
    while True:
        try:
            texto = input(mensaje_1).capitalize().strip()
            if texto == "":
                if permitir_campo_vacio:
                  if mensaje_3:
                      print(mensaje_3)
                  return None
                else:
                    print("ERROR... Este campo es obligatorio. No puede quedar vacío.")
                    continue
            if texto.replace(" ","").isalpha():
                if mensaje_2:
                  print(mensaje_2)
                return texto
            else:
                print("ERROR... El texto solo puede contener letras y espacios.")
        except KeyboardInterrupt:
           print("Se interrumpió el programa por el usuario.")
           break
        except Exception as e:
           print(f"Hubo un error inesperado... Error: {e}.")

def validar_entero(mensaje_1,mensaje_2=None):
   while True:
      try:
        entrada = input(mensaje_1).strip().lower()
        if entrada == 's':
          return "salir"
        numero = int(entrada)
        if numero < 0:
           print("ERROR... No se permiten números negativos.")
           continue
        if mensaje_2:
          print(mensaje_2)
        return numero
      except ValueError:
        print("ERROR... Por favor ingrese un número entero.")
      except Exception as e:
        print(f"Hubo un error inesperado... Error: {e}.")

def validar_flotante(mensaje_1,mensaje_2=None):
   while True:
      try:
        numero = float(input(mensaje_1))
        if numero < 0:
           print("ERROR... No se permiten números negativos.")
           continue
        if mensaje_2:
          print(mensaje_2)
        return numero
      except ValueError:
        print("ERROR... Por favor ingrese un número válido.")
      except Exception as e:
        print(f"Hubo un error inesperado... Error: {e}.")

# ====================================================================================================== #
# ====================================================================================================== #
# ====================================================================================================== #

#Bloque de manejo de csv

def cargar_archivo():
  lista = []
  try:
    with open("paises.csv", "r", encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo)
      for fila in reader:
        lista.append({
            "pais": fila["pais"],
            "poblacion": int(fila["poblacion"]),
            "superficie": float(fila["superficie"]),
            "continente": fila["continente"],
        }) 
    print("Archivo cargado exitosamente.")
  except FileNotFoundError:
    print("El archivo no existe. Se creará una lista vacía.")
  except PermissionError:
    print("Error... No tenes permiso de lectura en este archivo.")
  return lista

def guardar_archivo(lista):
  try:
    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
      fieldnames = ["pais", "poblacion", "superficie", "continente"]
      writer = csv.DictWriter(archivo, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(lista)
    print("Archivo guardado exitosamente.")
  except FileNotFoundError:
    print("El archivo no existe.")
  except PermissionError:
    print("Error... No tiene permiso para escritura.")

# ====================================================================================================== #
# ====================================================================================================== #
# ====================================================================================================== #

#Bloque de funciones utilizadas en el programa

def imprimir_diccionario(dict,primer_mensaje,segundo_mensaje):
    a = dict.keys()
    b = dict.values()
    lista_a = list(a)
    lista_b = list(b)
    for a, b in dict.items():
        print(f"   {primer_mensaje}: {a}")
        print(f"   {segundo_mensaje}: {b}")
        print(" — "*15)

# Funciones auxiliares para ordenar
def clave_nombre(pais):
    return pais["pais"]

def clave_poblacion(pais):
    return pais["poblacion"]

def clave_superficie(pais):
    return pais["superficie"]

# estas funciones buscan la clave que se le asigna a cada país, por ejemplo, la función "clave_nombre" devuelve el valor del nombre del país, 
# nos permite ordenar la lista de países segun nombre, poblacion o superficie

def mostrar_paises(lista):
    for p in lista:
        print(f"País: {p['pais']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

def continuar():
    print()
    input("""-- Presione cualquier tecla para continuar --
""")

def limpiado_consola():
    if os.name == 'nt': #"nt" representa Windows.
        os.system('cls') 
    else: #Acá si no es windows borra todo igual.
        os.system('clear')