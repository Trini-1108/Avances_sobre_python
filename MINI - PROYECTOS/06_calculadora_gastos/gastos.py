"""
EJERCICIO 6: Calculadora de gastos personales (con archivo)
----------------------------------------------------------------
Crea un programa con un menú (parecido al ejercicio 3) que permita:

  1. Registrar un gasto (descripción + monto)
  2. Ver todos los gastos y el total gastado
  3. Guardar los gastos en un archivo "gastos.txt"
  4. Salir

Cada gasto se guarda como un diccionario, ej:
  {"descripcion": "Almuerzo", "monto": 15.5}

Pistas:
  - Igual que el ejercicio 3, usa una lista y un bucle while True para el menú.
  - Para el total, usa sum(gasto["monto"] for gasto in gastos)
  - Para guardar en archivo:
      with open("gastos.txt", "w") as archivo:
          for gasto in gastos:
              archivo.write(f"{gasto['descripcion']}: S/ {gasto['monto']}\\n")
  - El archivo se crea en la misma carpeta donde corres el script.
"""


def mostrar_menu():
    print("\n--- Calculadora de gastos ---")
    print("1. Registrar gasto")
    print("2. Ver gastos y total")
    print("3. Guardar en archivo")
    print("4. Salir")


def main():
    gastos = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        # TODO: completa cada caso del menú
        # opcion == "1" -> pedir descripción y monto, agregar a la lista
        # opcion == "2" -> mostrar todos los gastos y la suma total
        # opcion == "3" -> guardar los gastos en "gastos.txt"
        # opcion == "4" -> despedirse y terminar (break)
        pass


if __name__ == "__main__":
    main()
