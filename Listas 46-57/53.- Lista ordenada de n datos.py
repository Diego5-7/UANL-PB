lista = []

while True:
    dato = input("Ingresa un dato (o 'no' para terminar): ")
    if dato.lower() == "no":
        break
    lista.append(dato)

lista.sort()
print("Lista ordenada:", lista)
