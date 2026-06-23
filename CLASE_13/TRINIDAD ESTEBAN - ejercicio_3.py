#EJERCICIO 3:

#AÑA

#ENTRADA:

libros = {
    "Python":12, "Java":8, "C++":6, "SQL":15, "Linux":10
}

precios=[120,140,150,80,100]

#PROCESO:
print("="*50)
total = 0
a = 0

for libro in libros:
    total = total + libros[libro] * precios[a]
    a+= 1

mayor = max(libros, key=libros.get)

# SALIDA:
print("Valor total del inventario:", total)
print("Libro con mayor stock:", mayor)
print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
