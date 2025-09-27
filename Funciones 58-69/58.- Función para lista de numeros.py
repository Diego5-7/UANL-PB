def llenar_lista(n):
    lista = []
    for i in range(n):
        numero = int(input("Ingresa un número: "))
        lista.append(numero)
    return lista

mi_lista = llenar_lista(5)
print("Lista:", mi_lista)
