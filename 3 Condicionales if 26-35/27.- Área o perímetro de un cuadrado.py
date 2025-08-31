opcion = input("¿Quieres calcular área o perímetro? (escribe 'area' o 'perimetro'): ")
lado = float(input("Ingresa el valor del lado: "))

if opcion == "area":
    print("El área es:", lado * lado)
elif opcion == "perimetro":
    print("El perímetro es:", lado * 4)
else:
    print("Opción no válida")
