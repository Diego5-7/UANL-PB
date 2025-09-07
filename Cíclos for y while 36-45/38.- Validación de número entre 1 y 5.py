while True:
    numero = int(input("Introduce un número entre 1 y 5: "))
    if 1 <= numero <= 5:
        print(f"El número {numero} es válido.")
        break  
    else:
        print("Número no válido. Debes ingresar un número entre 1 y 5.")
