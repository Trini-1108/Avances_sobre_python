def mostrar_menu():
    print("\n--- Lista de tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            tareas.append({"nombre": nombre, "completada": False})
            print("Tarea agregada.")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas.")
            for i, tarea in enumerate(tareas):
                estado = "[x]" if tarea["completada"] else "[ ]"
                print(f"{i + 1}. {estado} {tarea['nombre']}")

        elif opcion == "3":
            indice = int(input("Número de tarea a marcar: ")) - 1
            if 0 <= indice < len(tareas):
                tareas[indice]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número inválido.")

        elif opcion == "4":
            indice = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                eliminada = tareas.pop(indice)
                print(f"Eliminada: {eliminada['nombre']}")
            else:
                print("Número inválido.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
