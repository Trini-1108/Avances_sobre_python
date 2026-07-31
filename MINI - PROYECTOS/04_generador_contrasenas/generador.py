"""
EJERCICIO 4: Generador de contraseñas
------------------------------------------
Crea un programa que le pregunte al usuario la longitud deseada de la
contraseña, y genere una contraseña aleatoria usando letras (mayúsculas
y minúsculas), números y símbolos.

Ejemplo de salida:
  Tu contraseña generada es: aB3$kL9!zQ

Pistas:
  - import random y import string
  - string.ascii_letters -> todas las letras (a-z, A-Z)
  - string.digits -> "0123456789"
  - string.punctuation -> símbolos como !@#$%
  - Junta todos los caracteres posibles en un solo string.
  - Usa random.choice(caracteres) dentro de un bucle for para elegir
    un carácter al azar, tantas veces como la longitud pedida.
  - Une los caracteres elegidos con "".join(lista_de_caracteres)
"""

import random
import string


def generar_contrasena(longitud):
    # TODO: genera y devuelve una contraseña aleatoria de la longitud dada
    pass


def main():
    longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))
    contrasena = generar_contrasena(longitud)
    print(f"Tu contraseña generada es: {contrasena}")


if __name__ == "__main__":
    main()
