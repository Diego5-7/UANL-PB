def sumatoria(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

print("Sumatoria:", sumatoria([1, 3, 6, 10]))

def promedio(lista):
    return sumatoria(lista) / len(lista)

print("Promedio:", promedio([6, 8, 10]))
