import re

texto = input("Escribe un texto: ")
prohibidas = ["tonto", "feo"]
for palabra in prohibidas:
    texto = re.sub(palabra, "*" * len(palabra), texto, flags=re.IGNORECASE)

print("Texto censurado:", texto)
