# PREGUNTA 2:

#ENTRADA:
def aña(caracter="=", longitud=50):
    print(caracter * longitud)
def mostrar_ciu(lista):
    print("====== LISTA DE CIUDADES =====")
    print("Lista completa => ")
    for ciudad in lista:
        print(f" - {ciudad}")
    aña()
    print(f"Cantidad de ciudades: \n {len(lista)}")

    print(f"Primera ciudad : \n {lista[0]}")
    print(f"Última ciudad : \n {lista[-1]}")
#PROCESO:
while True:
    aña()
    ciudades=[]
    print("========= Registro de las ciudades =========")
    aña()
    for a in range(1,11):
        ciudad = input(f"Ingresa la ciudad {a}: \n ")
        ciudades.append(ciudad)
    aña()
#SALIDA:
    mostrar_ciu(ciudades)
    aña()
    msg=input("¿Deseas hacer otra lista de ciudades? (si/no): \n SU REPUESTA=> ").lower()
    if msg!="si":
        aña()
        print("====== ¡GRACIAS POR USAR EL PROGRAMA!======")
        aña()
        print("ELABORADO POR TRINIDAD ESTEBAN")
        aña()
        break   