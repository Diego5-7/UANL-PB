total = 0

while total <= 100000:
    abono = float(input("¿Cantidad a abonar? "))

    if abono < 0:
        print("Error: no se aceptan cantidades negativas.")
    else:
        total += abono

print("Meta alcanzada, total abonado:", total)
