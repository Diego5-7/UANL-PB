tipo = input("Lista de números (n) o texto (t): ")
lista = []

while True:
    opcion = input("Opciones: agregar, eliminar, ordenar, nueva, buscar, salir: ")
    
    if opcion == "agregar":
        valor = input("Valor: ")
        if tipo == "n":
            valor = float(valor)
        lista.append(valor)

    elif opcion == "eliminar":
        val = input("Valor a eliminar: ")
        if tipo == "n":
            val = float(val)
        if val in lista:
            lista.remove(val)

    elif opcion == "ordenar":
        lista.sort()

    elif opcion == "nueva":
        nueva = sorted(lista)
        print("Lista ordenada nueva:", nueva)

    elif opcion == "buscar":
        val = input("Valor a buscar: ")
        if tipo == "n":
            val = float(val)
        for i in range(len(lista)):
            if lista[i] == val:
                print("Valor encontrado en índice:", i)

    elif opcion == "salir":
        break

    print("Lista actual:", lista)
