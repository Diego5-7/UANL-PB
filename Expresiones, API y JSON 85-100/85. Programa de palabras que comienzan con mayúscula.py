import re

texto = input("Escribe un texto: ")
palabras = re.findall(r'\b[A-Z][a-zA-Z]*', texto)
print("Palabras con mayúscula:", palabras)
