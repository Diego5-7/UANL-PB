nombres = ["Pessi", "Diego", "Cristiano"]
ahorros = [500, 2000, 1500000]

for i in range(len(nombres)):
    if ahorros[i] < 1000:
        print(nombres[i], "no tendrás para tu futuro")
    elif ahorros[i] > 1000000:
        print(nombres[i], "ya merito te retiras")
