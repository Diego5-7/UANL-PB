def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

contador = 0
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    print("Factorial:", factorial(numero))
    contador += 1

print("Cantidad de números leídos:", contador)
