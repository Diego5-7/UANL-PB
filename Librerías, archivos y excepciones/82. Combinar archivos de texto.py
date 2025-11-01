try:
    with open("a.txt", "r") as a, open("b.txt", "r") as b:
        combinado = a.read() + "\n" + b.read()

    with open("combinado.txt", "w") as c:
        c.write(combinado)

    print("Archivos combinados en 'combinado.txt'")
except FileNotFoundError:
    print("Error: Uno de los archivos no existe.")
