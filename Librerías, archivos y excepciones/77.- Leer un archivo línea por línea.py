try:
    with open("entrada.txt", "r") as f:
        for i, linea in enumerate(f, start=1):
            print(f"Línea {i}: {linea.strip()}")
except FileNotFoundError:
    print("Error: El archivo 'entrada.txt' no existe.")
