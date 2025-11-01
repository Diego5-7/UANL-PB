try:
    with open("origen.txt", "r") as origen:
        contenido = origen.read()

    with open("copia.txt", "w") as copia:
        copia.write(contenido)

    print("Archivo copiado correctamente.")
except FileNotFoundError:
    print("Error: El archivo 'origen.txt' no existe.")
