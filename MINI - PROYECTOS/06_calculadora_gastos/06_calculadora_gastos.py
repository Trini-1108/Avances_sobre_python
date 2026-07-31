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

        if opcion == "1":
            descripcion = input("Descripción del gasto: ")
            monto = float(input("Monto: "))
            gastos.append({"descripcion": descripcion, "monto": monto})
            print("Gasto registrado.")

        elif opcion == "2":
            if not gastos:
                print("No hay gastos registrados.")
            for gasto in gastos:
                print(f"- {gasto['descripcion']}: S/ {gasto['monto']}")
            total = sum(gasto["monto"] for gasto in gastos)
            print(f"Total gastado: S/ {total:.2f}")

        elif opcion == "3":
            with open("gastos.txt", "w") as archivo:
                for gasto in gastos:
                    archivo.write(f"{gasto['descripcion']}: S/ {gasto['monto']}\n")
            print("Gastos guardados en gastos.txt")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
