#PREGUNTA 4:
def aea(caracter="=", longitud=50):
    print(caracter*longitud)

#ENTRADA:
empleados = {
    "Ana"  : "Ventas",
    "Luis" : "TI",
    "Pedro": "Marketing",
    "María": "Finanzas"
}

#Proceso:

def mostrar(dic):
    aea()
    print("========= LISTA DE LOS EMPLEADOS ========")
    aea()
    for nombre, area in dic.items():
        print(f" {nombre:10} => {area}")
while True:
    aea()
    mostrar(empleados)
    aea()
    nuevo=input("INGRESA UN NUEVO NOMBRE AL EMPLEADO: \n ").lower()
    nuevoarea=input(f"Ingresa el área de {nuevo}: \n ").lower()
    empleados[nuevo]=nuevoarea
    print("HA SIDO AGREGADO CORRECTAMENTE!")
    mostrar(empleados)
    aea()

    modificar= input("INGRESA EL NOMBRE DEL EMPLEADO QUE DESEA MODIFICAR: \n ").lower() 
    if modificar in empleados:
        aea()
        nuevoarea=input(f"INGRESA LA NUEVA ÁREA PARA {modificar}: \n").lower()
        empleados[modificar]= nuevoarea
        print(f"¡¡Ha sido {modificar} actualizado correctamente!!")
    mostrar(empleados)
    aea()

    eliminar = input("INGRESA EL NOMBRE DEL EMPLEADO A ELIMINAR: \n ").lower()

    if eliminar in empleados:
        del empleados[eliminar]
        print(f"¡¡¡Ha sido {eliminar} eliminado correctamente!!!")
        mostrar(empleados)
    aea()
    msg=input("¿Deseas hacer otro Listado? (si/no): \n ").lower()
    msg != "si"
    aea()
    print("¡GRACIAS POR USAR EL PROGRAMA!")
    aea()
    print("ELABORADO POR TRINIDAD ESTEBAN")
    aea()
    break