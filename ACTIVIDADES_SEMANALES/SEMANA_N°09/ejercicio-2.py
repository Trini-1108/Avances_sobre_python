# Escribir un programa que permita ingresar un nombre en la consola y
# después muestre por pantalla <NOMBRE> tiene <n> letras, donde
# <NOMBRE> es el nombre y <n> es el número de letras que tienen el nombre.

#Entrada:
print("="*50)
while True:
    print("="*50)
    nombre=input("Ingrese su nombre= \n Su repuesta => ")
    print("="*50)
#Proceso:
    n=len(nombre)

#salida:
    print(f"{nombre} tiene {n} letras")
    respuesta = input("\n¿Deseas repetir? (si/no): ").lower()
    if respuesta.lower() != 'si':
        break
print("="*50)
print("Elaborado por Esteban Trinidad")
print("="*50)
