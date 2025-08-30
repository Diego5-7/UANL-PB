
x1 = float(input("\nCoordenada x1: "))
y1 = float(input("Coordenada y1: "))
x2 = float(input("Coordenada x2: "))
y2 = float(input("Coordenada y2: "))

pendiente = (y2 - y1) / (x2 - x1)      
b = y1 - pendiente * x1                

print("Pendiente de la recta (m):", pendiente)
print("Ecuación de la recta: y =", pendiente, "x +", b)
