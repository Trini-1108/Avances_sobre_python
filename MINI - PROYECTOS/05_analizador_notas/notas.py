"""
EJERCICIO 5: Analizador de notas
------------------------------------
El usuario ingresa varias notas (de 0 a 20) una por una. Escribe "fin"
para terminar de ingresar notas. Al final, el programa debe mostrar:
  - El promedio
  - La nota más alta
  - La nota más baja
  - Cuántas notas fueron aprobadas (>= 10.5) y cuántas desaprobadas

Pistas:
  - Usa una lista vacía notas = [] para guardar los números.
  - Usa un bucle while True: que pida input() y lo agregue a la lista,
    hasta que el usuario escriba "fin".
  - Funciones útiles: sum(), max(), min(), len()
  - Recorre la lista con un for para contar aprobados/desaprobados.
"""


def main():
    notas = []

    print("Ingresa las notas una por una. Escribe 'fin' para terminar.")

    # TODO:
    # 1. Pide notas en un bucle hasta que el usuario escriba "fin".
    #    Convierte cada nota a float antes de guardarla en la lista.
    # 2. Cuando termine, calcula promedio, nota máxima y nota mínima.
    # 3. Cuenta cuántas notas son >= 10.5 (aprobadas) y cuántas no.
    # 4. Imprime un resumen con todos estos datos.
    pass


if __name__ == "__main__":
    main()
