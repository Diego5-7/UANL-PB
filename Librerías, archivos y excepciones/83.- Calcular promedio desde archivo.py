try:
    with open("numeros.txt", "r") as f:
        numeros = [float(linea.strip()) for linea in f]
        promedio = sum(numeros) / len(numeros)
        print("Promedio:", promedio)
except FileNotFoundError:
    print("Error: No se encontró 'numeros.txt'.")
except ValueError:
    print("Error: El archivo contiene datos no numéricos.")
except ZeroDivisionError:
    print("Error: El archivo está vacío.")
