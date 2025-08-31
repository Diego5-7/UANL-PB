nombre = input("Ingresa el nombre del vendedor: ")
ventas = float(input("Ingresa el volumen de ventas: "))

if ventas < 1000:
    situacion = "Despedido"
elif ventas < 5000:
    situacion = "En periodo de prueba"

elif ventas < 10000:
    situacion = "Bono del 5%"
else:
    situacion = "Bono del 10%"

print(nombre, "tiene la situacion de", situacion)
