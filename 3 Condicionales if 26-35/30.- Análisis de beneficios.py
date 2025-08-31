precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad vendida: "))
egresos = float(input("Egresos: "))

ingresos = precio * cantidad

if ingresos < egresos:
    print("La empresa está en pérdidas, no hay ganancias")
elif ingresos == egresos:
    print("La empresa está en punto de equilibrio")
else:
    print("La empresa está generando ganancias")
