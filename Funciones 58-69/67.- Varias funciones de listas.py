def ordena_creciente(lista):
    return sorted(lista)

def ordena_decreciente(lista):
    return sorted(lista, reverse=True)

def elimina_por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista.pop(indice)
    else:
        return None

def elimina_por_dato(lista, dato):
    if dato in lista:
        lista.remove(dato)
    return lista

def calcula_estadisticas(lista):
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo


numeros = []

n = int(input("¿Cuántos números quieres ingresar? "))
for i in range(n):
    num = float(input("Número: "))
    numeros.append(num)

print("\nLista original:", numeros)

print("Creciente:", ordena_creciente(numeros))
print("Decreciente:", ordena_decreciente(numeros))

indice = int(input("Índice a eliminar: "))
print("Eliminado:", elimina_por_indice(numeros, indice))
print("Lista actualizada:", numeros)

dato = float(input("Dato a eliminar: "))
print("Lista sin el dato:", elimina_por_dato(numeros, dato))

prom, maximo, minimo = calcula_estadisticas(numeros)
print("Promedio:", prom)
print("Máximo:", maximo)
print("Mínimo:", minimo)

