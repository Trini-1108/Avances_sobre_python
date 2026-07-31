def main():
    notas = []

    print("Ingresa las notas una por una. Escribe 'fin' para terminar.")

    while True:
        entrada = input("Nota: ")
        if entrada.lower() == "fin":
            break
        notas.append(float(entrada))

    if not notas:
        print("No ingresaste ninguna nota.")
        return

    promedio = sum(notas) / len(notas)
    aprobadas = 0
    desaprobadas = 0

    for nota in notas:
        if nota >= 10.5:
            aprobadas += 1
        else:
            desaprobadas += 1

    print(f"\nPromedio: {promedio:.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")
    print(f"Aprobadas: {aprobadas}")
    print(f"Desaprobadas: {desaprobadas}")


if __name__ == "__main__":
    main()
