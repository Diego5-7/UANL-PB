calificacion = float(input("Ingresa tu calificación (0 a 10): "))

if calificacion < 0 or calificacion > 10:
    print("Error: calificación inválida")
elif calificacion < 6:
    print("Irregular")
elif calificacion < 10:
    print("Regular")
else:
    print("Excelencia")
