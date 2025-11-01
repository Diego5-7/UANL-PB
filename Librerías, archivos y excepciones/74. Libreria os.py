import os

carpeta = input("Ingresa el nombre de la carpeta: ")

if os.path.isdir(carpeta):
    archivos = os.listdir(carpeta)
    csvs = [a for a in archivos if a.endswith(".csv")]
    csvs.sort()
    print("\nArchivos CSV encontrados:")
    for archivo in csvs:
        print(archivo)
else:
    print("La carpeta no existe.")
