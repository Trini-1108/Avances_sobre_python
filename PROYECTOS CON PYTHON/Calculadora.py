#Hacer una calculadora con operaciones simple: Suma, resta, multiplicación, división,  potencia y raíz cuadrada.
#El usuario deberá ingresar los números y la operación que desea realizar.

print("Usted es bienvenido a la calculadora de python")


print("="*50)
print("(1)= sum")
print("(2)= rest")
print("(3)= mult")
print("(4)= div")
print("="*50)
op = int(input("Ingrese la operación que desea realizar: "))
def calculadora (num1, num2, op):
    if op == 1:
        print(f"El resultado de la suma de {num1} y {num2} es: {num1 + num2}")
    elif op == 2:
        print(f"El resultado de la resta de {num1} y {num2} es: {num1 - num2}")
    elif op == 3:
        print(f"El resultado de la multiplicación de {num1} y {num2} es: {num1 * num2}")
    elif op == 4:
        print(f"El resultado de la división de {num1} y {num2} es: {num1 / num2:.2f}")
    else:
        print("La operación que selecciono es incorrecta, ingresa de nuevo")

variable1 = float(input("Indique el primer número: "))
variable2 = float(input("Indique el segundo numero: "))
calculadora (variable1, variable2, op)

print("="*50)
print("Este proyecto fue realizado por: Trini")
print("="*50)
