# EJERCICIO 04:
#ENTRADA:
cursos={
    "Algoritmos":"A101",
    "Base de Datos":"B205",
    "Redes":"C301",
    "Python":"D105"
}

print("="*50)
print("=== SISTEMA DE CURSOS ===")
print("="*50)

#PROCESO:

print("===== Cursos disponibles =====")
for curso in cursos:
    print(f"  {curso}: {cursos[curso]}")
print("="*50)

print("===== Agregar curso =====")
nuevo = input("Nombre: \n => ").capitalize()
codigo = input("Código: \n => ").capitalize()
cursos[nuevo] = codigo
print[f"¡Curso {nuevo} agregado!"]

print("="*50)

print("==== Modificar código ====")
curso = input("Curso a modificar: \n => ").capitalize()
if curso in cursos:
    newcod = input(f"Nuevo código para {curso}: \n => ").capitalize()
    cursos[curso] = newcod
    print(f"¡Código actualizado!")
else:
    print(f" Error: {curso} no existe")

print("="*50)

print("==== Eliminar curso =====")
eliminar = input("Curso a eliminar: \n =>  ").capitalize()
if eliminar in cursos:
    del cursos[eliminar]
    print(f"¡Curso {eliminar} eliminado!")
else:
    print(f"Error: {eliminar} no existe")


print("=== RESULTADO FINAL ===")
for curso in cursos:
    print(f"  {curso}: {cursos[curso]}")

print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
