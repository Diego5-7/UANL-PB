import re

texto = input("Escribe un texto con fechas: ")
fechas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto)
print("Fechas encontradas:", fechas)
