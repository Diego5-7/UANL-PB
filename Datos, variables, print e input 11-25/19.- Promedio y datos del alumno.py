nombre = input("Ingresa tu nombre: ")
boleta = input("Ingresa tu número de boleta: ")

calificaciones = []
for i in range(5):
    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)

print("\n--- Datos del Alumno ---")
print(f"Nombre: {nombre}")
print(f"Número de boleta: {boleta}")
print(f"Promedio obtenido: {promedio:.2f}")