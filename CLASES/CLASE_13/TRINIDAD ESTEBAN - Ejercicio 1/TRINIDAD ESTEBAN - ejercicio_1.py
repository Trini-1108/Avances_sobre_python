#EJERCICIO 1:

#De frente realizar las preguntas....

    #PREGUNTA 1: Funciones y condicionales.

    #Entrada:

def calcular_promedio(v1, v2, v3):
    promedio = (v1 + v2 + v3) / 3
    return promedio

def determinar_desempeno(promedio):
    if promedio <= 2000:
        return "Bajo"
    elif promedio <= 4000:
        return "Regular"
    elif promedio <= 7000:
        return "Bueno"
    else:
        return "Excelente"

print("=" * 50)
print("==== SISTEMA DE EVALUACIÓN DE VENTAS ====")
print("=" * 50)

nombre = input("Ingrese su nombre de vendedor= \n SU REPUESTA=>  ").capitalize()

print("\n=== Ingrese las ventas ===")
venta_e = int(input("Venta de enero: \n Su REPUESTA=> S/."))
venta_f = int(input("Venta de febrero: \n SU REPUESTA=>  S/."))
venta_m = int(input("Venta de marzo: \n SU REPUESTA=> S/."))

promedio = calcular_promedio(venta_e, venta_f, venta_m)

desempeno = determinar_desempeno(promedio)


print("="*50)
print("==== RESULTADOS ====")
print("=" * 50)
print("Nombre del vendedor:", nombre)
print("Promedio de ventas: $", promedio)
print("Desempeño:", desempeno)
print("=" * 50)

print("¡GRACIAS POR USAR EL PROGRAMA!")
print("ELABORADO POR ESTEBAN TRINIDAD")
