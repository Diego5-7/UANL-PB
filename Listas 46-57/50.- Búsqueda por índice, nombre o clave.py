productos = ["xbox", "pc", "play"]
claves = [777, 911, 666]
cantidades = [5, 12, 11]

opcion = input("Buscar por (i)ndice, (n)ombre o (c)lave: ")

if opcion == "i":
    indice = int(input("Índice: "))
    print(productos[indice], claves[indice], cantidades[indice])

elif opcion == "n":
    nombre = input("Nombre: ")
    encontrado = False
    for i in range(len(productos)):
        if productos[i] == nombre:
            print(productos[i], claves[i], cantidades[i])
            encontrado = True
    if not encontrado:
        print("Producto no encontrado")

elif opcion == "c":
    clave = int(input("Clave: "))
    encontrado = False
    for i in range(len(claves)):
        if claves[i] == clave:
            print(productos[i], claves[i], cantidades[i])
            encontrado = True
    if not encontrado:
        print("Producto no encontrado")
