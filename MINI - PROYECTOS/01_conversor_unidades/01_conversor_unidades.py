def convertir(opcion, valor):
    if opcion == "km-millas":
        return round(valor * 0.621371, 2)
    elif opcion == "kg-libras":
        return round(valor * 2.20462, 2)
    elif opcion == "celsius-fahrenheit":
        return round(valor * 9 / 5 + 32, 2)
    else:
        return "Opción no válida"


def main():
    print("Conversor de unidades")
    print("Opciones: km-millas | kg-libras | celsius-fahrenheit")

    opcion = input("¿Qué quieres convertir? ")
    valor = float(input("Ingresa el valor: "))

    resultado = convertir(opcion, valor)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
