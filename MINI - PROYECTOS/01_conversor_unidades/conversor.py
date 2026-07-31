"""
EJERCICIO 1: Conversor de unidades
------------------------------------
Crea un programa que le pregunte al usuario:
  1. Qué quiere convertir (opciones: "km-millas", "kg-libras", "celsius-fahrenheit")
  2. El valor a convertir

Y que imprima el resultado con 2 decimales.

Fórmulas:
  - km a millas:        millas = km * 0.621371
  - kg a libras:         libras = kg * 2.20462
  - celsius a fahrenheit: F = C * 9/5 + 32

Pistas:
  - Usa input() para leer datos.
  - Usa float() para convertir el texto a número.
  - Usa if/elif/else para elegir la fórmula correcta.
  - Usa round(numero, 2) para redondear a 2 decimales.
"""

def convertir(opcion, valor):
    # TODO: completa la lógica de conversión según la opción elegida
    pass


def main():
    print("Conversor de unidades")
    print("Opciones: km-millas | kg-libras | celsius-fahrenheit")

    opcion = input("¿Qué quieres convertir? ")
    valor = float(input("Ingresa el valor: "))

    resultado = convertir(opcion, valor)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
