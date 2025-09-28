def num_romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

numero = int(input("Ingresa un número entero (1 a 3999): "))

if numero < 1 or numero > 3999:
    print("Error: número fuera de rango (1..3999)")
else:
    romano = num_romano(numero)
    print("Número romano:", romano)