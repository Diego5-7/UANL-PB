productos = ["Takis", "Doritos", "Sabritas", "Chips", "Coca"]
precios = [22, 55, 27, 44, 35]
ventas = [100, 50, 30, 200, 40]

for i in range(5):
    ingreso = precios[i] * ventas[i]
    print(productos[i], "Su precio es de $", precios[i], "El total de ventas fue de", ventas[i],"productos", "Ingreso: $", ingreso)
