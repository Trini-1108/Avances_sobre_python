#PREGUNTA_1:

#ENTRADA:
def dosrayas(caracter="=", longitud=50):
    print(caracter * longitud)

def promedio(p1, p2, p3):
    resultado = (p1 + p2 + p3) / 3
    return resultado

def nivel(promedio):
    if promedio <= 8:
        return "Deficiente"
    elif promedio <= 12:
        return "Regular"
    elif promedio <= 16:
        return "Bueno"
    else:
        return "Excelente"

# Proceso:
while True:
    dosrayas()
    print("=== BIENVENIDO AL PROGRAMA DE DESPORTISTAS ===")
    dosrayas()

    nombre = input("Ingresa el nombre del deportista:\n  ").capitalize()
    p1 = float(input("Ingresa el puntaje 1: \n"))
    p2 = float(input("Ingresa el puntaje 2: \n"))
    p3 = float(input("Ingresa el puntaje 3: \n"))

    mi_promedio = promedio(p1, p2, p3)
    mi_nivel = nivel(mi_promedio)

#SALIDA:
    print("==== RESULTADO =====")
    print(f"Deportista : {nombre}")
    print(f"Promedio   : {mi_promedio:.2f}")
    print(f"Nivel      : {mi_nivel}")
    dosrayas()

    msg=input("¿Deseas hacer otra operación? (si/no)= \n Su repuesta=>  ").lower()
    if msg != "si":
        dosrayas()
        print("=== ¡GRACIAS POR USAR EL PROGRAMA! ===")
        dosrayas()
        print("ELABORADO POR TRINIDAD ESTEBAN")
        dosrayas()
        break