# Una juguetería tiene mucho éxito en dos de sus productos: payasos y
# muñecas. Suele hacer venta por correo y la empresa de logística les cobra por
# peso de cada paquete así que deben calcular el peso de los payasos y muñecas
# que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada
# muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#Entrada:
while True:
    print("="*50)
    print("===BIENVENIDO AL PROGRAMA DE PAQUETES===")
    print("="*50)

    pesopay= 112
    pesomun= 75
    pay=int(input("INGRESE LA CANTIDAD (EN UNIDADES) DE PAYASOS VENDIDOS: \n Su repuesta => "))
    mun=int(input("INGRESE EL NÚMERO DE MUÑECAS (EN UNIDADES) VENDIDAS: \n Su repuesta =>  "))
    print("="*50)
    peso=(pay*pesopay) + (mun * pesomun)

    print(f"El peso total del paquete es: \n {peso} g")
    print("="*50)

    rpta=input("¿Deseas hacer otro pedido? (si/no) \n Su repuesta: ").lower()
    if rpta != "si":
        print("="*50)
        print("¡GRACIAS POR USAR EL PROGRAMA!")
        break
print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)