import random


def jugar():
    secreto = random.randint(1, 100)
    intentos = 0

    while True:
        numero = int(input("Adivina el número (1-100): "))
        intentos += 1

        if numero < secreto:
            print("Más alto")
        elif numero > secreto:
            print("Más bajo")
        else:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            break


if __name__ == "__main__":
    jugar()
