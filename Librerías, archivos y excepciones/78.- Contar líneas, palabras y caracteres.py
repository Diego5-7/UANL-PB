try:
    with open("datos.txt", "r") as f:
        lineas = f.readlines()
        num_lineas = len(lineas)
        num_palabras = sum(len(l.split()) for l in lineas)
        num_caracteres = sum(len(l) for l in lineas)

        print("Lineas:", num_lineas)
        print("Palabras:", num_palabras)
        print("Caracteres:", num_caracteres)
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos.txt'.")