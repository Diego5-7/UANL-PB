materias = []
calificaciones = []

n = int(input("¿Cuántas materias tienes? "))

for i in range(n):
    nombre = input("Nombre de la materia: ")
    cal = float(input("Calificación: "))
    materias.append(nombre)
    calificaciones.append(cal)

print("\nPromedios:")
for i in range(n):
    print(materias[i], calificaciones[i])
