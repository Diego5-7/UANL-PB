try:
    frase = input("Escribe una frase: ")
    with open("registro.txt", "a") as f:
        f.write(frase + "\n")
    print("Frase añadida correctamente.")
except Exception as e:
    print("Error:", e)
