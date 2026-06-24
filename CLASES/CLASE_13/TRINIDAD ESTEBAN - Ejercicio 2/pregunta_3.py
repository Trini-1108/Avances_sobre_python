# PREGUNTA 3:

#ENTRADA:
def wasa(caracter= "=", longitud=50):
    print(caracter*longitud)

celulares = {
    "Samsung" : 15,
    "Apple"   : 8,
    "Motorola": 12,
    "Xiaomi"  : 18,
    "Honor"   : 10
}
precios=[2800, 5200, 1400, 1900, 1700]

#PROCESO:
marcas= list(celulares.keys())
total= 0
for a in range (len(marcas)):
    cantidad= celulares[marcas[a]]
    precio= precios[a]
    total= total + (cantidad * precio)

wasa()
print(f"Valor del inventario en Total=> \n S/. {total:,} ")
preciomax= precios[0]
marcamax=marcas[0]
for a in range(len(precios)):
    if precios[a] > preciomax:
        preciomax = precios[a]
        marcamax= marcas[a]
print(f"CELULAR MÁS COSTOSO: \n => {marcamax} - S/.{preciomax}")

preciomin = precios[0]
marcamin  = marcas[0]

for a in range(len(precios)):
    if precios[a] < preciomin:
        preciomin = precios[a]
        marcamin  = marcas[a]

print(f"Celular menos costoso: \n => {marcamin} - S/. {preciomin}")

wasa()
print("====== ¡GRACIAS POR USAR EL PROGRAMA! ======")
wasa()
print("ELABORADO POR TRINIDAD ESTEBAN")
wasa()