"""
EJERCICIO 3: Lista de tareas (To-Do list) en consola
------------------------------------------------------
Crea un programa con un menú que se repite hasta que el usuario elija "Salir":

  1. Agregar tarea
  2. Ver tareas
  3. Marcar tarea como completada
  4. Eliminar tarea
  5. Salir

Guarda las tareas en una lista de diccionarios, por ejemplo:
  {"nombre": "Estudiar Python", "completada": False}

Pistas:
  - Usa una lista vacía tareas = [] al inicio.
  - Usa un bucle while True: para mostrar el menú una y otra vez.
  - Usa input() para leer la opción del menú (como texto: "1", "2", etc.)
  - Para ver las tareas, recorre la lista con un for y muestra si están
    completadas con un [x] o [ ].
  - Para eliminar o marcar, pide el número de la tarea en la lista.
"""


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

        # TODO: completa cada caso del menú usando if/elif
        # opcion == "1" -> agregar tarea nueva a la lista
        # opcion == "2" -> mostrar todas las tareas numeradas
        # opcion == "3" -> pedir número de tarea y marcarla completada
        # opcion == "4" -> pedir número de tarea y eliminarla
        # opcion == "5" -> imprimir "¡Hasta luego!" y terminar el programa (break)
        pass


if __name__ == "__main__":
    main()
