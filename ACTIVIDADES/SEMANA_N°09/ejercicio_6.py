# Escribir un programa que pregunte el correo electrónico del usuario en la
# consola y muestre por pantalla otro correo electrónico con el mismo nombre (la
# parte delante de la arroba @) pero con dominio científica.edu.pe

#Entrada:
while True:
    print("="*50)
    correo=input("Ingrese su correo electrónico \n Su repuesta=> ")
    #proceso:
    nombre= correo.split("@")[0]
    nuevo= nombre + "@cientifica.edu.pe"
    #salida:
    print("="*50)
    print("El nuevo correo electrónico es: ", nuevo)
    print("="*50)
    respuesta=input("¿Deseas hacer otro correo electrónico? (si/no) \n Su respuesta => ").lower()
    if respuesta != "si":
        print("¡gracias por usar el programa!")
        break
print("="*50)
print("Elaborado por Esteban Trinidad")
print("="*50)