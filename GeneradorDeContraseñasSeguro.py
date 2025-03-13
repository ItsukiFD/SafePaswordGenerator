import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

while True:
    try:
        longitud = int(input("Ingrese la longitud de la contraseña (mínimo 6): "))
        if longitud < 6:
            print("La longitud mínima es 6 caracteres.")
            continue
        print("Contraseña generada:", generar_contrasena(longitud))
    except ValueError:
        print("Por favor, ingrese un número válido.")

    opcion = input("¿Desea generar otra contraseña? (s/n): ").strip().lower()
    if opcion != 's':
        break
