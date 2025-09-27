def reprobados(nombres, calificaciones):
    lista_reprobados = []
    for i in range(len(calificaciones)):
        if calificaciones[i] < 6:
            lista_reprobados.append(nombres[i])
    return lista_reprobados

nombres = ["Diego", "Correa", "Canales", "Alexis"]
calif = [8, 3, 10, 5]
print("Reprobados:", reprobados(nombres, calif))
