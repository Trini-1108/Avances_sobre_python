# Escribir un programa que pregunte por consola el precio de un producto en
# dólares con dos decimales y muestre por pantalla el número de dólares y el
# número de céntimos del precio introducido.

#Entrada:
print("="*50)
while True:
    precio=input("Ingrese el precio del producto en dólares con dos decimales \n Por ejemplo = 12.45 \n SU RESPUESTA =>  ")

#Proceso:
    partes=precio.split(".")
    dolares=partes[0]
    centimos=partes[1]
#salida:
    print("="*50)
    print(f"El número de dólares es: {dolares} y el número de centimos es: {centimos}")
    print("="*50)
    respuesta = input("\n¿Deseas repetir? (si/no): ").lower()
    if respuesta.lower() != 'si':
        break
print("="*50)
print("Elaborado por Esteban Trinidad")
print("="*50)