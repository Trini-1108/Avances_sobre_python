import random
import string


def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


def main():
    longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))
    contrasena = generar_contrasena(longitud)
    print(f"Tu contraseña generada es: {contrasena}")


if __name__ == "__main__":
    main()
