continuar = "si"

while continuar == "si":
    print("Operaciones: 1) Suma 2) Resta 3) Multiplicación 4) División 5) Exponente 6) Módulo")
    opcion = input("Elige una opción (1-6): ")

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", a + b)
    elif opcion == "2":
        print("Resultado:", a - b)
    elif opcion == "3":
        print("Resultado:", a * b)
    elif opcion == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Error: división entre cero.")
    elif opcion == "5":
        print("Resultado:", a ** b)
    elif opcion == "6":
        print("Resultado:", a % b)
    else:
        print("Opción no válida")

    continuar = input("¿Deseas realizar otra operación? (si/no): ")
