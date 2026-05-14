import csv

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