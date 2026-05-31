# Escribir un programa que ingrese tu nombre y el apellido en la consola y un
# número entero e imprima por pantalla en líneas distintas tu nombre y
# apellido tantas veces como el número introducido

#Entrada:
while True:

    print("="*50)

    nombre=input("Ingrese su nombre= \n ")
    apellido=input("Ingrese su apellido= \n ")
    numero=int(input("Ingrese un número entero= \n "))

    print("="*50)
#Proceso:
    for a in range(numero):
        print(nombre)
        print(apellido)
    respuesta = input("\n¿Deseas repetir? (si/no): ").lower()
    if respuesta.lower() != "si":
        break

print("="*50)

print("Elaborado por Esteban Trinidad")

print("="*50)
