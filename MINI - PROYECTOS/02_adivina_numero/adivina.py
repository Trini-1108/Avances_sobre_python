"""
EJERCICIO 2: Adivina el número
------------------------------------
La computadora elige un número secreto al azar entre 1 y 100.
El usuario debe adivinarlo. Después de cada intento, el programa dice
si el número secreto es "más alto" o "más bajo".
El juego termina cuando el usuario acierta, y muestra cuántos intentos usó.

Pistas:
  - import random
  - random.randint(1, 100) genera un número al azar entre 1 y 100.
  - Usa un bucle while True: y rómpelo con break cuando acierte.
  - Lleva un contador de intentos.
"""

import random


def jugar():
    secreto = random.randint(1, 100)
    intentos = 0

    # TODO:
    # 1. Crea un bucle que siga pidiendo números hasta que acierte.
    # 2. Cada vez que el usuario adivine, suma 1 al contador de intentos.
    # 3. Si el número es menor al secreto, di "más alto".
    # 4. Si el número es mayor al secreto, di "más bajo".
    # 5. Si acierta, felicítalo y muestra el total de intentos, luego termina.
    pass


if __name__ == "__main__":
    jugar()
