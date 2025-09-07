while True:
    numero = float(input("Introduce un número: "))
    
    print(f"El cuadrado de {numero} es {numero ** 2}")
    
    respuesta = input("¿Quieres ingresar otro número? (sí/no): ").lower()
    
    if respuesta != "sí":
        break 