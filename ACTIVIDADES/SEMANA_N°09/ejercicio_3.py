# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
# donde el prefijo es el código del país +57, y la extensión tiene dos
# dígitos (por ejemplo +57-317724710-56). Escribir un programa que pregunte
# por un número de teléfono con este formato y muestre por pantalla el número
# de teléfono sin el prefijo y la extensión

#Entrada:
while True:
    print("="*80)
    numero_telefono= input("Ingrese un número de teléfono con su prefijo y su extensión. \n (Por ejemplo = +57 - 317724710 - 56) = \n Su Repuesta =>  ")

#proceso:
    print("="*80)
    partes= numero_telefono.split("-")
    numero_sin_prefijo_extension=partes[1]
#salida:
    print(f"El número de teléfono sin el prefijo y la extensión es: {numero_sin_prefijo_extension}")
    print("="*80)
    respuesta = input("\n¿Deseas repetir? (si/no): ").lower()
    if respuesta.lower() != 'si':
        break
print("="*80)
print("Elaborado por Esteban Trinidad")
print("="*80)
