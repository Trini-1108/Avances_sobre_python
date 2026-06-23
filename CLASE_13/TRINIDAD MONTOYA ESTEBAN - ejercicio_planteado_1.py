#Ejercicios en Python:
#Condicionales, Diccionarios y Funciones.
#La Academia de Informática SISAT ofrece cursos de Programación Python con 4 niveles distintos y precios variables según el nivel elegido y la modalidad de estudio (virtual, semipresencial o presencial). 
#Además, algunos estudiantes reciben descuentos especiales según su condición académica. 
#Se requiere calcular el monto final a pagar. 

#Nivel del Curso: 
# Nivel Básico (B) → S/ 300.00 
# Nivel Intermedio (I) → S/ 450.00 
# Nivel Avanzado (A) → S/ 600.00 
# Nivel Experto (E) → S/ 800.00 

#Modalidad de Estudio: 
# Si la modalidad es Virtual (V), descuento del 12%. 
# Si la modalidad es Semipresencial (S), sin cambio. 
# Si la modalidad es Presencial (P), incremento del 10%. 

#Condición Académica: 
# Becado (B) → descuento adicional del 15%. 
# Regular (R) → sin descuento. 
# Destacado (D) → descuento adicional del 8%. 

# Ejemplo: 

#Nivel: I 
#Modalidad: V 
#Condición: D 
#Monto a pagar: S/ 364.32 

#Desarrolle el programa de esta forma: 

# Nivel del curso (B/I/A/E) 
# Modalidad de estudio (V/S/P) 
# Condición académica (B/R/D) 
# Y determine el monto final a pagar. 

#ENTRADA:

precios_por_nivel = {
    "Basico": 300.00,
    "Intermedio": 450.00,
    "Avanzado": 600.00,
    "Experto": 800.00
}
#LO COPIO TAL CUAL DICE EL PROBLEMA, PA NO METERME EN PROBLEMAS LUEGO.

factor_por_modalidad = {
    "Virtual": 0.88,   # (100 - 12)% = 88%
    "Semipresencial": 1.00,  
    "Presencial": 1.10    # (100 + 10)% = 110%
    # NOTA PARA MI: NO SE COLOCA "," AL FINAL. PORQUE SALE ERROR :C
}

factor_por_condicion = {
    "Becado": 0.85,   # (100- 15)% = 85%
    "Regular": 1.00,   
    "Destacado": 0.92    # (100 - 8)% = 92%
}

#PROCESO: 

def obtener_precio_por_nivel(nivel):
    if nivel in precios_por_nivel:
        return precios_por_nivel[nivel]
    else:
        print("Nivel inválido.")
        return None
# SE USA PRIMERO "()", DESPUES "[]", es cuando se usa por funciones.
#GAAA

def aplicar_por_la_modalidad(precio, modalidad):
    if modalidad in factor_por_modalidad:
        return precio * factor_por_modalidad[modalidad]
    else:
        print("Modalidad inválida.")
        return None


def aplicar_por_la_condicion(precio, condicion):
    if condicion in factor_por_condicion:
        return precio * factor_por_condicion[condicion]
    else:
        print("Condición académica inválida.")
        return None


def calcular_monto_final(nivel, modalidad, condicion):
    precio = obtener_precio_por_nivel(nivel)
    if precio is None:
        return

    precio = aplicar_por_la_modalidad(precio, modalidad)
    if precio is None:
        return

    precio = aplicar_por_la_condicion(precio, condicion)
    if precio is None:
        return

    print(f"\n Nivel =>      {nivel}")
    print(f"\n Modalidad =>  {modalidad}")
    print(f"\n Condición =>  {condicion}")
    print(f"\n Monto a pagar => S/ {precio:.3f}")


# SALIDA:
while True:
    print("="*30)
    print("======= Academia SISAT =======")
    print("="*30)

    nivel     = input("Nivel del cursito (Basico /Intermedio /Avanzado /Experto):\n SU REPUESTA => ").capitalize()
    modalidad = input("Modalidad de estudio (Virtual /Semipresencial /Presencial):\n SU REPUESTA => ").capitalize()
    condicion = input("Condición académica (Becado /Regular /Destacado):\n SU REPUESTA => ").capitalize()

#lower: minusculas
#upper: mayusculas
#casefold: mayusculas y minusculas a la vez
#capitalize: Ese era la condicion :,c, pone la primera letra en mayúscula y el resto en minúscula.

    calcular_monto_final(nivel, modalidad, condicion)
    precio = obtener_precio_por_nivel(nivel)
    precio = aplicar_por_la_modalidad(precio, modalidad)
    precio = aplicar_por_la_condicion(precio, condicion)

    print("="*50)
    msg=input("¿Deseas hacer otra operación bro? (si/no)=\n SU REPUESTA  ")
    if msg != "si":
        print("="*50)
        print("====== ¡GRACIAS POR USAR EL PROGRAMA! ======")
        print("="*50)
        print("===== ELABORADO POR ESTEBAN TRINIDAD MONTOYA =====")
        print("="*50)
        break
