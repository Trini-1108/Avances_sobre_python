# Escribir un programa que pida al usuario su peso (en kg) y estatura (en
# metros), calcule el índice de masa corporal y lo almacene en una variable, e
# imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
# es el índice de masa corporal calculado. redondeado con dos decimales.

#Entrada:
while True:
    print("="*50)
    a =float(input("Ingresa tu peso en kilogramos (kg): \n Su repuesta =>  "))
    
    b =float(input("Ingrese su estatura en metros: \n Por ejemplo: 1.40 m \n Su repuesta =>  "))
    print("="*50)

    IMC= a / b**2
    print(f"Tu Índice de Masa Corporal (IMC) es: \n {round(IMC, 2)}")
    rpta= input("\n ¿Deseas calcular otro IMC? (si/no): \n Su Respuesta =>  ").lower()
    print("="*50)
    if rpta.lower() != "si":
        print("="*50)
        print("¡GRACIAS POR USAR EL PROGRAMA IMC!")
        break
print("="*50)
print("Elaborado por Esteban Trinidad")
print("="*50)