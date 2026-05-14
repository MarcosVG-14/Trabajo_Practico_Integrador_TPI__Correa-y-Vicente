
def validar_texto(mensaje_1,mensaje_2=None):
    while True:
        try:
          texto = input(mensaje_1).strip().capitalize()
          if texto.isalpha():
            if mensaje_2:
              print(mensaje_2)
            return texto
          else:
            print("ERROR... El texto solo puede contener letras.")
        except KeyboardInterrupt:
           print("Se interrumpió el programa por el usuario.")
           break
        except Exception as e:
           print(f"Hubo un error inesperado... Error: {e}.")
def validar_entero(mensaje_1,mensaje_2=None):
   while True:
      try:
        numero = int(input(mensaje_1))
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