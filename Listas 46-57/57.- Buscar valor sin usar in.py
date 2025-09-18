lista = [10, 20, 30, 40, 50]
valor = int(input("Valor a buscar: "))
encontrado = False

for i in range(len(lista)):
    if lista[i] == valor:
        print("Valor encontrado en índice:", i)
        encontrado = True

if not encontrado:
    print("Valor no encontrado")
