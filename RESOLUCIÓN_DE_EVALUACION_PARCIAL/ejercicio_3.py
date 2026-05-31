# Academia de idiomas:
# 1. Entrada:
nivel = input("NIVEL (I/M/A/C): \n").upper()
horario = input("HORARIO (M/T/N): \n ").upper()
edad = int(input("EDAD: \n "))

#2. Proceso:
if nivel == "I":
    precio=250
elif nivel == "M":
    precio = 350
elif nivel == "A":
    precio = 450
elif nivel== "C":
    precio = 600
else:
    print("NIVEL NO VÁLIDO")

#DESCUENTO SEGÚN HORARIO:
if horario == "M":
    precio = precio * 0.90
elif horario == "N":
    precio = precio * 1.15

#DESCUENTO POR EDAD:
if edad < 18:
    precio = precio * 0.95
elif edad > 60:
    precio = precio * 0.92

print(f"Monto a pagar: {precio:.2f} soles")
