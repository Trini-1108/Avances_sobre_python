# Escribir un programa que pregunte por consola por los productos de un carrito
# de compras, separados por comas, y muestre por pantalla cada uno de los
# productos en una línea distinta.

#Entrada:
while True:
    print("="*50)
    productos= input("Ingrese los productos de un carrito de compras, seprados por comas. \n Por ejemplo => leche, pan, trigo, arroz \n SU RESPUESTA =>  ")

#proceso:
    lista=productos.split(",")

#salida:
    print("="*50)
    print("Los productos del carrito son: ")
    for productos in lista:
        print(productos.strip())
    print("="*50)
    respuesta = input("¿Deseas hacer otra consulta? (si/no) \n Su respuesta => ")
    if respuesta .lower() != "si":
        print("¡Gracias por usar el programa!")
        break
print("="*50)
print("Elaborado por Esteban Trinidad")
print("="*50)
