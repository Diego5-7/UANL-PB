import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y, 'o-', label="Datos")
plt.title("Gráfica de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.savefig("grafica.png")
plt.show()
