# PREGUNTA 2:
# REGISTRO DE PACIENTES

def mostrar_pacientes(lista):
    print("=== LISTA DE PACIENTES ===")
    for paciente in lista:
        print("=> ", paciente)

# ENTRADA: 
print("=" * 50)
print("==== REGISTRO DE PACIENTES ====")
print("=" * 50)

#PROCESO:
pacientes = []

print("Ingrese los nombres de 6 pacientes: \n SU REPUESTA=> ")

for a in range(6):
    nombre = input(f"Paciente {a + 1}: ")
    pacientes.append(nombre)

print("="* 50)
print("==== LISTA COMPLETA DE PACIENTES ====")
print("=" * 50)
print(pacientes)

print("=" * 50)
print("==== INFORMACIÓN DE PACIENTES ====")
print("=" * 50)
print(f"Cantidad de pacientes: {len(pacientes)}")
print(f"Primer paciente: {pacientes[0]}")
print(f"Último paciente: {pacientes[-1]}")

mostrar_pacientes(pacientes)

#PROCESO:
print("=" * 50)
print("¡GRACIAS POR USAR EL PROGRAMA BRO!")
print("=" * 50)