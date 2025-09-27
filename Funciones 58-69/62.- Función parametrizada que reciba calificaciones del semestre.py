def calificacion_final(c1, c2, c3):
    prom = (c1 + c2 + c3) / 3
    if prom < 6:
        return prom, "Te vas a extra"
    else:
        return prom, "Aprobado"

print(calificacion_final(8, 9, 4))
