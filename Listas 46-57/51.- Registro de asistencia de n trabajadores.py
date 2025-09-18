n = int(input("¿Cuántos trabajadores? "))
nombres = []
asistencias = []

for i in range(n):
    nombre = input("Nombre: ")
    
    while True:
        asistencia = int(input("Asistió? 1 sí, 0 no: "))
        if asistencia == 0 or asistencia == 1:
            break
        else:
            print("Error: ingresa solo 0 o 1")
    
    nombres.append(nombre)
    asistencias.append(asistencia)

print("\nAsistencia de los trabajadores:")
for i in range(n):
    if asistencias[i] == 1:
        print(nombres[i], "asistió a trabajar")
    else:
        print(nombres[i], "no asistió a trabajar")
